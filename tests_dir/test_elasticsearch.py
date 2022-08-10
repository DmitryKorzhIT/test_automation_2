import os.path
import datetime
from functions_dir.elasticsearch import Elasticsearch



def test_1():
    ''' Check all the pages in the results of the elasticsearch on the 404 error. '''

    flag_global = True

    # List of the search queries to test.
    search_queries = ['Denmark']

    # Create a report file.
    elasticsearch = Elasticsearch()
    file_name = elasticsearch.create_report_file(test_name='elasticsearch_error_404')

    # Start a loop to check each search query.
    for search_query in search_queries:

        elasticsearch = Elasticsearch()
        elasticsearch.load_first_page()
        elasticsearch.accept_cookies()
        elasticsearch.press_search_btn()
        elasticsearch.search_field(search_request=search_query)
        flag_local = elasticsearch.check_pages_elastic_search(file_name=file_name,
                                                       search_query=search_query)

        # If the page has the 404 error.
        if flag_local == False:
            flag_global = False  # at least one test hasn't been passed


    assert flag_global