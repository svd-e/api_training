import pytest


@pytest.mark.test_get_brewery
class TestGetBrewery:
    """
    This class created for testing the "Get Brewery" option of the openbrewerydb.org resource
    """

    @pytest.mark.parametrize('id', ["10-56-brewing-company-knox", "zwei-brewing-co-fort-collins"])
    def test_simple_positive(self, client, id):
        client.request_by_id(id)
        client.is_the_status_code_is_200()
        client.is_the_parsed_id_matches_the_response()
        client.is_the_length_of_answer_is_correct()
        client.is_there_an_non_null_name_field()

    @pytest.mark.parametrize('id', ["3",
                                    "~",
                                    "10000000000000000000000000000000000000000000000000000000000000000000000000000",
                                    pytest.param("/", marks=pytest.mark.xfail),
                                    "null",
                                    "get",
                                    "None",
                                    "-5",
                                    "qwerty",
                                    "id",
                                    "<1>",
                                    ",",
                                    pytest.param(".", marks=pytest.mark.xfail),
                                    "Ё",
                                    "|",
                                    "\\",
                                    "7"])
    def test_negative(self, id, client):
        client.request_by_id(id)
        client.is_the_status_code_is_404()
        client.is_the_failure_message_is_correct()


@pytest.mark.test_list_breweries
@pytest.mark.parametrize('sort_param', ["city", "country"])
class TestListBreweries:
    """
    This class created for testing the "List Breweries" option of the openbrewerydb.org resource
    """

    def test_of_ascending_order(self, client, sort_param):
        sort_type = "asc"
        params = {"sort": f"{sort_param}:{sort_type}", "per_page": 50}
        client.request_sorting(params, sort_param)
        client.is_the_status_code_is_200()
        client.is_the_order_ascending()

    def test_of_descending_order(self, client, sort_param):
        sort_type = "desc"
        params = {"sort": f"{sort_param}:{sort_type}", "per_page": 50}
        client.request_sorting(params, sort_param)
        client.is_the_status_code_is_200()
        client.is_the_order_descending()

    # pytest -v -s -m test_get_brewery test_me.py
    # pytest -v -s -m test_list_breweries test_me.py
    # print(json.dumps(self.data, indent=4))
