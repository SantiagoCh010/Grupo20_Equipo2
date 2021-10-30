import os
import functools
import secrets

from flask import Flask, request, g, url_for, flash, session
from modelos.uModels import User, Deletes, Admins, Pilotos
from modelos.vModels import Vuelos
from flask.templating import render_template
from werkzeug.utils import redirect
from datetime import timedelta
from sqlite3.dbapi2 import Error
from modelos.etemplates import *
from utils import *
#from forms import FormRegistro
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)

#Decorador para verificar que el usuario esté logeado
def login_requiered(view):
    @functools.wraps(view)
    def wrapped_view(**kargs):
        if g.user is None:
            return redirect( url_for('login') )
        
        return view(**kargs)
    
    return wrapped_view

# Usuarios que no sean administradores no pueden utilizar esta ruta
def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kargs):
        if g.usertype != "administrador":
            return redirect( url_for('home') )
        
        return view(**kargs)
    
    return wrapped_view

# Usuarios que no sean pilotos no pueden utilizar esta ruta
# La creé planeando utilizarla, pero no tuve la oportunidad (jejeje)
def pilot_required(view):
    @functools.wraps(view)
    def wrapped_view(**kargs):
        if g.usertype != "piloto":
            return redirect( url_for('home') )
        
        return view(**kargs)
    
    return wrapped_view

# El usuario normal no puede utilizar esta ruta
def user_notrequired(view):
    @functools.wraps(view)
    def wrapped_view(**kargs):
        if g.usertype == "usuario":
            return redirect( url_for('home') )
        
        return view(**kargs)
    
    return wrapped_view

# Función para guardar la imagen de perfil
def save_picture(profile_pic):
    try:
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(profile_pic.filename)
        if f_ext == '.png' or f_ext == '.jpg' or f_ext == '.jpeg':
            picture_fn = random_hex + f_ext
            picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
            profile_pic.save(picture_path)

            return picture_fn
        
        return ''
    except TypeError:
        print('Ocurrio un error al momento de guardar la imagen -' + str(TypeError))
        return ''

@app.before_request
def cargar_usuario():
    # Para saber si hay un usuario utilizando la app o no
    user = session.get('user')
    if user is None:
        g.user = None
    else:
        g.user = User.cargar(user)
        
        # Variables universales que permitirán saber características del usuario loggeado
        informacion = User.info_usuario(user)
        if informacion:
            for i in informacion:
                g.usuario = i["usuario"]
                g.sexo = i["sexo"]
                g.usertype = i["usertype"]
                g.image = i["img_profile"]

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Home/')
def Home():
    return render_template('Home.html')

@app.route('/ingresar', methods=['GET', 'POST'])
def login():
    if g.user: return redirect(url_for('home'))
    else:
        if request.method == 'GET':
            return render_template('Login.html')
        else:
            try:
                usr = request.form["userName"].replace("'", "")
                pwd = request.form["password"].replace("'", "")
                obj_user = User("", "", "", "", "", usr, pwd, "", "")
                if obj_user.autentificar():
                    session.clear()
                    session["user"] = usr
                    if request.form.get('rememberMe'): 
                        session.permanent = True
                        app.permanent_session_lifetime = timedelta(minutes=5)
                    return redirect(url_for('home'))
                
                flash("Usuario o Contraseña Incorrecta. Porfavor, Intente Nuevamente.")
                return render_template('login.html')
            
            except KeyError or TypeError:
                print("ha ocurrido un error al recibir los datos")

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if g.user: return redirect(url_for('home'))
    else:
        if request.method == 'GET':
            return render_template('Registro.html')
        else:
            if request.form:
                errores = ""
                try:
                    nombre = request.form['name']
                    apellido = request.form['surname']
                    sexo = request.form['sex']
                    birthday = request.form['birthday']
                    email = request.form['email']
                    user = request.form['username']
                    contraseña = request.form['password']
                    confirmacion = request.form.get('pconfirmation')
                    declaracion = request.form.get('TeC')
                    tipoUser = "usuario"

                    # Validaciones dentro del servidor con "utils"
                    if not isPasswordValid(contraseña): errores += 'La contraseña es invalida'
                    elif contraseña != confirmacion: errores += 'Las contraseñas son distintas. Intentelo nuevamente.'
                    if not isEmailValid(email): errores += 'El correo electronico es invalido'
                    
                    if declaracion != "checked": errores += 'Tiene que aceptar los Términos y condiciones'

                    obj_usuario = User(nombre, apellido, sexo, birthday, email, user, contraseña, '', tipoUser)
                    usr_unique = obj_usuario.unique('usuario', user)
                    email_unique = obj_usuario.unique('email', email)
                    
                    if usr_unique or email_unique: errores += (usr_unique +  " " + email_unique)

                    if not errores:
                        if obj_usuario.insertar():
                            mail = welcoming_email(sexo, email, nombre, apellido, user)
                            if mail: 
                                flash(mail)
                                return render_template('Registro.html')
                            #retornar al login
                            return redirect(url_for("login"))
                    else:
                        flash(errores)
                        return render_template('Registro.html')
                    
                except KeyError or TypeError:                
                    print("ha ocurrido un error al recibir los datos")
                    return render_template('Registro.html')

@app.route('/registrar/<string:admin>', methods=['GET', 'POST'])
@login_requiered
@admin_required
def adminregistrar(admin):
    if request.method == 'GET':
        return render_template('RegistroAdmin.html', admin=admin)
    else:
        if request.form:
            errores = ""
            try:
                nombre = request.form['name']
                apellido = request.form['surname']
                sexo = request.form['sex']
                birthday = request.form['birthday']
                email = request.form['email']
                user = request.form['username']
                contraseña = request.form['password']
                confirmacion = request.form.get('pconfirmation')
                tipoUser = request.form['userType']

                # Validaciones dentro del servidor con "utils"
                if not isPasswordValid(contraseña): errores += 'La contraseña es invalida'
                elif contraseña != confirmacion: errores += 'Las contraseñas son distintas. Intentelo nuevamente.'
                if not isEmailValid(email): errores += 'El correo electronico es invalido'
                
                obj_usuario = User(nombre, apellido, sexo, birthday, email, user, contraseña, '', tipoUser)
                usr_unique = obj_usuario.unique('usuario', user)
                email_unique = obj_usuario.unique('email', email)
                
                if usr_unique or email_unique: errores += (usr_unique +  " " + email_unique)
                if not errores:
                    if obj_usuario.insertar():
                        mail = welcoming_email(sexo, email, nombre, apellido, user)
                        if mail: 
                            flash(mail)
                            return render_template('RegistroAdmin.html')
                        #retornar al login
                        if obj_usuario.usertype == 'administrador': 
                            Admins(nombre + ' ' + apellido, user, email).insertar_admin()
                        if obj_usuario.usertype == 'piloto':
                            Pilotos(nombre + ' ' + apellido, user, email).insertar_piloto()
                        return redirect(url_for("home"))
                else:
                    flash(errores)
                    return render_template('RegistroAdmin.html')
                    
            except KeyError or TypeError:                
                print("ha ocurrido un error al recibir los datos")
                return render_template('RegistroAdmin.html')

@app.route('/información/usuarios/', methods=['GET', 'POST'])
@login_requiered
@admin_required
def ver_usuarios():
    informacion=User.usuarios_all()
    if request.method == 'GET':
        return render_template('VerUsuario.html', informacion=informacion)
    else:
        try:
            nombre = request.form['fullname']
            usertype = ''
            if request.form.get('userType'): usertype = request.form['userType']

            obj_user = User(nombre, '', '', '', '', '', '', '', usertype)

            return render_template('VerUsuario.html', informacion=obj_user.ver_usuarios(nombre, usertype))
        except Error as err:
            print('Ocurrió un error al momento de buscar el usuario: ' + err)

@app.route('/perfil/<string:user>', methods=['GET'])
@login_requiered
@admin_required
def informacion_admin(user):
    return render_template('InformacionUsuario.html', item=User.cargar(user))

@app.route('/perfil/', methods=['GET'])
@login_requiered
def informacion():
    return render_template('InformacionUsuario.html', item=User.cargar(g.usuario))

@app.route('/perfil/editar/<string:usuario>', methods=['GET', 'POST'])
@login_requiered
def editar_usuario(usuario=None):
    item = User.cargar(usuario)
    if request.method  == 'GET':
        return render_template('EditarUsuario.html', item=item)
    else:
        errores = mailerrors = ''
        try:
            nombre = request.form['name']
            apellido = request.form['surname']
            sexo = request.form['sex']
            birthday = request.form['birthday']
            email = request.form['email']
            user = request.form['username']
            p_pic = request.files['profile_file']

            if not isEmailValid(email): errores += 'El correo electronico es invalido'
            
            if p_pic:
                picture_file = save_picture(p_pic)
                if not picture_file:
                    flash('El archivo debe ser .png, .jpg o .jpeg', 'error')
                    if g.usertype == 'administrador': return redirect(url_for('informacion_admin', user=item.usuario))
                    return redirect(url_for('informacion'))
            else: picture_file = "placeholder-square.jpg"
            
            obj_usuario = User(nombre, apellido, sexo, birthday, email, user, None, picture_file, None)
            if item.usuario != user: errores += obj_usuario.unique('usuario', user)
            
            if not errores:
                if obj_usuario.editar(item.usuario):
                    if item.email != email: mailerrors += editar_mail(email, user) + " "
                    if item.usuario != user: mailerrors += edit_usuario(email, nombre, apellido, user)
                    if mailerrors: flash(mailerrors, 'error')
                    else: flash('El perfil fue editado exitosamente.', 'success')
                    
                    if g.usertype == 'administrador': return redirect(url_for('informacion_admin', user=item.usuario))
                    return redirect(url_for('informacion'))
            
            flash('Un error ocurrió al momento de editar el perfil. Vuelva a intentarlo', 'error')
            if g.usertype == 'administrador': return redirect(url_for('informacion_admin', user=item.usuario))
            return redirect(url_for('informacion'))

        except ValueError or TypeError:
            flash('Un error ocurrió al momento de editar el perfil. Vuelva a intentarlo', 'error')
            return redirect(url_for('información'))

@app.route('/perfil/borrar/<string:usuario>', methods=['GET', 'POST'])
@login_requiered
@admin_required
def eliminar_usuario(usuario=None):
    item = User.cargar(usuario)
    if request.method == 'GET':
        return render_template('EliminarUser.html', item=item)
    else:
        errores = ""
        try:
            user = request.form['username']
            email = request.form['email']
            password = request.form['password']
            comentario = request.form['comentario']

            if not isEmailValid(email): errores += 'El correo electronico es invalido'

            obj_admin = User('', '', '', '', '', g.usuario, password, '', '')
            if obj_admin.autentificar():
                obj_usuario = User('', '', '', '', email, user, '', '', '')
                if item.usertype == 'administrador': 
                    Admins(item.nombre + ' ' + item.apellido, user, email).eliminar_admin()
                if item.usertype == 'piloto':
                    Pilotos(item.nombre + ' ' + item.apellido, user, email).eliminar_piloto()
                
                obj_delete = Deletes(g.usuario, item.nombre + ' ' + item.apellido, email, comentario)

                obj_delete.insertar_del()

                if obj_usuario.eliminar():
                    goodbye_mail(email, item.nombre, item.apellido, user)
                    flash('El perfil fue eliminado exitosamente.', 'success')
                    return redirect(url_for('ver_usuarios'))
                
                flash('Ocurrió un error al momento de eliminar el usuario.', 'error')
                return redirect(url_for('ver_usuarios'))
            
            flash('Ocurrió un error al momento de eliminar el usuario.', 'error')
            return redirect(url_for('ver_usuarios'))
        
        except Error as err:
            print('Ha ocurrido un error al eliminar el usuario: ' + err)

@app.route('/perfil/vuelos/', methods=['GET', 'POST'])
@login_requiered
def ver_vuelos():
    informacion = Vuelos.vuelos_all()
    if request.method == 'GET':
        return render_template('VerVuelos.html', informacion=informacion)
    else:
        try:
            vuelo = request.form['IDVuelo']
            fecha = request.form['fecha']

            obj_vuelo = Vuelos(vuelo, '', '', '', '', fecha, '', '')

            return render_template('VerVuelos.html', informacion=obj_vuelo.ver_vuelos(vuelo, fecha))
        except Error as err:
            print('Ocurrió un error al momento de buscar el vuelo: ' + err)

# Reescribí el código de Santiago para poder trabajr con el y la dinámica de los usuarios
@app.route('/vuelos/itinerario/<string:piloto>', methods=['GET'])
@login_requiered
@user_notrequired
def ItinerarioVuelo(piloto):
    try:
        pilotName = Pilotos.cargar(piloto)
        vuelos_piloto = Vuelos.buscarItinerario(piloto)

        return render_template('ItinerarioVuelo.html', informacion=vuelos_piloto, pilotName=pilotName.nombre)
    
    except Error:
        print('Ha ocurrido un error al momento de mostrar el itinerario: ' + Error)
        flash('Ha ocurrio un error con el itinerario', 'error')
        if g.usertype == 'administrador': return redirect(url_for('informacion', user = pilotName.id))
        elif g.usertype == 'piloto': return redirect(url_for('informacion'))

@app.route("/cerrarsesion")
@login_requiered
def logout():
    session.clear()
    return redirect( url_for('login') )

# (Nataly)

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
    
@app.route('/CambiarContraseña/', methods=["GET",'PUT', 'POST'])
def CambContraseña():
    if request.method == "GET":
        return render_template('CambiarContraseña.html')    
    else: 
        if request.form:
            usuarioID = request.form['usuarioID']
            contrasena = request.form['password']
            obj_usuario = usuario('','','','','',usuarioID,contrasena)
            if obj_usuario.logearse():
                nuevaContrasena = request.form['nueva']
                if obj_usuario.modificarContra(usuarioID, nuevaContrasena):
                    return render_template('HomeUsuarioLogueado.html')

            return render_template('HomeUsuarioLogueado.html')

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
def consultar_vuelos():
    return render_template('ConsultaVuelo.html')

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

@app.route('/EliminarVuelo/', methods=["GET",'DELETE'])
def EliminarVuelo():
    return render_template('EliminarVuelo.html')

@app.route('/HomeAdministrador/', methods=['GET','POST'])
def HomeAdministrador():
    if request.method == "GET":        
        return render_template('HomeAdministradorLogueado.html')
    else:        
        if request.form:            
            busquedaOrigen = request.form["BsOrigen"]
            busquedaDestino = request.form["BsDestino"]
            busquedaFecha = request.form["BsFecha"]
            busquedaNumeroPersonas = request.form["BsPersona"]
            error = ""                       

            if len(busquedaOrigen)< 2:
                error= "-Debe escribir un lugar de origen valido- "
            
            if len(busquedaDestino)<2:
                error += "-Debe escribir un lugar de destino valido- "
            
            if len(busquedaFecha)<2:
                error +="-Debe escribir una fecha valida- "                
            
            if len(busquedaNumeroPersonas)<1:
                error +="-El numero de personas debe ser mayor de cero- "
            
            if not error:                
                BusquedaVuelo = vuelo.buscarPorHome(busquedaOrigen, busquedaDestino, busquedaFecha)                             
                if (BusquedaVuelo):                                                    
                    return render_template('HomeAdministradorLogueado.html', lista = BusquedaVuelo) 
                else:                                        
                    return render_template('HomeAdministradorLogueado.html', error= "Vuelos no encontrados") 
            else:                   
                return render_template('HomeAdministradorLogueado.html', error = error)  
            

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

@app.route('/RecuperarContraseña/', methods=["GET",'POST'])
def RecuperarContraseña():
    if request.method == "GET":
        return render_template('RecuperarContraseña.html')        
    else:
            nombreDeUsuario = request.form["userName"]
            email = request.form["email"]
            error = ""

            if not isUsernameValid(nombreDeUsuario):
                error+= "Debe escribir un nombre de usuario valido . "
            
            if not isEmailValid(email):
                error += "Debe escribir un email valido . "
            
            if not error:
                contrasenaRecuperada = usuario.BuscarRecuperarContrasena(nombreDeUsuario, email)                
                if (contrasenaRecuperada ):                     
                    print()                     
                    yag = yagmail.SMTP("alertaeropuertojuancaseano@gmail.com","Equipo2_alert") 
                    yag.send(to=email, subject="Alerta recuperar contraseña",
                             contents= "Estimado usuario, La contraseña de " + nombreDeUsuario + 
                             " es "+ contrasenaRecuperada[0]["contrasena"]  ) 
                    return render_template("RecuperarContraseña.html", errores = "Se ha enviado un correo electronico con su contraseña")
                else:
                    return render_template("RecuperarContraseña.html", errores = "Usuario no encontrado")
            else:
                return render_template("RecuperarContraseña.html", errores = error)

@app.route('/ReservaVuelo/', methods=['GET','POST'])
def reservar_vuelo():
    return render_template('ReservaVuelo.html')

