

# Import the site parsers and RSS feed generators
from feedgen.parsers import Parser, TagConfig
from feedgen.writers import Rss

class FedDataStrategyNews(Parser):
    """
    Subclass of the Parser class that specifically searches on the Federal
    Data Strategy news site
    """

    def __init__(self, **kwargs):
        """Initialize the search parser
        """
        super().__init__(**kwargs)

        self.name = 'Federal Data Strategy News'
        self.type = 'feddatastrategy'

        # Define the URL and query parameters
        self.url['root'] = 'https://strategy.data.gov/'
        self.url['base'] = 'https://strategy.data.gov/news/'
        self.url['params'] = {}

        # Tags to be parsed
        self.tag_config = TagConfig(
            container = 'li.h-entry',
            title     = 'h2.p-name',
            link      = 'a',
            descrip   = 'h2.p-name'
        )


    def parse_html(self):
        """
        Assembles and submits a given query to a website and parses the returned
        HTML to extract the information requested by the user. Also appends the 
        root url to the returned links

        Returns
        -------
        Parsed results from the specified URL
        """
        # Run the base code
        result = super().parse_html()
        
        # Prepend the news story links to the root url
        for res in result:
            res.link = self.url['root'] + res.link

        return result


class DataGovBlog(Parser):
    """
    Subclass of the Parser class that specifically searches on 'data.gov'
    """

    def __init__(self, **kwargs):
        """Initialize the search parser
        """
        super().__init__(**kwargs)

        self.name = 'Data Gov'
        self.type = 'datagov'

        # Define the URL and query parameters
        self.url['root'] = 'https://www.data.gov/'
        self.url['base'] = 'https://www.data.gov/meta/'
        self.url['params'] = {}

        # Tags to be parsed
        self.tag_config = TagConfig(
            container = 'article.post',
            title     = 'h2.entry-title a',
            link      = 'h2 a',
            descrip   = 'div.entry-summary p'
        )


    def parse_html(self):
        """
        Assembles and submits a given query to a website and parses the returned
        HTML to extract the information requested by the user. Also appends the 
        root url to the returned links

        Returns
        -------
        Parsed results from the specified URL
        """
        # Run the base code
        result = super().parse_html()
        
        # Prepend the news story links to the root url
        for res in result:
            print(res)
            if res.link is not None:
                res.link = self.url['base'] + res.link

        return result


class NextGovDataNews(Parser):
    """
    Subclass of the Parser class that specifically searches on 'data.gov'
    """

    def __init__(self, **kwargs):
        """Initialize the search parser
        """
        super().__init__(**kwargs)

        self.name = 'Data Gov'
        self.type = 'datagov'

        # Define the URL and query parameters
        self.url['root'] = 'https://www.nextgov.com/'
        self.url['base'] = 'https://www.nextgov.com/analytics-data/'
        self.url['params'] = {}

        # Tags to be parsed
        self.tag_config = TagConfig(
            container = 'div.river-item-inner',
            title     = 'h2.river-item-hed a',
            link      = 'h2.river-item-hed a',
            descrip   = 'h3.river-item-dek'
        )


    def parse_html(self):
        """
        Assembles and submits a given query to a website and parses the returned
        HTML to extract the information requested by the user. Also appends the 
        root url to the returned links

        Returns
        -------
        Parsed results from the specified URL
        """
        # Run the base code
        result = super().parse_html()
        
        # Prepend the news story links to the root url
        for res in result:
            print(res)
            if res.link is not None:
                res.link = self.url['base'] + res.link

        return result

# Main function
if __name__ == '__main__':
    res = [
        *NextGovDataNews().parse_html(), 
        *FedDataStrategyNews().parse_html(), 
        *DataGovBlog().parse_html()
    ]

    # Write to RSS
    rss = Rss(title='Peregrine Advisors Federal Data News',
              link='https://www.peregrineadvisors.com',
              descrip='Federal data news aggregated from a variety of news outlets.')

    rss.write(res, 'feed_results.xml')
    