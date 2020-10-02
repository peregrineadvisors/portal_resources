
import requests
import os
import pickle

class Organizations():

    def __init__(self, fetch=True, save=True):
        """
        Initialize a class that defines organization data
        """
        # Define the request query
        self.requestUrl = 'https://catalog.data.gov/api/action/organization_list'
        self.requestPars = {'sort': 'name asc', 'all_fields': True}
        self.save_path = os.path.curdir + '/organizations.pkl'

        # Internally stored organization
        self.orgs = {}

        # Here we list all of the fields returned by our query. Fields
        # that are not to be saved are commented out.
        self.data_fields = [
            #'approval_status',
            #'created',
            'description',
            'display_name',
            'id',
            'image_display_url',
            #'is_organization',
            'name',
            'organization_type',
            #'package_count',
            #'packages',
            #'revision_id',
            #'state',
            'title',
            #'type'
        ]

        # Go ahead and do the fetching
        if fetch:
            try:
                self.fetch(save=save)
            except:
                # If failed to fetch, load from saved file
                self.load()

        
    def __getitem__(self, org_name):
        """
        Return data on given organization name (overloads `[<key>]`)
        """
        return self.orgs[org_name]


    def fetch(self, save=False):
        """
        Fetch the results from the database
        """
        # Fetch the organizations
        orgs = requests.get(self.requestUrl, 
                            params={'sort': 'name asc', 'all_fields': True})
        
        # Loop over the organizations and store the results
        for org_data in orgs.json()['result']:
            # Get the data to be stored
            extracted = {}
            for field_name in self.data_fields:
                extracted[field_name] = org_data[field_name]

            # Store the data we need
            self.orgs[org_data['name']] = extracted

        # Save results to file if requested
        if save:
            self.save()

        return


    def save(self):
        """
        Write the results to a file

        Return
        ------
        True if save was successful, otherwise false
        """
        # Write the organization data to file
        with open(self.save_path, 'wb') as fh:
            pickle.dump(self.orgs, fh)
        return


    def load(self):
        """
        Load organizations from previously saved file
        """
        # Open the file and load organization data
        with open(self.save_path, 'rb') as fh:
            self.orgs = pickle.load(fh)
        return
