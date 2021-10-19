import abc
from re import A
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField, IntegerField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField

class FormAgregarVuelo(FlaskForm): # Form para las validaciones internas al agregar vuelo, falta el form para editar los vuelos
    CodVuelo = IntegerField('Código de vuelo', validators=[validators.required(), validators.length(max=3), validators.regexp("^[0-9]*$")]) 
    CiudadOrigen = StringField('Ciudad de Origen', validators=[validators.required(), validators.length(max=20)])
    CiudadDestino = StringField('Ciudad de Destino', validators=[validators.required(), validators.length(max=20)])
    FechaVuelo = StringField('Fecha de vuelo',validators=[validators.required(), validators.regexp("^(0[1-9]|[12][0-9]|3[01])[- /.]")])
    HoraVuelo = StringField('Hora de vuelo', validators=[validators.required(), validators.length(max=6)])
    CodPiloto = IntegerField('Código del piloto', validators=[validators.required(), validators.length(max=4), validators.regexp("^[0-9]*$")])
    CodAvion = IntegerField('Código del avión', validators=[validators.required(), validators.length(max=2), validators.regexp("^[0-9]*$")])
    enviar = SubmitField('Crear')
    
class FormReservaVuelo(FlaskForm):
    CodReserva = IntegerField('Código de reserva', validators=[validators.required(), validators.length(max=3), validators.regexp("^[0-9]*$")]) 
    UsuarioID = StringField('Usuario', validators=[validators.required(), validators.length(max=30, min=6) ])
    Origen = StringField('Ciudad de Origen', validators=[validators.required(), validators.length(max=20)])
    Destino = StringField('Ciudad de Destino', validators=[validators.required(), validators.length(max=20)])
    FechaVuelo = StringField('Fecha de vuelo',validators=[validators.required(), validators.regexp("^(0[1-9]|[12][0-9]|3[01])[- /.]")])
    NumeroPersonas = StringField('Hora de vuelo', validators=[validators.required(), validators.length(max=2)])
    CodVuelo = IntegerField('Código del avión', validators=[validators.required(), validators.length(max=3), validators.regexp("^[0-9]*$")])
    enviar = SubmitField('Reservar')    

'''
class FormRegistro(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(), validators.regexp("/^[A-Za-z]+$/")])
    apellido = StringField('Apellido',validators=[validators.required(), validators.regexp("/^[A-Za-z]+$/")])
    sexo = StringField('Sexo',validators=[validators.required()])
    fecha =  StringField('Fecha',validators=[validators.required(), validators.regexp("^(0[1-9]|[12][0-9]|3[01])[- /.]")])
    correo = StringField('Correo',validators=[validators.required(), validators.email()])
    usuario = StringField('Usuario', validators=[validators.required(), validators.length(max=30, min=6) ])
    contrasena = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=16, min=8)])
    confirmarContrasena = PasswordField('Validar Contraseña', validators=[validators.required(), validators.length(max=16, min=8)])
    enviar = SubmitField('Registrar')'''

class FormComentario(FlaskForm):
    UsuarioID = StringField('Usuario', validators=[validators.required(), validators.length(max=30, min=6) ])
    CodVuelo = IntegerField('Código del avión', validators=[validators.required(), validators.length(max=3), validators.regexp("^[0-9]*$")])
    Comentario = TextAreaField('Mensaje', validators=[validators.required(), validators.length(max=250)])
    enviar = SubmitField('Enviar')



class FormPiloto(FlaskForm):
    CodPiloto = IntegerField('Código del piloto', validators=[validators.required(), validators.length(max=2), validators.regexp("^[0-9]*$")])
    Nombre = StringField('Nombre',validators=[validators.required(), validators.regexp("/^[A-Za-z]+$/")])
    Apellidos = StringField('Apellido',validators=[validators.required(), validators.regexp("/^[A-Za-z]+$/")])
    UsuarioID = StringField('Usuario', validators=[validators.required(), validators.length(max=30, min=6) ])
    Sexo = StringField('Sexo',validators=[validators.required()])
    FechaNacimiento =  StringField('Fecha de nacimiento',validators=[validators.required(), validators.regexp("^(0[1-9]|[12][0-9]|3[01])[- /.]")])
    CorreoElectronico = StringField('Correo',validators=[validators.required(), validators.email()])
    enviar = SubmitField('Registrar')

class FormRegistroAdminsitrado(FlaskForm):
    Nombres = StringField('Nombre',validators=[validators.required(), validators.regexp("/^[A-Za-z]+$/")])
    Apellidos = StringField('Apellido',validators=[validators.required(), validators.regexp("/^[A-Za-z]+$/")])
    Sexo = StringField('Sexo',validators=[validators.required()])
    FechaNacimiento =  StringField('Fecha de nacimiento',validators=[validators.required(), validators.regexp("^(0[1-9]|[12][0-9]|3[01])[- /.]")])
    CorreoElectronico = StringField('Correo',validators=[validators.required(), validators.email()])
    UsuarioID = StringField('Usuario', validators=[validators.required(), validators.length(max=30, min=6) ])
    Contrasena = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=16, min=8)])
    confirmarContrasena = PasswordField('Validar Contraseña', validators=[validators.required(), validators.length(max=16, min=8)])
    enviar = SubmitField('Registrar')


'''
    mensaje = TextAreaField('Mensaje', validators=[validators.required(), validators.length(max=500)])
    tipo = RadioField('Tipo de Mensaje', choices=[('P','Pregunta'),('Q','Queja'),('S','Sugerencia')])
    enviar = SubmitField('Enviar Mensaje')
   respuesta = TextAreaField('Respuesta', validators=[validators.required(), validators.length(max=500)])
    enviar = SubmitField('Enviar Respuesta')
    '''