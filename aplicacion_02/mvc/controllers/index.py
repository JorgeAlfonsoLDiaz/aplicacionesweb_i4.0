import web

render = web.template.render('mvc/views/index.html')

class Index:
    def GET(self):
        return render.index()