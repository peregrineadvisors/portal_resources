import sys
import os
import argparse
import json
from datetime import datetime, timedelta

# Add the directory containing the peregrine portal module
sys.path.append(os.path.curdir + '../')
import peregrineportal as pp


def get_orgs():
    # Load the organization information
    orgs = pp.Organizations()
    return orgs.orgs


def get_recent(min_date):
    # Load the most recently saved data
    datasets = pp.DataSets(fetch_size=1000)
    datasets = datasets.fetch_recent(min_date=min_date)

    # Get the organization data
    org_data = get_orgs()

    # Assemble the final data objects
    result = []
    for data in datasets.values():
        org = data['organization']['name']
        result.append({
            'metadata_modified': data['metadata_modified'],
            'organization': org,
            'name': data['name'],
            'title': data['title'],
            'org_type': org_data[org]['organization_type'],
            'org_title': org_data[org]['title']
        })

    return result


def load_cache(cache_file):
    """
    """
    # Load data from a pre-saved datafile
    cache = {}
    try:
        with open(cache_file, 'r') as fl:
            cache = json.load(fl)
    except:
        cache['modified_date'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        cache['description'] = 'Recent data.gov dataset updates'
        cache['data'] = list()

    return cache


def write(data, filename):
    """
    """
    # Update the modified date
    data['modified_date'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    # Write the data to a json formatted file
    with open(filename, 'w') as fl:
        json.dump(data, fl)


def process_data(data, min_date):
    # Keep track of when the most recent result was obtained
    last_date = min_date

    # Loop through all existing datasets
    for d in range(len(data['data'])-1, -1, -1):
        dset = data['data'][d]
        dset_date = datetime.fromisoformat(dset['metadata_modified'])

        # If the data is too long ago, remove it
        if dset_date < min_date:
            data['data'].pop(d)
        # Check if this is from a later date
        elif dset_date > last_date:
            last_date = dset_date

    return last_date


def update_cache(filename, min_date):
    # Get previous results
    data = load_cache(opts.cache_file)

    # Pre-process results
    last_date = process_data(data, min_date)

    # Update data
    new_data = get_recent(last_date)

    # Add the new data to the old data
    data['data'].extend(new_data)

    # Write file
    write(data, opts.cache_file)


# for python libraries
if __name__ == '__main__':
    # Define command line parameters
    args = argparse.ArgumentParser()
    args.add_argument('--cache_file', default='test.json', type=str,
                      help='File for storing output')
    args.add_argument('--days_ago', default=7, type=int,
                      help='Number of days into the past to keep data')
    opts = args.parse_args()

    # Run the data processing
    min_date = datetime.utcnow() - timedelta(days=opts.days_ago)
    update_cache(opts.cache_file, min_date)
