import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base='base_layout')
modelo_producto = Producto()

class Ver:
    def GET(self, id):
        producto = modelo_producto.obtener_detalles(id)
        return render.ver_producto(producto)

        