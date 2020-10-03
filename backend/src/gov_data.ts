/****************************************************************************
 * @file gov_data.ts
 * 
 * This file is responsible for detailing how to load and parse the data
 * aggregated from data.gov. 
 ****************************************************************************
 * Copyright (c): 2020 Peregrine Advisors
 ****************************************************************************/

/**
 * Interface for loading data from recent aggregated data.gov results
 */
interface recent_gov {
    metadata_modified: string;
    organization: string;
    name: string;
    title: string;
    org_type: string;
    org_title: string;
};


/**
 * Helper function for loading recently uploaded data to data.gov from 
 * properly formatted JSON file
 * @param database_url URL where JSON file can be loaded
 * @returns Promise<recent_gov[]>
 */
async function getRecentGov(database_url: string): Promise<recent_gov[]> {
    // Load the database file
    let data_json = await fetch(database_url)
                            .then(response => {return response.json()});
    let cdoDatabase:recent_gov[] = data_json.data;

    return cdoDatabase;
};