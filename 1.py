import requests
import json
def my():
    api_url = "https://api.openbrewerydb.org/breweries?sort=phone:desc&per_page=3"

    res = requests.get(api_url)
    # print(res.status_code)
    # print(res.headers["Content-Type"])
    # print(res.json())  # returns json.loads(res.text) :)

    data = res.json()

    # print(json.dumps(data, indent=4))
    # print(data[1]["phone"])
    sorted_data = []
    for i in range(0, len(data)):
        sorted_data.append(data[i]["phone"])
        # print(json.dumps(data[i]["phone"], indent=4))
    return sorted_data



my()



print(my())
print(my())
# id = "10-56-brewing-company-knox"
# url = "https://api.openbrewerydb.org/breweries/" + id
# print(url)