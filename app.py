from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return "<p>Hola Mundo</p>"


@app.route("/datos", methods=['POST', 'GET'])
def datos():
    if request.method == 'POST':
        try:
            # Obtener los coeficientes del formulario
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            # Calcular el discriminante
            discriminante = b ** 2 - 4 * a * c

            if discriminante > 0:
                # Dos soluciones reales
                x1 = (-b + math.sqrt(discriminante)) / (2 * a)
                x2 = (-b - math.sqrt(discriminante)) / (2 * a)
                resultado = f"Dos soluciones reales: x1 = {x1}, x2 = {x2}"
            elif discriminante == 0:
                # Una solución real
                x = -b / (2 * a)
                resultado = f"Una solución real: x = {x}"
            else:
                # Soluciones complejas
                parte_real = -b / (2 * a)
                parte_imaginaria = math.sqrt(-discriminante) / (2 * a)
                resultado = (f"Dos soluciones complejas: x1 = {parte_real} + {parte_imaginaria}i, "
                             f"x2 = {parte_real} - {parte_imaginaria}i")
        except ValueError:
            resultado = "Entrada no válida, por favor ingrese solo números."
        except ZeroDivisionError:
            resultado = "El coeficiente 'a' no puede ser cero."
        return render_template("formulario.html", resultado=resultado)
    return render_template("formulario.html", resultado=None)


if __name__ == "__main__":
    app.run()