import web
from models.modelo_productos import Producto

render = web.template.render('mvc/views/')
modelo_producto = Producto()

class Index:
    def GET(self):
        productos = producto.obtener_productos()
            return render.index(productos)
        