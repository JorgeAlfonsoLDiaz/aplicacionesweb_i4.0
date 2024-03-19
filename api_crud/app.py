"""Framework web.py"""
import web

#  Rutas de los controladores
urls = (
    "/", "mvc.controllers.listar_productos.Listar",
    "/insertar", "mvc.controllers.insertar_producto.Insertar",
    "/borrar/(.*)", "mvc.controllers.borrar_producto.Eliminar",
    "/actualizar/(.*)", "mvc.controllers.actualizar_producto.Actualizar",
    "/ver/(.*)", "mvc.controllers.ver_producto.Ver")
app = web.application(urls, globals())

#  Punto de entrada
if __name__ == "__main__":
    web.config.debug == True
    app.run()
