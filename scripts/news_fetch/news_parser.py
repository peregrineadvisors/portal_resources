

# Import the site parsers and RSS feed generators
from feedgen.parsers import Parser, TagConfig
from feedgen.parsers import CSSInnerText, CSSAttribute
from feedgen.writers import RssFeed, JsonFeed

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
            container = CSSInnerText('li.h-entry'),
            title     = CSSInnerText('h2.p-name'),
            link      = CSSAttribute('a', 'href'),
            descrip   = CSSInnerText('h2.p-name'),
            extras    = {
                'pubDate': CSSInnerText('div.dt-published')
            }
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
            container = CSSInnerText('article.post'),
            title     = CSSInnerText('h2.entry-title a'),
            link      = CSSAttribute('h2 a', 'href'),
            descrip   = CSSInnerText('div.entry-summary p'),
            extras    = {
                'pubDate': CSSAttribute('time.published', 'datetime')
            }
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
    Subclass of the Parser class that specifically searches on 'nextgov.com'
    """

    def __init__(self, **kwargs):
        """Initialize the search parser
        """
        super().__init__(**kwargs)

        self.name = 'NextGov'
        self.type = 'nextgov'

        # Define the URL and query parameters
        self.url['root'] = 'https://www.nextgov.com/'
        self.url['base'] = 'https://www.nextgov.com/analytics-data/'
        self.url['params'] = {}

        # Tags to be parsed
        self.tag_config = TagConfig(
            container = CSSInnerText('div.river-item-inner'),
            title     = CSSInnerText('h2.river-item-hed a'),
            link      = CSSAttribute('h2.river-item-hed a', 'href'),
            descrip   = CSSInnerText('h3.river-item-dek'),
            extras    = {
                'pubDate': CSSAttribute('li.story-meta-date time', 'datetime')
            }
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

class FedScoopNews(Parser):
    """
    Subclass of the Parser class that specifically searches on 'fedscoop.com'
    """

    def __init__(self, **kwargs):
        """Initialize the search parser
        """
        super().__init__(**kwargs)

        self.name = 'FedScoop'
        self.type = 'fedscoop'

        # Define the URL and query parameters
        self.url['base'] = 'https://fedscoop.com/'
        self.url['params'] = {}

        # Tags to be parsed
        self.tag_config = TagConfig(
            container = CSSInnerText('article.article-thumb'),
            title     = CSSInnerText('a.article-thumb__title h3'),
            link      = CSSAttribute('a.article-thumb__title', 'href'),
            descrip   = CSSInnerText('div.article-thumb__short p')
        )


# Main function
if __name__ == '__main__':
    res = [
        *NextGovDataNews().parse_html(), 
        *FedScoopNews().parse_html(),
        *FedDataStrategyNews().parse_html(), 
        *DataGovBlog().parse_html()
    ]

    # Write to RSS
    json_feed = JsonFeed(title='Peregrine Advisors Federal Data News',
              link='https://www.peregrineadvisors.com',
              descrip='Federal data news aggregated from a variety of news outlets.')

    json_feed.write(res, 'feed_results.json')
    