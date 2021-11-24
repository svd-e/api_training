import requests


class MainMethods:
    """
    This is a class of basic methods for testing openbrewerydb.org
    """
    def __init__(self):
        self.url = "https://api.openbrewerydb.org/breweries/"
        self.id = None
        self.res = None
        self.data = None
        self.sorted_data = None

    def request_by_id(self, id):
        self.id = id
        self.res = requests.get(self.url + self.id)
        self.data = self.res.json()
        return self.data

    def request_sorting(self, params, sort_param):
        self.sorted_data = []
        self.res = requests.get(self.url, params=params)
        self.data = self.res.json()
        for i in range(0, len(self.data)):
            self.sorted_data.append(self.data[i][sort_param])

    def is_the_order_ascending(self):
        assert self.sorted_data == sorted(self.sorted_data), "The order is not ascending"

    def is_the_order_descending(self):
        assert self.sorted_data == sorted(self.sorted_data, reverse=True), "The order is not descending"

    def is_the_status_code_is_200(self):
        assert self.res.status_code == 200, "Status code is not 200"

    def is_the_status_code_is_404(self):
        assert self.res.status_code == 404, "Status code is not 404"

    def is_the_parsed_id_matches_the_response(self):
        assert self.data["id"] == self.id, "API returned the wrong id"

    def is_the_length_of_answer_is_correct(self):
        assert len(self.data) == 17, "Data has a wrong structure"

    def is_the_failure_message_is_correct(self):
        assert self.data["message"] == "Couldn't find Brewery", "The failure message is wrong"

    def is_there_an_non_null_name_field(self):
        assert self.data["name"] is not None, "The brewery doesn't have a name"
