function renderRowColors() {
    var rows = document.querySelectorAll("tr:not([style*='display: none'])");

    rows.forEach(function(row, index) {
        if (index % 2 === 0) {
            row.style.backgroundColor = "#2c314294";    // $grey-color-light
        }else{
            row.style.backgroundColor = "#1f222e";      // $background-color
        }
    });
}