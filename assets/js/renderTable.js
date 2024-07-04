function renderRowColors() {
    var tables = document.querySelectorAll("table");

    tables.forEach(function(table) {
        var rows = table.querySelectorAll("tr:not(.compare):not([style*='display: none'])");

        rows.forEach(function(row, index) {
            if (!row.classList.contains('active')) {
                if (index % 2 === 0) {
                    row.style.backgroundColor = "#2c314294";    // $grey-color-light
                } else {
                    row.style.backgroundColor = "#1f222e";      // $background-color
                }
            }
        });
    });
}


function renderRowIndexs() {
    var tables = document.querySelectorAll("table");

    tables.forEach(function(table) {
        var rows = table.querySelectorAll("tr:not(.compare):not([style*='display: none'])");

        rows.forEach(function(row, index) {
            if (!row.classList.contains('active')) {
                var itemIndex = row.querySelector("p.item-index");
                if (itemIndex) {
                    itemIndex.style.display = 'block';
                    itemIndex.textContent = '#' + index;
                }
            }
        });
    });
}