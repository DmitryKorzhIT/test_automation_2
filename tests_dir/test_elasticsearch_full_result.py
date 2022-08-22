import os
import sys

path = os.getcwd()  # get current directory
parent_path = os.path.abspath(os.path.join(path, os.pardir))  # prints parent directory
sys.path.append(parent_path)


from functions_dir.elasticsearch_full_result import ElasticsearchFullResult


def test_1():
    """Check all the pages in the full results of the elasticsearch on the 404 error."""

    flag = True
    search_queries = ["de"]  # enter the search queries on your own, e.g. ['sport', 'Denmark', 'news', 'swimming'].

    # Create a report file.
    elasticsearch_full_result = ElasticsearchFullResult()
    header = "Search query,Page title,Page url\n"
    file_name = elasticsearch_full_result.create_report_file(
        test_name="elasticsearch_full_result_error_404", header=header
    )

    for search_query in search_queries:
        elasticsearch_full_result = ElasticsearchFullResult()

        elasticsearch_full_result.load_specific_page()
        elasticsearch_full_result.accept_cookies()
        elasticsearch_full_result.press_search_btn()
        elasticsearch_full_result.search_field(search_request=search_query)
        elasticsearch_full_result.press_search_btn_2()
        pages_links_list = (
            elasticsearch_full_result.check_pages_search()
        )  # return list of all the links in the search result.

        for page in pages_links_list:
            elasticsearch_full_result.get(page)
            if elasticsearch_full_result.is_404_error() is True:
                flag = False
                elasticsearch_full_result.check_pages_elasticsearch_report(
                    file_name=file_name,
                    search_query=search_query,
                    page_title="",
                    page_url=page,
                )

    assert flag
