from flask import Flask, render_template,redirect,jsonify,request

app = Flask(__name__)


@app.route("/")
def ingresar():
    return render_template("registro-login.html")

@app.route('/seccion', methods=['POST'])
def seccion():
    usuario = request.form['usuario']
    password = request.form['clave']

    if usuario == 'goku' and password == 'colombia':
        return redirect('/iniciar')
    else:
        return redirect('/')

@app.route("/iniciar" , methods=["GET", "POST"])
def iniciar():
    return render_template("index.html")

@app.route("/perfil", methods=["GET", "POST"])
def perfil():
    
    return render_template("perfil-usuario-portada.html")

@app.route("/perfil/seccion_perfil", methods=["GET", "POST"])
def seccion_perfil():
    
    return render_template("seccion-perfil-usuario.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
