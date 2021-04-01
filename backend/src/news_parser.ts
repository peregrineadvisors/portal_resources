/****************************************************************************
 * @file news_parser.ts
 * 
 * This file is responsible for detailing how to load and parse a news feed
 ****************************************************************************
 * Copyright (c): 2021 Peregrine Advisors
 ****************************************************************************/

/**
 * Interface for a single news entry
 */
interface newsItem {
    id: string;
    title: string;
    url: string;
    date: string;
    content_text: string;
}


/**
 * Interface for loading data from recent aggregated news results
 */
async function getNewsFeed(news_feed_url: string): Promise<newsItem[]> {
    // Load the database file
    let data_json = await fetch(news_feed_url)
                            .then(response => {return response.json()});
    console.log(data_json);
    let articleList:newsItem[] = data_json.items;

    return articleList;
};