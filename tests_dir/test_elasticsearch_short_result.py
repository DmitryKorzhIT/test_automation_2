import os
import sys

path = os.getcwd()  # get current directory
parent_path = os.path.abspath(os.path.join(path, os.pardir))  # prints parent directory
sys.path.append(parent_path)


from functions_dir.elasticsearch_short_result import ElasticsearchShortResult


def test_1():
    """Check all the pages in the results of the short elasticsearch on the 404 error."""

    flag_global = True

    # List of the search queries to test.
    search_queries = ["de"]

    # Create a report file.
    elasticsearch_short_result = ElasticsearchShortResult()
    header = "Search query,Page title,Page url\n"
    file_name = elasticsearch_short_result.create_report_file(
        test_name="elasticsearch_short_result_error_404", header=header
    )

    # Start a loop to check each search query.
    for search_query in search_queries:

        elasticsearch_short_result = ElasticsearchShortResult()
        elasticsearch_short_result.load_specific_page()
        elasticsearch_short_result.accept_cookies()
        elasticsearch_short_result.press_search_btn()
        elasticsearch_short_result.search_field(search_request=search_query)
        flag_local = elasticsearch_short_result.check_pages_elasticsearch(
            file_name=file_name, search_query=search_query
        )

        # If the page has the 404 error.
        if flag_local is False:
            flag_global = False  # at least one test hasn't been passed

    assert flag_global
