from functions_dir.search import Search


def test_1():
    search_queries = ['Denmark', 'forbund']  # list of words to test
    for search_query in search_queries:
        search = Search()
        search.load_first_page()

        try:
            search.accept_cookies()

        finally:
            search.press_search_btn()
            search.search_field(search_request=search_query)
            flag = search.check_pages_elastic_search()
            if flag == False:
                break

    assert flag