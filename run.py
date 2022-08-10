# This file is for developer. You don't have to use it.

from functions_dir.search import Search
import time


search_queries = ['de']

search = Search()
file_name = search.create_report_file(test_name='search_error_404')

for search_query in search_queries:
    search = Search()

    search.load_first_page()
    search.accept_cookies()
    search.press_search_btn()
    search.search_field(search_request=search_query)
    search.press_search_btn_2()
    pages_links_list = search.check_pages_search()  # return list of all the links in the search result.
    pages_links_list[1] = 'https://teamdanmark.dk/j83jr'
    pages_links_list[3] = 'https://teamdanmark.dk/j2390'
    pages_links_list[4] = 'https://teamdanmark.dk/j83jr'
    pages_links_list[7] = 'https://teamdanmark.dk/j2390'

    i = 0
    for page in pages_links_list:
        i += 1
        search.get(page)
        if search.is_404_error() == True:
            flag = False
            search.check_pages_elasticsearch_report(file_name=file_name,
                                                    search_query=search_query,
                                                    page_title='-',
                                                    page_url=page)