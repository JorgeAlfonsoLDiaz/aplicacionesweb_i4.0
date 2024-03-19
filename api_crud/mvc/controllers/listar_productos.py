import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base='base_layout')
modelo_producto = Producto()

class Listar:
    def GET(self):
        productos = modelo_producto.obtener_productos()
        return render.lista_productos(productos)
        