// URL Parameters Filter Handler
// Bidirectional sync between URL parameters and filters/stat prices
// Usage examples:
//   ?include=update (show only updated items)
//   ?include=attack-damage,ability-power
//   ?exclude=armor
//   ?price=attack-damage:35.5,ability-power:21.75

(function() {
    'use strict';

    // Parse URL parameters
    function getUrlParams() {
        const params = new URLSearchParams(window.location.search);
        return {
            include: params.get('include'),
            exclude: params.get('exclude'),
            price: params.get('price')
        };
    }

    // Update URL without page reload
    function updateUrl() {
        const params = new URLSearchParams();

        // Collect include filters
        const includeCheckboxes = document.querySelectorAll('input[type="checkbox"].include-filter:checked');
        if (includeCheckboxes.length > 0) {
            const includeStats = Array.from(includeCheckboxes).map(cb =>
                cb.id.replace('include-', '')
            );
            params.set('include', includeStats.join(','));
        }

        // Collect exclude filters
        const excludeCheckboxes = document.querySelectorAll('input[type="checkbox"].exclude-filter:checked');
        if (excludeCheckboxes.length > 0) {
            const excludeStats = Array.from(excludeCheckboxes).map(cb =>
                cb.id.replace('exclude-', '')
            );
            params.set('exclude', excludeStats.join(','));
        }

        // Collect modified stat prices
        const basePriceInputs = document.querySelectorAll('.base-price-input');
        const modifiedPrices = [];
        basePriceInputs.forEach(function(input) {
            if (input.value != input.defaultValue) {
                const parentTd = input.parentElement;
                const classList = Array.from(parentTd.classList);
                const priceClass = classList.find(c => c.startsWith('base-price-'));
                if (priceClass) {
                    const statName = priceClass.replace('base-price-', '');
                    modifiedPrices.push(statName + ':' + input.value);
                }
            }
        });
        if (modifiedPrices.length > 0) {
            params.set('price', modifiedPrices.join(','));
        }

        // Update URL
        const newUrl = params.toString()
            ? window.location.pathname + '?' + params.toString()
            : window.location.pathname;

        window.history.replaceState({}, '', newUrl);
    }

    // Apply filters from URL
    function applyUrlFilters() {
        const params = getUrlParams();
        let filtersApplied = false;

        // Handle stat prices first (before other filters)
        if (params.price) {
            const prices = params.price.split(',');
            prices.forEach(function(priceStr) {
                const [stat, value] = priceStr.split(':');
                if (stat && value) {
                    const input = document.querySelector('.base-price-' + stat + ' .base-price-input');
                    if (input) {
                        input.value = value;
                        filtersApplied = true;
                    }
                }
            });

            // Trigger base price update
            if (filtersApplied && typeof updateBasePrice === 'function') {
                const event = new Event('change');
                document.querySelector('.base-price-input').dispatchEvent(event);
            }
        }

        // Handle include filters (comma-separated)
        if (params.include) {
            const includeStats = params.include.split(',').map(s => s.trim());
            includeStats.forEach(function(stat) {
                const checkbox = document.getElementById('include-' + stat);
                if (checkbox) {
                    checkbox.checked = true;
                    filtersApplied = true;
                }
            });
        }

        // Handle exclude filters (comma-separated)
        if (params.exclude) {
            const excludeStats = params.exclude.split(',').map(s => s.trim());
            excludeStats.forEach(function(stat) {
                const checkbox = document.getElementById('exclude-' + stat);
                if (checkbox) {
                    checkbox.checked = true;
                    filtersApplied = true;
                }
            });
        }

        // If include or exclude filters were applied, trigger toggleElements
        if (params.include || params.exclude) {
            if (typeof toggleElements === 'function') {
                toggleElements();
            }
        }

        // Show clear button if any filters were applied
        if (filtersApplied) {
            const clearAllButton = document.getElementById('clear-all');
            if (clearAllButton) {
                clearAllButton.style.display = 'inline-block';
            }
        }
    }

    // Attach event listeners for real-time URL updates
    function attachUrlUpdateListeners() {
        // Listen to include/exclude checkbox changes
        const includeCheckboxes = document.querySelectorAll('input[type="checkbox"].include-filter');
        const excludeCheckboxes = document.querySelectorAll('input[type="checkbox"].exclude-filter');

        includeCheckboxes.forEach(function(checkbox) {
            checkbox.addEventListener('change', updateUrl);
        });

        excludeCheckboxes.forEach(function(checkbox) {
            checkbox.addEventListener('change', updateUrl);
        });

        // Listen to stat price input changes
        const basePriceInputs = document.querySelectorAll('.base-price-input');
        basePriceInputs.forEach(function(input) {
            input.addEventListener('input', updateUrl);
        });

        // Listen to clear all button
        const clearAllButton = document.getElementById('clear-all');
        if (clearAllButton) {
            clearAllButton.addEventListener('click', function() {
                // Delay to let clearAllFilters() finish
                setTimeout(updateUrl, 10);
            });
        }
    }

    // Initialize
    function init() {
        applyUrlFilters();
        attachUrlUpdateListeners();
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
