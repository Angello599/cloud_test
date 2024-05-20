from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Base URL para el balanceador de carga
LIBROS_URL = 'http://lb-prod-proyecto-498384887.us-east-1.elb.amazonaws.com:8000/libros'
USUARIOS_URL = 'http://lb-prod-proyecto-498384887.us-east-1.elb.amazonaws.com:8001/usuarios'
PRESTAMOS_URL = 'http://lb-prod-proyecto-498384887.us-east-1.elb.amazonaws.com:8002/prestamos'

@app.route('/')
def index():
    libros = requests.get(LIBROS_URL).json()
    usuarios = requests.get(USUARIOS_URL).json()
    prestamos = requests.get(PRESTAMOS_URL).json()
    return render_template('index.html', libros=libros['libros'], usuarios=usuarios['usuarios'], prestamos=prestamos['prestamos'])

# Rutas para manejar libros
@app.route('/add_libro', methods=['POST'])
def add_libro():
    nuevo_libro = {
        "titulo": request.form['titulo'],
        "autor": request.form['autor'],
        "genero": request.form['genero'],
        "disponibilidad": request.form['disponibilidad'] == 'true'
    }
    requests.post(LIBROS_URL, json=nuevo_libro)
    return redirect(url_for('index'))

@app.route('/delete_libro/<int:libro_id>', methods=['POST'])
def delete_libro(libro_id):
    requests.delete(f'{LIBROS_URL}/{libro_id}')
    return redirect(url_for('index'))

# Rutas para manejar usuarios
@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    nuevo_usuario = {
        "nombre": request.form['nombre'],
        "direccion": request.form['direccion']
    }
    requests.post(USUARIOS_URL, json=nuevo_usuario)
    return redirect(url_for('index'))

@app.route('/delete_usuario/<int:usuario_id>', methods=['POST'])
def delete_usuario(usuario_id):
    requests.delete(f'{USUARIOS_URL}/{usuario_id}')
    return redirect(url_for('index'))

# Rutas para manejar prestamos
@app.route('/add_prestamo', methods=['POST'])
def add_prestamo():
    nuevo_prestamo = {
        "usuario_id": request.form['usuario_id'],
        "libro_id": request.form['libro_id'],
        "fecha_prestamo": request.form['fecha_prestamo'],
        "fecha_devolucion": request.form['fecha_devolucion']
    }
    requests.post(PRESTAMOS_URL, json=nuevo_prestamo)
    return redirect(url_for('index'))

@app.route('/delete_prestamo/<int:prestamo_id>', methods=['POST'])
def delete_prestamo(prestamo_id):
    requests.delete(f'{PRESTAMOS_URL}/{prestamo_id}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)