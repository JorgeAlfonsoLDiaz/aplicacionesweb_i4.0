import web, requests, json


class Producto:
    def __init__(self):
        URI = "https://api-crud-4e49c699968d.herokuapp.com/"

        response_uri = requests.get(URI)
        response_json = json.loads(response_uri.text)

        self.length = len(response_json)
        self.response = response_json

    def obtener_productos(self):
        return self.response