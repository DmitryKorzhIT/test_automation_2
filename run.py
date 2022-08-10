import os.path
import datetime
from functions_dir.search import Search

def search_tst():
    ''' Check all the pages in the results of the elastic search on the 404 error. '''

    flag_global = True

    # List of the search queries to test.
    search_queries = ['Talent', 'Denmark', 'Danmark', 'Sport']

    # Create the report file.
    current_date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f'elastic_search_error_404_{current_date_time}.csv'
    file = open(os.path.dirname(__file__) + f'/reports/{file_name}', 'w')
    file.close()

    # Start a loop to check each search query.
    for search_query in search_queries:
        search = Search()
        search.load_first_page()
        try:
            search.accept_cookies()

        except:
            pass

        finally:
            search.press_search_btn()
            search.search_field(search_request=search_query)
            flag_local = search.check_pages_elastic_search(file_name=file_name,
                                                           search_query=search_query)

            # If the page has the 404 error.
            if flag_local == False:
                flag_global = False  # at least one test hasn't been passed

search_tst()