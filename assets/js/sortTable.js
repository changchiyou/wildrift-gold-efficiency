function sortTable(table, index, type, order) {
    const rows = Array.from(table.querySelectorAll('tbody tr'));
    rows.sort((a, b) => {
        let cellA = a.cells[index].innerText;
        let cellB = b.cells[index].innerText;

        if (type === 'number') {
            cellA = Number(cellA);
            cellB = Number(cellB);
        } else if (type === 'percentage') {
            cellA = parseFloat(cellA.replace('%', ''));
            cellB = parseFloat(cellB.replace('%', ''));
        }

        if (order === 'asc') {
            return cellA > cellB ? 1 : -1;
        } else {
            return cellA < cellB ? 1 : -1;
        }
    });

    rows.forEach(row => table.querySelector('tbody').appendChild(row));
}

function restoreOriginalOrder(table, originalRows) {
    originalRows.forEach(row => table.querySelector('tbody').appendChild(row));
}