from flask import Flask, render_template

app = Flask(__name__)

@app.route('/AgregarVuelo')
def AgregarVuelo():
    return render_template('AgregarVuelo.html')

@app.route('/CambiarContraseña')
def CambContraseña():
    return render_template('CambiarContraseña.html')

@app.route('/Comentarios')
def Comentarios():
    return render_template('ComentarioVuelos.html')

@app.route('/ConsultaVuelos')
def ConsultaVuelos():
    return render_template('ConsultaVuelo.html')

@app.route('/EdicionUsuario')
def EdicionUsuario():
    return render_template('EdicionUsuario.html')

@app.route('/EditarUsuario')
def EditarUsuario():
    return render_template('EditarUsuario.html')

@app.route('/EditarVuelo')
def EditarVuelo():
    return render_template('EditarVuelo.html')

@app.route('/EliminarUser')
def EliminarUser():
    return render_template('EliminarUser.html')

@app.route('/EliminarVuelo')
def EliminarVuelo():
    return render_template('EliminarVuelo.html')

@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/HomeAdministrador')
def HomeAdministrador():
    return render_template('HomeAdministradorLogueado.html')

@app.route('/HomePiloto')
def HomePiloto():
    return render_template('HomePilotoLogueado.html')

@app.route('/HomeUser')
def HomeUser():
    return render_template('HomeUsuarioLogueado.html')

@app.route('/InfoPiloto')
def InfoPiloto():
    return render_template('InformacionPiloto.html')

@app.route('/InfoUser')
def InfoUser():
    return render_template('InformacionUsuario.html')

@app.route('/ItinerarioVuelo')
def ItinerarioVuelo():
    return render_template('ItinerarioVuelo.html')

@app.route('/login')
def Login():
    return render_template('Login.html')

@app.route('/RecuperarContraseña')
def RecuperarContraseña():
    return render_template('RecuperarContraseña.html')

@app.route('/RegistroUsuario')
def RegistroUsuario():
    return render_template('RegistroUsuario.html')

@app.route('/RegistroUsuarioAdmin')
def RegistroUsuarioAdmin():
    return render_template('RegistroUsuarioSuperAdmin.html')

@app.route('/ReservaVuelo')
def ReservaVuelo():
    return render_template('ReservaVuelo.html')
