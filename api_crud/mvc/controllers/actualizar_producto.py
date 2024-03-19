import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base='base_layout')
modelo_producto = Producto()

class Actualizar:
    def GET(self, id):
        producto = modelo_producto.obtener_detalles(id)
        return render.actualizar_producto(producto)

    def POST(self, id):
        data = web.input()

        name = data.name
        description = data.description
        cost = float(data.cost)
        stock = int(data.stock)
        
        put_response = modelo_producto.actualizar_producto(id, name, description, cost, stock)

        if put_response:
            raise web.seeother('/')

        else:
            return "Error al actualizar."
