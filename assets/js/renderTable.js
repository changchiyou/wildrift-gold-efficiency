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

        var data_order = 'non-order'
        var costAmountCols = Array.from(table.querySelectorAll("th")).filter(function(th) {
            return th.textContent.trim() === 'Cost' || th.textContent.trim() === 'Amount';
        });
        costAmountCols.forEach(function(col) {
            if (col.getAttribute('data-order') === 'ascending') {
                data_order = 'ascending'
            }
            if (col.getAttribute('data-order') === 'descending') {
                data_order = 'descending'
            }
        });

        rows.forEach(function(row, index) {
            if (!row.classList.contains('active')) {
                var itemIndex = row.querySelector("p.item-index");
                if (itemIndex) {
                    if (data_order === 'non-order') {
                        itemIndex.style.display = 'none';
                    }
                    if (data_order === 'ascending') {
                        itemIndex.style.display = 'block';
                        itemIndex.textContent = '#' + (rows.length - 1 - index);
                    }
                    if (data_order === 'descending') {
                        itemIndex.style.display = 'block';
                        itemIndex.textContent = '#' + index;
                    }
                }
            }
        });
    });
}