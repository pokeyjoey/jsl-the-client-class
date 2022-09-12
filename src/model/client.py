import requests

class Client:

    @classmethod
    def json_response(self, url):
        response = requests.get(url)

        return response.json()

