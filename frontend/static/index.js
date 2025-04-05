let allOnuData = [];
let currentSortColumn = 'IntfName';
let currentSortDirection = 'desc';

function fetchOnuFullData() {
    fetch('/getOnuFullData')
        .then(res => res.json())
        .then(json => {
            allOnuData = json;
            sortTableBy(currentSortColumn);
        })
        .catch(console.error);
}

function sortTableBy(column) {
    currentSortDirection = currentSortColumn === column && currentSortDirection === 'asc' ? 'desc' : 'asc';
    currentSortColumn = column;

    const sorted = [...allOnuData].sort((a, b) => compareValues(a[column], b[column], column));
    renderOnuTable(sorted);
}

function compareValues(aVal, bVal, column) {
    if (column === 'IntfName') {
        const [a1, a2] = parseIntfName(aVal);
        const [b1, b2] = parseIntfName(bVal);
        return currentSortDirection === 'asc' ? a1 - b1 || a2 - b2 : b1 - a1 || b2 - a2;
    }

    const valA = (aVal ?? '').toString().toUpperCase();
    const valB = (bVal ?? '').toString().toUpperCase();

    if (valA < valB) return currentSortDirection === 'asc' ? -1 : 1;
    if (valA > valB) return currentSortDirection === 'asc' ? 1 : -1;
    return 0;
}

function parseIntfName(str) {
    const match = str?.match(/(\d+)\/(\d+):(\d+)/);
    return match ? [parseInt(match[2]), parseInt(match[3])] : [0, 0];
}

function renderOnuTable(data) {
    const container = document.getElementById('onuTableContainer');
    if (!container) return;

    const headers = Object.keys(data[0] || {});
    const thead = headers.map(h => `<th style="cursor:pointer; white-space:nowrap;" onclick="sortTableBy('${h}')">${h}</th>`).join('');

    const rows = data.map(row => {
        const cells = headers.map(h => {
            const val = row[h] ?? 'отсутствует';
            const text = getCellText(h, val);
            return `<td style="white-space:nowrap;">${text}</td>`;
        }).join('');
        return `<tr>${cells}</tr>`;
    }).join('');

    container.innerHTML = `<table class="table table-hover">
        <thead class="table-light"><tr>${thead}</tr></thead>
        <tbody>${rows}</tbody>
    </table>`;
}

function getCellText(column, value) {
    return column === 'IntfName' ? value.toUpperCase() : value;
}
