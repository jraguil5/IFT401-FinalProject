// Buy Stock Page - Modal confirmation added
console.log('buy_stock.js loaded!');

// Get DOM elements
const stockSelect = document.getElementById('stock');
const sharesInput = document.getElementById('shares');
const priceDisplay = document.getElementById('priceDisplay');
const estimatedCost = document.getElementById('estCost');
const cashDisplay = document.getElementById('cashAvail');
const reviewBuyBtn = document.getElementById('reviewBuyBtn');
const balanceWarning = document.getElementById('warnBalance');
const statusMsg = document.getElementById('statusMessage');
const tradeForm = document.getElementById('tradeForm');
const tickerInput = document.getElementById('tradeTickerBuy');
const quantityInput = document.getElementById('tradeQuantityBuy');

// Modal stuff
const modal = document.getElementById('buyConfirmModal');
const confirmBtn = document.getElementById('confirmBuyBtn');
const cancelBtn = document.getElementById('cancelBuyBtn');
const overlay = document.getElementById('buyModalOverlay');
const summary = document.getElementById('buyOrderSummary');

// Track user's cash balance
const initialCash = cashDisplay.textContent.replace('$', '').replace(/,/g, '');
let userCash = parseFloat(initialCash) || 0;

// Format number as currency
function formatMoney(amount) {
  return '$' + Number(amount).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Update calculations when stock or quantity changes
function calculate() {
  const price = parseFloat(stockSelect.value || 0);
  const qty = parseInt(sharesInput.value || 0);
  const total = price * qty;
  
  // Get stock details
  const selected = stockSelect.options[stockSelect.selectedIndex];
  const ticker = selected?.dataset?.ticker;
  const name = selected?.dataset?.name;
  const opening = parseFloat(selected?.dataset?.opening || 0);
  const high = parseFloat(selected?.dataset?.high || 0);
  const low = parseFloat(selected?.dataset?.low || 0);
  const volume = parseInt(selected?.dataset?.volume || 0);
  
  // Show/hide stock details
  const detailsPanel = document.getElementById('stockDetails');
  if (detailsPanel && price > 0 && ticker) {
    detailsPanel.style.display = 'block';
    
    document.getElementById('stockName').textContent = name || '-';
    document.getElementById('stockTicker').textContent = ticker || '-';
    document.getElementById('currentPrice').textContent = formatMoney(price);
    document.getElementById('openingPrice').textContent = formatMoney(opening);
    document.getElementById('dayHigh').textContent = formatMoney(high);
    document.getElementById('dayLow').textContent = formatMoney(low);
    document.getElementById('floatShares').textContent = volume.toLocaleString();
    document.getElementById('marketCap').textContent = formatMoney(price * volume);
  } else if (detailsPanel) {
    detailsPanel.style.display = 'none';
  }
  
  // Update displays
  priceDisplay.textContent = formatMoney(price);
  estimatedCost.textContent = formatMoney(total);
  cashDisplay.textContent = formatMoney(userCash);
  
  // Check if enough cash
  const hasStock = price > 0;
  const hasQuantity = qty > 0;
  const hasFunds = total <= userCash;
  
  balanceWarning.style.display = (hasStock && hasQuantity && !hasFunds) ? 'block' : 'none';
  reviewBuyBtn.disabled = !(hasStock && hasQuantity && hasFunds);
}

// Show confirmation modal
reviewBuyBtn.addEventListener('click', function() {
    console.log('Review button clicked'); // Debug
    
    const price = parseFloat(stockSelect.value || 0);
    const qty = parseInt(sharesInput.value || 0);
    const selected = stockSelect.options[stockSelect.selectedIndex];
    const ticker = selected?.dataset?.ticker;
    const name = selected?.dataset?.name;
    const total = price * qty;
    
    // Make sure everything is valid
    if (!ticker || qty <= 0 || total > userCash) {
        console.log('Validation failed'); // Debug
        return;
    }
    
    // Build the summary
    summary.innerHTML = `
        <p><strong>Stock:</strong> <span>${ticker}</span></p>
        <p><strong>Company:</strong> <span>${name}</span></p>
        <p><strong>Quantity:</strong> <span>${qty} shares</span></p>
        <p><strong>Price per Share:</strong> <span>${formatMoney(price)}</span></p>
        <p class="order-total"><strong>Total Cost:</strong> <span>${formatMoney(total)}</span></p>
    `;
    
    // Show modal
    modal.style.display = 'block';
});

// Confirm button - execute the trade
confirmBtn.addEventListener('click', function() {
    const price = parseFloat(stockSelect.value || 0);
    const qty = parseInt(sharesInput.value || 0);
    const ticker = stockSelect.options[stockSelect.selectedIndex]?.dataset?.ticker;
    const total = price * qty;
    
    // Hide modal
    modal.style.display = 'none';
    
    // Double check validation
    if (total > userCash || !ticker || qty <= 0) {
        return;
    }
    
    // Set form values
    tickerInput.value = ticker;
    quantityInput.value = qty;
    
    // Disable buttons
    confirmBtn.disabled = true;
    reviewBuyBtn.disabled = true;
    reviewBuyBtn.textContent = 'Processing...';
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
            // Success
            userCash = parseFloat(body.new_cash);
            statusMsg.style.color = 'darkgreen';
            statusMsg.style.background = '#dcfce7';
            statusMsg.textContent = body.message + ` New Cash: ${formatMoney(userCash)}`;
            sharesInput.value = '';
        } else {
            // Error
            statusMsg.style.color = '#b91c1c';
            statusMsg.style.background = '#fee2e2';
            statusMsg.textContent = body.error || 'Trade failed';
        }
    })
    .catch(error => {
        statusMsg.style.color = '#b91c1c';
        statusMsg.style.background = '#fee2e2';
        statusMsg.textContent = 'Network error. Please try again.';
        console.error('Error:', error);
    })
    .finally(() => {
        confirmBtn.disabled = false;
        reviewBuyBtn.textContent = 'Review Order';
        sharesInput.value = '';
        calculate();
    });
});

// Cancel button
cancelBtn.addEventListener('click', function() {
    modal.style.display = 'none';
    statusMsg.style.color = '#0369a1';
    statusMsg.style.background = '#e0f2fe';
    statusMsg.textContent = 'Order cancelled';
    statusMsg.style.display = 'block';
    
    setTimeout(function() {
        statusMsg.style.display = 'none';
    }, 3000);
});

// Click outside modal to close
overlay.addEventListener('click', function() {
    modal.style.display = 'none';
});

// Setup listeners
stockSelect.addEventListener('change', calculate);
sharesInput.addEventListener('input', calculate);

// Run initial calculation
calculate();