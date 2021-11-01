import pytest

from methods import MainMethods

@pytest.mark.test_get_brewery
class TestGetBrewery():

    def test_simple_positive(self, client):
        id = "10-56-brewing-company-knox"
        client.request_by_id(id)
        client.is_the_status_code_is_200()
        client.is_the_parsed_id_matches_the_response(id)
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
class TestListBreweries():
    def test_of_ascending_order(self, client):
        req = "?sort=city:asc&per_page=50"
        client.request_sorting(req)
        client.is_the_status_code_is_200()
        client.is_the_order_ascending()

    def test_of_descending_order(self, client):
        req = "?sort=city:desc&per_page=50"
        client.request_sorting(req)
        client.is_the_status_code_is_200()
        client.is_the_order_descending()






    # 10-barrel-brewing-co-denver-denver

    # pytest -v -s -m test_get_brewery test_me.py
    # pytest -v -s -m test_list_breweries test_me.py
