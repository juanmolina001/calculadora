from flask_cors import CORS
from flask import Flask
import math as mt
from flask import jsonify

app = Flask(__name__)
CORS(app)

# index principal 
@app.route('/')
def principal():
    titulo = 'En la url define /(Operacion)/(numero1)/(numero2)'

# suma 
@app.route('/suma/<float:numero1>/<float:numero2>')
@app.route('/suma/<int:numero1>/<int:numero2>')
@app.route('/suma/<int:numero1>/<float:numero2>')
@app.route('/suma/<float:numero1>/<int:numero2>')
def suma(numero1, numero2):
    titulo = 'Suma'
    resultado = f'el resultado de {numero1} + {numero2} es: {numero1 + numero2}'
    data={
        'resultado' : resultado,
        'operacion' : 'Suma'
    }
    jsonify(data)


# resta 
@app.route('/')
@app.route('/resta/<float:numero1>/<float:numero2>')
@app.route('/resta/<int:numero1>/<int:numero2>')
@app.route('/resta/<int:numero1>/<float:numero2>')
@app.route('/resta/<float:numero1>/<int:numero2>')
def resta(numero1, numero2):
    titulo = 'Resta'
    resultado = f'el resultado de {numero1} - {numero2} es: {numero1 - numero2}'    
    data={
        'resultado' : resultado,
        'operacion' : 'Resta'
    }
    jsonify(data)

# multiplicacion 
@app.route('/')
@app.route('/multiplicacion/<float:numero1>/<float:numero2>')
@app.route('/multiplicacion/<int:numero1>/<int:numero2>')
@app.route('/multiplicacion/<int:numero1>/<float:numero2>')
@app.route('/multiplicacion/<float:numero1>/<int:numero2>')
def multiplicacion(numero1, numero2):
    titulo = 'Multiplicacion'
    resultado = f'el resultado de {numero1} x {numero2} es: {numero1 * numero2}'
    data={
        'resultado' : resultado,
        'operacion' : 'Multiplicacion'
    }
    jsonify(data)

# division 
@app.route('/')
@app.route('/division/<float:numero1>/<float:numero2>')
@app.route('/division/<int:numero1>/<int:numero2>')
@app.route('/division/<int:numero1>/<float:numero2>')
@app.route('/division/<float:numero1>/<int:numero2>')
def division(numero1, numero2):
    titulo = 'Division'
    resultado = f'el resultado de {numero1} ÷ {numero2} es: {numero1 / numero2}'
    data={
        'resultado' : resultado,
        'operacion' : 'Division'
    }
    jsonify(data)

# potenciacion 
@app.route('/')
@app.route('/potenciacion/<float:numero1>/<float:numero2>')
@app.route('/potenciacion/<int:numero1>/<int:numero2>')
@app.route('/potenciacion/<int:numero1>/<float:numero2>')
@app.route('/potenciacion/<float:numero1>/<int:numero2>')
def potenciacion(numero1, numero2):
    titulo = 'Potenciacion'
    resultado = f'el resultado de {numero1} ** {numero2} es: {numero1 ** numero2}'
    data={
        'resultado' : resultado,
        'operacion' : 'Potenciacion'
    }
    jsonify(data)

# seno 
@app.route('/')
@app.route('/seno/<float:numero1>')
@app.route('/seno/<int:numero1>')
def seno(numero1):
    titulo = 'Seno'
    resultado = f'el seno de {numero1} es: {mt.sin(numero1)}'
    data={
        'resultado' : resultado,
        'operacion' : 'Seno'
    }
    jsonify(data)

# coseno 
@app.route('/')
@app.route('/coseno/<float:numero1>')
@app.route('/coseno/<int:numero1>')
def coseno(numero1):
    titulo = 'Coseno'
    resultado = f'el coseno de {numero1} es: {mt.cos(numero1)}'
    data={
        'resultado' : resultado,
        'operacion' : 'Coseno'
    }
    jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
