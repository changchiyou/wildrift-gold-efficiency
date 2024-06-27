function groupRows(rows) {
    const groups = [];
    let currentGroup = [];
    rows.forEach(row => {
        if (!row.classList.contains('compare')) {
            if (currentGroup.length) groups.push(currentGroup);
            currentGroup = [row];
        } else {
            currentGroup.push(row);
        }
    });
    if (currentGroup.length) groups.push(currentGroup);
    return groups;
}

function sortGroupedRows(groups, index, type, order) {
    groups.sort((groupA, groupB) => {
        const cellA = groupA[0].cells[index].innerText;
        const cellB = groupB[0].cells[index].innerText;
        let valA, valB;

        if (type === 'number') {
            valA = Number(cellA);
            valB = Number(cellB);
        } else if (type === 'percentage') {
            valA = parseFloat(cellA.replace('%', ''));
            valB = parseFloat(cellB.replace('%', ''));
        }

        // First, compare based on the specified type and order
        let comparisonResult;
        if (order === 'asc') {
            comparisonResult = valA > valB ? 1 : -1;
        } else {
            comparisonResult = valA < valB ? 1 : -1;
        }

        // If values are equal based on first comparison, compare by "Item" column
        if (valA === valB) {
            const itemA = groupA[0].cells[0].innerText;
            const itemB = groupB[0].cells[0].innerText;
            comparisonResult = itemA.localeCompare(itemB); // Compare strings based on ASCII order
        }

        return comparisonResult;
    });

    const tbody = groups[0][0].parentNode;
    groups.forEach(group => group.forEach(row => tbody.appendChild(row)));
}

function restoreOriginalOrder(table, originalRows) {
    const tbody = table.querySelector('tbody');
    originalRows.forEach(row => tbody.appendChild(row));
}