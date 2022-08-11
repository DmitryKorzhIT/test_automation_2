from functions_dir.search import Search


def test_1():
    flag = True
    search_queries = ['de']

    # Create a report file.
    search = Search()
    file_name = search.create_report_file(test_name='search_error_404')

    for search_query in search_queries:
        search = Search()

        search.load_specific_page()
        search.accept_cookies()
        search.press_search_btn()
        search.search_field(search_request=search_query)
        search.press_search_btn_2()
        pages_links_list = search.check_pages_search()  # return list of all the links in the search result.

        for page in pages_links_list:
            search.get(page)
            if search.is_404_error() == True:
                flag = False
                search.check_pages_elasticsearch_report(file_name=file_name,
                                                        search_query=search_query,
                                                        page_title='-',
                                                        page_url=page)


    assert flag





