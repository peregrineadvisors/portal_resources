/****************************************************************************
 * @file cdo_data.ts
 * 
 * This file is responsible for detailing how to load and parse the data
 ****************************************************************************
 * Copyright (c): 2020 Peregrine Advisors
 ****************************************************************************/

/**
 * Interface defining data associated with a CDO
 */
interface cdo {
    agency: {
        name: string;
        abbrv: string;
        image: string;
        ocdo: string;
        data: string;
        goverance?: string;
        website: string;
    },
    name: {
        first: string;
        last: string;
    },
    contact: {
        email: string;
        linkedin: string;
    },
    acting?:boolean;
};


/**
 * Helper function for loading CDO data from properly formatted JSON file
 * @param database_url URL where JSON database file can be loaded
 */
async function getCdoDatabase(database_url: string): Promise<cdo[]> {
    // Load the database file
    let data_json = await fetch(database_url)
                            .then(response => {return response.json()});
    let cdoDatabase:cdo[] = data_json.data;

    return cdoDatabase;
};
