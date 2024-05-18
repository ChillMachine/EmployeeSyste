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

        // Determine the last row index based on whether it contains <th> or <td>
        var lastRowIndex = rows[rows.length - 1].getElementsByTagName("th").length ? rows.length - 1 : rows.length;

        // Loop through all rows (except the header row and the last row, if it's a form row)
        for (i = 1; i < lastRowIndex - 1; i++) {
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

function sortDateColumn(columnIndex) {
    var table, rows, switching, i, shouldSwitch;
    table = document.getElementById("my_table");
    switching = true;

    ascending = (currentColumn === columnIndex && ascending) ? false : true;
    currentColumn = columnIndex;

    while (switching) {
        switching = false;
        rows = table.rows;

        // Determine the last row index based on whether it contains <th> or <td>
        var lastRowIndex = rows[rows.length - 1].getElementsByTagName("th").length ? rows.length - 1 : rows.length;

        // Loop through all rows (except the header row and the last row, if it's a form row)
        for (i = 1; i < lastRowIndex - 1; i++) {
            shouldSwitch = false;
            var x = parseDate(rows[i].getElementsByTagName("td")[columnIndex].textContent.trim());
            var y = parseDate(rows[i + 1].getElementsByTagName("td")[columnIndex].textContent.trim());

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

function parseDate(dateString) {
    // Пример строки: "7 июля 2015 г."
    var months = {
        'января': 0, 'февраля': 1, 'марта': 2, 'апреля': 3, 'мая': 4, 'июня': 5,
        'июля': 6, 'августа': 7, 'сентября': 8, 'октября': 9, 'ноября': 10, 'декабря': 11
    };
    var parts = dateString.split(' ');
    var day = parseInt(parts[0]);
    var month = months[parts[1]];
    var year = parseInt(parts[2]);
    return new Date(year, month, day);
}