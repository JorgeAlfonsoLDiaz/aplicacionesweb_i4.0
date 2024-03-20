import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base='base_layout')
modelo_producto = Producto()

class Listar:
    def GET(self):
        query = web.input()
        name = query.get('name')

        whole_list = modelo_producto.obtener_productos(name="")
        total_count = modelo_producto.length

        if name:
            productos = modelo_producto.obtener_productos(name)
        else:
            productos = modelo_producto.obtener_productos(name="")
        
        count = modelo_producto.length

        return render.lista_productos(productos, name, count, total_count)
    
