// customer/static/js/main.js

// Function to format a number as currency with thousands commas
export const fmt = n => {
    if (isNaN(n) || n === null) {
        return '$0.00';
    }
    // toFixed(2) ensures two decimal places
    // replace adds thousands commas
    return '$' + (Number(n).toFixed(2)).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};