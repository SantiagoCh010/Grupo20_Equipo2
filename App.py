import os
from flask import Flask, render_template, request, redirect, url_for, session
from utils import *
#from forms import FormRegistro
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)


@app.route('/', methods=["GET",'POST'])
def index():
    return render_template('Home.html')    

@app.route('/AgregarVuelo/', methods=["GET",'POST'])
def AgregarVuelo():
        if request.method == "GET":
        #formulario = FormRegistro()
            return render_template('AgregarVuelo.html')    
        else: 
            if request.form:
                cod_vuelo = request.form['vuelo']
                ciudad_origen = request.form['origen']
                ciudad_destino = request.form['destino']
                fecha_vuelo = request.form['departure-D']
                hora_vuelo = request.form['departure-H']
                cod_piloto = request.form['pilotID']
                cod_avion = request.form['airplane']
                estado = "A tiempo"

                obj_usuario = vuelo(cod_vuelo , cod_avion , cod_piloto , ciudad_origen ,  ciudad_destino ,  fecha_vuelo , hora_vuelo , estado)
                if obj_usuario.insertar():
                    return render_template('AgregarVuelo.html', mensaje="Se registró el usuario exitosamente.")

                return render_template('AgregarVuelo.html', mensaje="Todos los datos son obligatorios.")
    
@app.route('/CambiarContraseña/', methods=["GET",'PUT'])
def CambContraseña():
    return render_template('CambiarContraseña.html')

@app.route('/Comentarios/', methods=["GET", "POST"])
def Comentarios():
    if request.method == "GET":
        return render_template('ComentarioVuelos.html')
    else:
        if request.form:
            usr = request.form["usuarioID"]
            cod_vuelo = request.form["vuelo"]
            comentario = request.form["comentario"]
            numero = request.form["usuarioID"]

            obj_comentario = comentarios(numero, usr,cod_vuelo, comentario)
            if obj_comentario.insertar():
                return redirect( url_for('HomeUser'))
            
            return render_template('ComentarioVuelos.html')    

@app.route('/ConsultaVuelos/', methods=['GET'])
def ConsultaVuelos():
    return render_template('ConsultaVuelo.html')

@app.route('/EdicionUsuario/', methods=["GET",'PUT'])
def EdicionUsuario():
    return render_template('EdicionUsuario.html')

@app.route('/EditarUsuario/', methods=["GET",'PUT'])
def EditarUsuario():
    return render_template('EditarUsuario.html')

@app.route('/EditarVuelo/', methods=["GET",'PUT','POST'])
def EditarVuelo():
        if request.method == "GET":
            return render_template('EditarVuelo.html')    
        else: 
            if request.form:
                cod_vuelo = request.form['vuelo']
                ciudad_origen = request.form['origen']
                ciudad_destino = request.form['destino']
                fecha_vuelo = request.form['departure-D']
                hora_vuelo = request.form['departure-H']
                cod_piloto = request.form['pilotID']
                cod_avion = request.form['airplane']
                estado = request.form['estado']

                obj_usuario = vuelo(cod_vuelo , cod_avion , cod_piloto , ciudad_origen ,  ciudad_destino ,  fecha_vuelo , hora_vuelo , estado)
                if obj_usuario.modificar():
                    return render_template('EditarVuelo.html')

                return render_template('EditarVuelo.html')

@app.route('/EliminarUser/', methods=["GET",'DELETE'])
def EliminarUser():
    return render_template('EliminarUser.html')

@app.route('/EliminarVuelo/', methods=["GET",'DELETE'])
def EliminarVuelo():
    return render_template('EliminarVuelo.html')

@app.route('/Home/', methods=['GET','POST'])
def Home():
    return render_template('Home.html')

@app.route('/HomeAdministrador/', methods=['GET','POST'])
def HomeAdministrador():
    return render_template('HomeAdministradorLogueado.html')

@app.route('/HomePiloto/', methods=['GET','POST'])
def HomePiloto():
    return render_template('HomePilotoLogueado.html')

@app.route('/HomeUser/', methods=['GET','POST'])
def HomeUser():
    return render_template('HomeUsuarioLogueado.html')

@app.route('/InfoPiloto/', methods=['GET'])
def InfoPiloto():
    return render_template('InformacionPiloto.html')

@app.route('/InfoUser/', methods=['GET'])
def InfoUser():
    return render_template('InformacionUsuario.html')

@app.route('/ItinerarioVuelo/', methods=['GET'])
def ItinerarioVuelo():
    return render_template('ItinerarioVuelo.html')

@app.route('/Login/', methods=['POST','GET'])
def Login():
    if request.method == "GET":
        return render_template('Login.html')
    else:
        usr = request.form["userName"]
        pwd = request.form["password"]

        obj_usuario = usuario('','','','','',usr,pwd)
        if obj_usuario.logearse():
            session.clear()
            session["nombre_usuario"] = usr
            return redirect( url_for('HomeUser'))
        
        return render_template('Login.html', mensaje="Nombre de usuario o contraseña incorrecta.")    


@app.route('/RecuperarContraseña/', methods=["GET",'POST'])
def RecuperarContraseña():
    return render_template('RecuperarContraseña.html')

@app.route('/RegistroUsuario/', methods=['GET','POST'])
def RegistroUsuario():
    if request.method == "GET":
        #formulario = FormRegistro()
        return render_template('RegistroUsuario.html')    
    else: 

        ''' #La forma de hacerlo si tuvieras la validación del formswtf
        formulario = FormRegistro(request.form)
        if formulario.validate_on_submit():
            return render_template('RegistroUsuario.html',mensaje="Registro exitoso.", form=formulario)
        return render_template('RegistroUsuario.html', mensaje="Registro inválido, compruebe los campos", form=formulario)'''
        if request.form:
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            sexo = request.form['sexo']
            fecha_nacimiento = request.form['fecha_nacimiento']
            correo = request.form['correo']
            usuarioID = request.form['usuarioID']
            contrasena = request.form['contrasena']
            #tipoUsuario = request.form['']

            obj_usuario = usuario(nombres, apellidos, sexo, fecha_nacimiento, correo, usuarioID, contrasena)
            if obj_usuario.insertar():
                return render_template('RegistroUsuario.html', mensaje="Se registró el usuario exitosamente.")

            return render_template('RegistroUsuario.html', mensaje="Todos los datos son obligatorios.")

@app.route('/RegistroUsuarioAdmin/', methods=['GET','POST'])
def RegistroUsuarioAdmin():
    return render_template('RegistroUsuarioSuperAdmin.html')

@app.route('/ReservaVuelo/', methods=['GET','POST'])
def ReservaVuelo():
    return render_template('ReservaVuelo.html')
