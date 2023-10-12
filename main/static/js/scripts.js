var currentColumn = -1;
var ascending = true;

function sortNumberColumn(columnIndex) {
    var table, rows, switching, i, shouldSwitch;
    table = document.getElementById("my_table");
    switching = true;

    ascending = (currentColumn === columnIndex && ascending) ? false : true;
    currentColumn = columnIndex;

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            var x = parseFloat(rows[i].getElementsByTagName("td")[columnIndex].textContent);
            var y = parseFloat(rows[i + 1].getElementsByTagName("td")[columnIndex].textContent);

            if (ascending) {
                if (x > y) {
                    shouldSwitch = true;
                    break;
                }
            } else {
                if (x < y) {
                    shouldSwitch = true;
                    break;
                }
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

// Функция для сортировки строк
function sortStringColumn(columnIndex) {
    var table, rows, switching, i, shouldSwitch;
    table = document.getElementById("my_table");
    switching = true;

    ascending = (currentColumn === columnIndex && ascending) ? false : true;
    currentColumn = columnIndex;

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            var x = rows[i].getElementsByTagName("td")[columnIndex].textContent.toLowerCase();
            var y = rows[i + 1].getElementsByTagName("td")[columnIndex].textContent.toLowerCase();

            if (ascending) {
                if (x > y) {
                    shouldSwitch = true;
                    break;
                }
            } else {
                if (x < y) {
                    shouldSwitch = true;
                    break;
                }
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}