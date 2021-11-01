import json

import requests

class MainMethods:
    def __init__(self):
        self.url = "https://api.openbrewerydb.org/breweries/"

    def request_by_id(self, req):
        self.id = req
        self.res = requests.get(self.url + self.id)
        self.data = self.res.json()
        return self.data

    def request_sorting(self, req):
        self.sorted_data = []
        # print(self.sorted_data)

        self.order = req
        self.res = requests.get(self.url + self.order)
        self.data = self.res.json()
        # print(json.dumps(self.data, indent=4))
        for i in range(0, len(self.data)):
            self.sorted_data.append(self.data[i]["city"])
            # print(self.data[i]["phone"])
            # print(json.dumps(self.data[i], indent=4))
            # print(self.data[i]["phone"])
        # print(self.sorted_data)
        # print(self.data)
        # return self.sorted_data

    def is_the_order_ascending(self):
        # print(self.sorted_data)
        # print(sorted(self.sorted_data))
        # # print(self.sorted_data.sort(reverse=True))
        # print(self.sorted_data.sort())
        # pass
        assert self.sorted_data == sorted(self.sorted_data), "The order is not ascending"
        # assert self.sorted_data == self.sorted_data.sort(reverse=True), "The order is not ascending"


    def is_the_order_descending(self):
        # print(self.sorted_data)
        # print(sorted(self.sorted_data))
        # pass
        assert self.sorted_data == sorted(self.sorted_data, reverse=True), "The order is not descending"


    def is_the_status_code_is_200(self):
        assert self.res.status_code == 200, "Status code is not 200"

    def is_the_status_code_is_404(self):
        assert self.res.status_code == 404, "Status code is not 404"

    def is_the_parsed_id_matches_the_response(self, id):
        assert self.data["id"] == id, "API returned the wrong id"

    def is_the_length_of_answer_is_correct(self):
        assert len(self.data) == 17, "Data has a wrong structure"

    def is_the_failure_message_is_correct(self):
        assert self.data["message"] == "Couldn't find Brewery", "The failure message is wrong"

    def is_there_an_non_null_name_field(self):
        assert self.data["name"] != None, "The brewery doesn't have a name"