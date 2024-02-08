"""Framework web.py"""
import web

#  Rutas de los controladores
urls = (
    "/", "hello", 
    "/pagina2", "pagina2",
    "/pagina3", "pagina3"
)
app = web.application(urls, globals())


class hello:
    def GET(self):
        return "Hello, pagina 1"


class pagina2:
    def GET(self):
        return "Hola, pagina 2"

class pagina3:
    def GET(self):
        return "Hola, pagina 3"


if __name__ == "__main__":
    app.run()