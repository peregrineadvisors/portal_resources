/****************************************************************************
 * @file table.ts
 * 
 * This file defines the Table class
 ****************************************************************************
 * Copyright (c): 2020 Peregrine Advisors
 ****************************************************************************/

/**
 * @class Table
 * Defines a simple HTML table constructor
 */
class Table {

    // Variables
    header: Array<string> = [];
    data: Array<Array<any>> = [[]];
    tableClass: string = '';

    constructor(header: Array<string>, data: Array<Array<any>>) {
        this.setHeader(header);
        this.setData(data);
    }

    // Build the actual table
    build() {
        //creates table
        let table = $('<table></table>').addClass(this.tableClass);

        let tr = $('<tr></tr>'); //creates row
        let th = $('<th></th>'); //creates table header cells
        let td = $('<td></td>'); //creates table cells

        // Fill header row
        let header = tr.clone();
        this.header.forEach(d => {
            header.append(th.clone().text(d));
        });

        // Add the header row
        table.append($('<thead></thead>').append(header));

        // Create the table body
        var tbody = $('<tbody></tbody>');

        // Fills out the table body
        this.data.forEach(d => {
            // Create a new row
            var row = tr.clone();
            d.forEach(e => { 
                row.append(td.clone().html(e));
            });

            // Put the row into the table body
            tbody.append(row);
        })

        // Put the table in the div
        $('#cdo_directory').append(table.append(tbody));

        return this;
    }

    // Set the row data for the table
    setData(data: Array<Array<any>>) {
        this.data = data;
        return this;
    }

    // Set the header data for the table
    setHeader(keys: Array<string>) {
        this.header = keys;
        return this;
    }

    // Set the class name of the table (for CSS formatting)
    setTableClass(tableClass: string) {
        this.tableClass = tableClass;
    }

}