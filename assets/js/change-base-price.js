// Declare updateBasePrice as a global function so it can be called from url-params-filter.js
window.updateBasePrice = null;

document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.base-price-input');
    let basePriceDict = {};

    function updateBasePriceInternal() {
        basePriceDict = {};
        inputs.forEach(function(input) {
            const parentTd = input.parentElement;
            const parentClassList = parentTd.classList;
            parentClassList.forEach(function(classItem) {
                if (classItem.startsWith('base-price-')) {
                    const key = classItem.substring('base-price-'.length);
                    const value = input.value;
                    basePriceDict[key] = value;
                }
            });
        });
        console.log(basePriceDict);

        const itemRows = document.querySelectorAll('tr.item-row');
        itemRows.forEach(function(row) {
            const itemPriceElement = row.querySelector('td.item-price div');
            const itemPriceText = itemPriceElement.textContent.trim().split(' ')[0];
            const itemPrice = parseFloat(itemPriceText);

            let totalValue = 0;
            const statsElements = row.querySelectorAll('b.stat');
            let formula = '(';

            statsElements.forEach(function(statElement, index) {
                const classList = statElement.classList;
                classList.forEach(function(className) {
                    const statValue = parseFloat(statElement.textContent);
                    if (basePriceDict[className]) {
                        const baseValue = basePriceDict[className];
                        totalValue += statValue * baseValue;

                        formula += `${statValue}*${baseValue}`;
                        if (index < statsElements.length - 1) {
                            formula += '+';
                        }
                    }
                });
            });

            formula += `)/${itemPrice}`;

            const newRatio = (totalValue / itemPrice * 100).toFixed(2) + '%';
            const tooltipElement = row.querySelector('.tooltip.item.toleft');
            tooltipElement.innerHTML = `${newRatio}<span class="tooltiptext">${formula}</span>`;
        });
    }

    // Expose the function globally
    window.updateBasePrice = updateBasePriceInternal;

    inputs.forEach(function(input) {
        input.addEventListener('change', updateBasePriceInternal);
    });
});
