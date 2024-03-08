import web
from models.modelo_productos import Producto

render = web.template.render('views/')
modelo_producto = Producto()

class Listar:
    def GET(self):
        productos = producto.obtener_productos()
            return render.index(productos)
        