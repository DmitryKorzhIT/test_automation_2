import os.path
import datetime
from functions_dir.search import Search



def test_1():
    # List of the search queries to test.
    search_queries = ['Denmark', 'forbund']

    # Open the report file.
    current_date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f'elastic_search_error_404_{current_date_time}'
    file = open(os.path.dirname(__file__) + f'/../reports/{file_name}.csv', 'a')

    flag_global = True
    serial_number = 0

    # Start a loop to check each web page's link.
    for search_query in search_queries:
        search = Search()
        search.load_first_page()

        try:
            search.accept_cookies()

        finally:
            search.press_search_btn()
            search.search_field(search_request=search_query)
            check_pages_elastic_search_return = search.check_pages_elastic_search()
            flag_local = check_pages_elastic_search_return['no_error']

            # If the page has the 404 error.
            if not flag_local:
                flag_global = False  # at least one test hasn't been passed
                item_title = check_pages_elastic_search_return['item_title']
                item_url = check_pages_elastic_search_return['item_url']
                serial_number += 1

                error_page_info = f'{serial_number}.,"{search_query}","{item_title}","{item_url}"\n'
                file.write(error_page_info)

    file.close()


    assert flag_global