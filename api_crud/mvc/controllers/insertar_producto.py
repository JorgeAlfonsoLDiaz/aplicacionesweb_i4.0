import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/')
modelo_producto = Producto()

class Insertar:
    def GET(self):
        return render.insertar_producto()


    def POST(self):
        data = web.input()

        name = data.name
        description = data.description
        cost = float(data.cost)
        stock = int(data.stock)

        post_response = modelo_producto.insertar_producto(name, description, cost, stock)

        if post_response:
            print("Producto Insertado Correctamente!")
            raise web.seeother('/')
        else:
            return "Hubo un error en la inserción del producto."
