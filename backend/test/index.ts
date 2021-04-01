import { IncomingMessage, ServerResponse } from "http";

var http = require('http');
var fs   = require('fs');
var url  = require('url');

/**
 * Fetches the test_cdo_data.json file
 */
function getJsonData(data_url:string): string {
    return fs.readFileSync(data_url, 'utf8');
}

/**
 * Initiate a server to allow testing the various components
 */
http.createServer(function (req: IncomingMessage, res: ServerResponse) {
    
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.writeHead(200, { 'Content-Type': 'text/html' });
    
    // Figure out which endpoint file we want
    let request_url = url.parse(req.url);

    // Return data based on the endpoint
    switch (request_url.path) {
        // Serve up the cdo test datasets
        case "/cdo_data.json":
            res.end(getJsonData('test/data/test_cdo_data.json'));
            break;
        case "/gov_data.json":
            res.end(getJsonData('test/data/test_gov_data.json'));
            break;
        case "/news_feed.json":
            res.end(getJsonData('../scripts/news_fetch/feed_results.json'));
            break;
        default:
            res.end('{unknown url}');
            break;
    }
}).listen(8080);
