from flask import Flask, render_template, request # type: ignore
import forms # type: ignore
from zodiaco import ZodiacoForm # type: ignore
from datetime import datetime # type: ignore

app = Flask(__name__)

app.secret_key = '161103'

# Ruta principal
@app.route("/")
def index1():
    titulo = "IDGS805"
    lista = ["Python", "Java", "C#", "JavaScript"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    mat=''
    nom = ''
    ape=''
    email=''
    alumno_clase=forms.UserForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data
    return render_template("Alumnos.html", form=alumno_clase,mat=mat, nom=nom, ape=ape, email=email)
    
def calcular_edad(año, mes, dia):
    hoy = datetime.today()
    edad = hoy.year - año
    if (hoy.month, hoy.day) < (mes, dia):
        edad -= 1
    return edad

def obtener_signo_zodiaco_chino(año):
    signos = ["Rata", "Buey", "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]
    return signos[(año - 1900) % 12]

@app.route('/Zodiaco', methods=['GET', 'POST'])
def index():
    form = ZodiacoForm(request.form)
    nombre = None
    apellidopaterno = None
    apellidomaterno = None
    dia = None
    mes = None
    año = None
    sexo = None
    edad = None
    signo_zodiaco = None

    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        apellidopaterno = form.apellidopaterno.data
        apellidomaterno = form.apellidomaterno.data
        dia = form.dia.data
        mes = form.mes.data
        año = form.año.data
        sexo = form.sexo.data

        edad = calcular_edad(año, mes, dia)
        signo_zodiaco = obtener_signo_zodiaco_chino(año)

    return render_template('zodiaco.html', 
                           form=form, 
                           nombre=nombre, 
                           apellidopaterno=apellidopaterno,
                           apellidomaterno=apellidomaterno,
                           dia=dia, 
                           mes=mes, 
                           año=año, 
                           sexo=sexo, 
                           edad=edad, 
                           signo_zodiaco=signo_zodiaco)
# Rutas con parámetros dinámicos
@app.route('/user/<string:user>')
def user(user):
    return f'Hola {user}'

@app.route("/numero/<int:n>")
def numero(n):
    return f'Numero: {n}'

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f"Usuario: {username}, con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route("/default")
@app.route("/default/<string:tem>")
def funcion1(tem="Juan"):
    return f"Hola {tem}"

@app.route('/adios')
def adios():
    return 'Adios Mundo'

# Rutas de formularios
@app.route("/formulario")
def form1():
    return """
        <form>
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre">
            <label for="apellido">Apellido:</label>
            <input type="text" id="apellido" name="apellido">
        </form>
    """

# Rutas de operaciones matemáticas
@app.route("/operaciones")
def operaciones():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        num1 = request.form.get("n1")  # Obtiene el valor de n1
        num2 = request.form.get("n2")  # Obtiene el valor de n2
        return f"La multiplicación de {num1} x {num2} es: {int(num1) * int(num2)}"
    return "Método no permitido"

@app.route("/resultado2", methods=["GET", "POST"])
def result2():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("operacion")

        if not num1 or not num2 or not operacion:
            return "Por favor, completa todos los campos y selecciona una operación."

        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            return "Por favor, ingresa números válidos."
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 == 0:
                return "No se puede dividir por cero."
            resultado = num1 / num2
        else:
            return "Operación no válida"
        # Pasar el resultado y la operación a la plantilla
        return render_template("OperasBas.html", resultado=resultado, operacion=operacion)
    return render_template("OperasBas.html")

# Rutas de plantillas adicionales
@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html")

# rutas para cinepolis
@app.route("/cinepolis1")
def cinepolis1():
    return render_template("cinepolis1.html")

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=8000)