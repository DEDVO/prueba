from urllib import request
from flask import render_template, request
import flask as fl


app = fl.Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return "<p>Hello World</p>"
@app.route("/datos", methods=['POST', 'GET'])
def datos():
    if request.method == 'POST':
        try:
            a = request.form['a']
            b = request.form['b']
            c=int(a)+int(b)
            #print(a+b)
        except ValueError:
            c = "Emttrada no valida"
        return render_template("formulario.html", c=c)
    return render_template("formulario.html")

if __name__ == "__main__":
    app.run()