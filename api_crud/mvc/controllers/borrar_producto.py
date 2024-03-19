import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/')
modelo_producto = Producto()

class Eliminar:
    def GET(self, id):
        producto = modelo_producto.obtener_detalles(id)
        return render.borrar_producto(producto)

    def POST(self, id):
        delete_response = modelo_producto.borrar_producto(id)

        if delete_response:
            print("Producto Eliminado Correctamente.")
            raise web.seeother('/')
        else:
            return "Hubo un error en la eliminación del producto."
