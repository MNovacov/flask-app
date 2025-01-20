from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario del Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        aprobado = promedio >= 40 and asistencia >= 75

        resultado = {
            'promedio': round(promedio, 2),
            'asistencia': asistencia,
            'estado': 'Aprobado' if aprobado else 'Reprobado'
        }

        return render_template('resultado.html', resultado=resultado)
    return render_template('form_ejercicio1.html')

# Ruta para el formulario del Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)

        resultado = {
            'nombre': nombre_mas_largo,
            'caracteres': len(nombre_mas_largo)
        }

        return render_template('resultado.html', resultado=resultado)
    return render_template('form_ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
