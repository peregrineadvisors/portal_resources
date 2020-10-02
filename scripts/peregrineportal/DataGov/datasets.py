import os
import datetime as dt

import pickle
import requests

class DataSets():

    def __init__(self, fetch_size=1000):
        """
        Initialize the dataset getter class
        """
        # Set the batch size
        self.fetch_size = fetch_size

        # Define the URL to query from and parameters to submit
        self.requestUrl = 'https://catalog.data.gov/api/action/package_search'
        self.requestPars = {
            'sort': 'metadata_modified desc', 
            'rows': fetch_size
        }

        self.save_path = os.path.curdir + '/datasets.pkl'

        # Here we list all of the fields returned by our query. Fields
        # that are not to be saved are commented out.
        self.data_fields = [
            'author',
            'author_email',
            #'creator_user_id',
            #'extras',
            #'groups',
            'id',
            #'isopen',
            #'license_id',
            #'license_title',
            #'maintainer',
            #'maintainer_email',
            #'metadata_created',
            'metadata_modified',
            'name',
            'notes',
            #'num_resources',
            #'num_tags',
            'organization',
            #'owner_org',
            #'private',
            #'relationships_as_object',
            #'relationships_as_subject',
            #'resources',
            'revision_id',
            #'state',
            #'tags',
            'title',
            #'tracking_summary',
            #'type',
            'url',
            #'version'
        ]

        # Storage item
        self.datasets = dict()
        

    def fetch(self, save=False):
        """
        Fetch most recent organization data back to supplied min_date
        """
        pass


    def fetch_recent(self, save=False, min_date=None, query_pars={}):
        """
        Parameters
        ----------
        min_date: datetime.datetime
            Minimum date/time (UTC) to obtain updates for
        query_pars: dict()
            Parameters to use for query
        """
        # Set the minimum date to 1 day ago if not supplied
        if min_date is None:
            min_date = self._default_min_date(days_ago=1)

        # Copy the parameters
        requestPars = self.requestPars
        for key,val in query_pars:
            requestPars[key] = val
        requestPars['start'] = 0

        # Submit the query until we have an entry that's too old
        oldest = dt.datetime.utcnow()
        while oldest > min_date:
            # Submit the query and get the list of results
            res = requests.get(self.requestUrl, requestPars)
            res_list = res.json()['result']['results']
            
            # Loop on the results
            for dataset in res_list:
                # Get the date of this update
                oldest = dt.datetime.fromisoformat(dataset['metadata_modified'])

                # Make sure we're still looking at data from the correct time period
                if oldest > min_date:
                    # Assemble the data fields we want
                    items = {}
                    for key in self.data_fields:
                        items[key] = dataset[key]

                    # Add this item to the dataset
                    self.datasets[items['revision_id']] = items

                # ... otherwise break
                else:
                    break

            # Increment the request start
            requestPars['start'] += self.fetch_size

        if save:
            self.save()

        return self.datasets

    
    def _default_min_date(self, days_ago=1):
        """
        docstring
        """
        return dt.datetime.utcnow() - dt.timedelta(days=days_ago)


    def save(self):
        """
        Write the results to a file
        """
        # Write the data to file
        with open(self.save_path, 'wb') as fh:
            pickle.dump(self.datasets, fh)
        return
