"""Framework web.py"""
import web

#  Rutas de los controladores
urls = ("/", "mvc.controllers.index.Index", "/pagina2", "mvc.controllers.pagina2.Pagina2", "/pagina3", "mvc.controllers.pagina3.Pagina3")
app = web.application(urls, globals())

#  Punto de entrada
if __name__ == "__main__":
    app.run()