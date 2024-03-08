import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/')
modelo_producto = Producto()

class Index:
    def GET(self):
<<<<<<< HEAD
        productos = producto.obtener_productos()
=======
        productos = modelo_producto.obtener_productos()
>>>>>>> 910e5a4096b2e3be144064b2c10b69d70b4e1117
        return render.index(productos)
        