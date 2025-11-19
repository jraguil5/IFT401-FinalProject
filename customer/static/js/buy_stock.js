// Buy Stock Page - Handles stock selection, calculation, and purchase
console.log('buy_stock.js loaded!');
// Get DOM elements
const stockSelect = document.getElementById('stock');
const sharesInput = document.getElementById('shares');
const priceDisplay = document.getElementById('priceDisplay');
const estimatedCost = document.getElementById('estCost');
const cashDisplay = document.getElementById('cashAvail');
const buyButton = document.getElementById('buyBtn');
const balanceWarning = document.getElementById('warnBalance');
const statusMsg = document.getElementById('statusMessage');
const tradeForm = document.getElementById('tradeForm');
const tickerInput = document.getElementById('tradeTickerBuy');
const quantityInput = document.getElementById('tradeQuantityBuy');

// Track user's cash balance
const initialCash = cashDisplay.textContent.replace('$', '').replace(/,/g, '');
let userCash = parseFloat(initialCash) || 0;

// Format number as currency
function formatMoney(amount) {
  return '$' + Number(amount).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Update all calculations when stock or quantity changes
function calculate() {
  const price = parseFloat(stockSelect.value || 0);
  const qty = parseInt(sharesInput.value || 0);
  const total = price * qty;
  
  // Get stock details from selected option
  const selected = stockSelect.options[stockSelect.selectedIndex];
  const ticker = selected?.dataset?.ticker;
  const name = selected?.dataset?.name;
  const opening = parseFloat(selected?.dataset?.opening || 0);
  const high = parseFloat(selected?.dataset?.high || 0);
  const low = parseFloat(selected?.dataset?.low || 0);
  const volume = parseInt(selected?.dataset?.volume || 0);
  
  // Show/hide stock details panel
  const detailsPanel = document.getElementById('stockDetails');
  if (detailsPanel && price > 0 && ticker) {
    detailsPanel.style.display = 'block';
    
    const stockNameEl = document.getElementById('stockName');
    const stockTickerEl = document.getElementById('stockTicker');
    const currentPriceEl = document.getElementById('currentPrice');
    const openingPriceEl = document.getElementById('openingPrice');
    const dayHighEl = document.getElementById('dayHigh');
    const dayLowEl = document.getElementById('dayLow');
    const floatSharesEl = document.getElementById('floatShares');
    const marketCapEl = document.getElementById('marketCap');
    
    if (stockNameEl) stockNameEl.textContent = name || '-';
    if (stockTickerEl) stockTickerEl.textContent = ticker || '-';
    if (currentPriceEl) currentPriceEl.textContent = formatMoney(price);
    if (openingPriceEl) openingPriceEl.textContent = formatMoney(opening);
    if (dayHighEl) dayHighEl.textContent = formatMoney(high);
    if (dayLowEl) dayLowEl.textContent = formatMoney(low);
    if (floatSharesEl) floatSharesEl.textContent = volume.toLocaleString();
    
    // Calculate market cap (price × volume)
    const marketCap = price * volume;
    if (marketCapEl) marketCapEl.textContent = formatMoney(marketCap);
  } else if (detailsPanel) {
    detailsPanel.style.display = 'none';
  }
  
  // Update price and cost displays
  priceDisplay.textContent = formatMoney(price);
  estimatedCost.textContent = formatMoney(total);
  cashDisplay.textContent = formatMoney(userCash);
  
  // Check if user has enough cash
  const hasStock = price > 0;
  const hasQuantity = qty > 0;
  const hasFunds = total <= userCash;
  
  balanceWarning.style.display = (hasStock && hasQuantity && !hasFunds) ? 'block' : 'none';
  buyButton.disabled = !(hasStock && hasQuantity && hasFunds);
}

// Handle buy button click
function executeBuy(e) {
  e.preventDefault();
  
  const price = parseFloat(stockSelect.value || 0);
  const qty = parseInt(sharesInput.value || 0);
  const ticker = stockSelect.options[stockSelect.selectedIndex]?.dataset?.ticker;
  const total = price * qty;
  
  // Validate before submitting
  if (total > userCash || !ticker || qty <= 0) {
    return;
  }
  
  // Set form values
  tickerInput.value = ticker;
  quantityInput.value = qty;
  
  // Disable button and show processing
  buyButton.disabled = true;
  buyButton.textContent = 'Processing...';
  statusMsg.textContent = 'Executing order...';
  statusMsg.style.display = 'block';
  
  // Submit trade
  fetch(tradeForm.action, {
    method: 'POST',
    body: new FormData(tradeForm),
  })
  .then(response => response.json().then(data => ({ 
    status: response.status, 
    body: data 
  })))
  .then(({ status, body }) => {
    if (status === 200) {
      // Success!
      userCash = parseFloat(body.new_cash);
      statusMsg.className = 'warn';
      statusMsg.style.color = 'darkgreen';
      statusMsg.style.background = '#dcfce7';
      statusMsg.style.borderColor = '#bbf7d0';
      statusMsg.textContent = body.message + ` New Cash: ${formatMoney(userCash)}`;
      sharesInput.value = '';
    } else {
      // Failed
      statusMsg.className = 'warn';
      statusMsg.style.color = '#b91c1c';
      statusMsg.style.background = '#fee2e2';
      statusMsg.style.borderColor = '#fecaca';
      statusMsg.textContent = body.error || `Trade failed`;
    }
  })
  .catch(error => {
    statusMsg.className = 'warn';
    statusMsg.style.color = '#b91c1c';
    statusMsg.style.background = '#fee2e2';
    statusMsg.style.borderColor = '#fecaca';
    statusMsg.textContent = 'Network error. Please try again.';
    console.error('Error:', error);
  })
  .finally(() => {
    buyButton.textContent = 'Execute Buy Order';
    sharesInput.value = '';
    calculate();
  });
}

// Set up event listeners
stockSelect.addEventListener('change', calculate);
sharesInput.addEventListener('input', calculate);
buyButton.addEventListener('click', executeBuy);

// Initial calculation
calculate();