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

    def obtener_detalles(self, id):
        id = int(id)

        response_uri = requests.get(f"{self.bd}items/{id}")
        response_json = json.loads(response_uri.text)

        self.response = response_json

        return self.response

    def insertar_producto(self, name, description, cost, stock):

        req_str = {
            "name": name,
            "description": description,
            "cost": cost,
            "stock": stock
        }

        req_json = json.dumps(req_str)

        post_uri = f"{self.bd}items"

        header = {'Content-Type': 'application/json'}

        request_post = requests.post(post_uri, headers=header, data=req_json)

        return request_post

    def borrar_producto(self, id):

        delete_uri = f"{self.bd}items/{id}"

        request_delete = requests.delete(delete_uri)

        return request_delete
