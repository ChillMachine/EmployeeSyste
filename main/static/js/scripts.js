
var currentColumn = -1;
var ascending = true;


function sortTable(columnIndex) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("my_table");
    switching = true;


    ascending = (currentColumn === columnIndex && ascending) ? false : true;
    currentColumn = columnIndex;

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[columnIndex].textContent.toLowerCase();
            y = rows[i + 1].getElementsByTagName("td")[columnIndex].textContent.toLowerCase();

            if ((ascending && x > y) || (!ascending && x < y)) {
                shouldSwitch = true;
                break;
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}