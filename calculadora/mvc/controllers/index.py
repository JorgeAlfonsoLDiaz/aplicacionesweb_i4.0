import web

render = web.template.render('mvc/views/')

class Calculadora:
    def GET(self):
        return render.index()

    def POST(self):
        input_data = web.input()

        num1 = int(input_data.num1)
        num2 = int(input_data.num2)

        resultado = num1 + num2

        return render.index(resultado, num1, num2)

