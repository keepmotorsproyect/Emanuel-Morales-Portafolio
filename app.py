from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return'¡Hola mundo desde Flask!'

@app.route('/saludo')
def inicio():
    return'Hola!'

@app.route('/')
def inicio():
    return'Página de inicio'

@app.route('/acerca')
def acerca():
    return'Página acerca de nosotros'

@app.route('/contacto')
def contacto():
    return'Página de contacto'

@app.route('/usuario/<nombre>')
def mostrar_usuario(nombre):
    return f'Perfil de usuario:{nombre}'

@app.route('/post/<int:post_id>')
def mostrar_post(post_id):
    return f'Mostrar el post número: {post_id}'


if __name__ == '__main__':
    app.run(debug=True)

