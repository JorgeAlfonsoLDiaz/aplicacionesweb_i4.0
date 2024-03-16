import web, requests, json


class Producto:
    def __init__(self):
        URI = "https://api-crud-4e49c699968d.herokuapp.com/"

        self.bd = URI
    def obtener_productos(self):
        response_uri = requests.get(self.bd)
        response_json = json.loads(response_uri.text)
        
        self.length = len(response_json)
        self.response = response_json

        return self.response