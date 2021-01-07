"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
/****************************************************************************
 * @file cdo_data.ts
 *
 * This file is responsible for detailing how to load and parse the data
 ****************************************************************************
 * Copyright (c): 2020 Peregrine Advisors
 ****************************************************************************/
;
/**
 * Helper function for loading CDO data from properly formatted JSON file
 * @param database_url URL where JSON database file can be loaded
 */
function getCdoDatabase(database_url) {
    return __awaiter(this, void 0, void 0, function () {
        var data_json, cdoDatabase;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, fetch(database_url)
                        .then(function (response) { return response.json(); })];
                case 1:
                    data_json = _a.sent();
                    cdoDatabase = data_json.data;
                    return [2 /*return*/, cdoDatabase];
            }
        });
    });
}
;
/****************************************************************************
 * @file gov_data.ts
 *
 * This file is responsible for detailing how to load and parse the data
 * aggregated from data.gov.
 ****************************************************************************
 * Copyright (c): 2020 Peregrine Advisors
 ****************************************************************************/
;
/**
 * Helper function for loading recently uploaded data to data.gov from
 * properly formatted JSON file
 * @param database_url URL where JSON file can be loaded
 * @returns Promise<recent_gov[]>
 */
function getRecentGov(database_url) {
    return __awaiter(this, void 0, void 0, function () {
        var data_json, cdoDatabase;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, fetch(database_url)
                        .then(function (response) { return response.json(); })];
                case 1:
                    data_json = _a.sent();
                    cdoDatabase = data_json.data;
                    return [2 /*return*/, cdoDatabase];
            }
        });
    });
}
;
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
var Table = /** @class */ (function () {
    function Table(header, data) {
        // Variables
        this.header = [];
        this.data = [[]];
        this.tableClass = '';
        this.setHeader(header);
        this.setData(data);
    }
    // Build the actual table
    Table.prototype.build = function () {
        //creates table
        var table = $('<table></table>').addClass(this.tableClass);
        var tr = $('<tr></tr>'); //creates row
        var th = $('<th></th>'); //creates table header cells
        var td = $('<td></td>'); //creates table cells
        // Fill header row
        var header = tr.clone();
        this.header.forEach(function (d) {
            header.append(th.clone().text(d));
        });
        // Add the header row
        table.append($('<thead></thead>').append(header));
        // Create the table body
        var tbody = $('<tbody></tbody>');
        // Fills out the table body
        this.data.forEach(function (d) {
            // Create a new row
            var row = tr.clone();
            d.forEach(function (e) {
                row.append(td.clone().html(e));
            });
            // Put the row into the table body
            tbody.append(row);
        });
        // Put the table in the div
        $('#cdo_directory').append(table.append(tbody));
        return this;
    };
    // Set the row data for the table
    Table.prototype.setData = function (data) {
        this.data = data;
        return this;
    };
    // Set the header data for the table
    Table.prototype.setHeader = function (keys) {
        this.header = keys;
        return this;
    };
    // Set the class name of the table (for CSS formatting)
    Table.prototype.setTableClass = function (tableClass) {
        this.tableClass = tableClass;
    };
    return Table;
}());
