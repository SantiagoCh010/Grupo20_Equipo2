from smtplib import SMTPAuthenticationError
import yagmail as mail
# Hotmail de la página
yag = mail.SMTP('alertaeropuertojuancaseano@gmail.com', 'Equipo2_alert')

def welcoming_email(user_sexo, user_mail, user_name, user_sur, user):
    try:    
        welcome = ""
        if user_sexo == "femenino": welcome += "Bienvenida"
        elif user_sexo == "noDefinido": welcome += "Bienvenidx"
        elif user_sexo == "masculino": welcome += "Bienvenido"

        # Se envía un correo al usuario informandole de su registro en la página
        yag.send(
            to=user_mail, 
            subject= "Su cuenta ha sido registrada con exito", 
            contents='''{0} {1},
                
                Gracias por registrarte con el Aeropuerto Juan Casiano, esperamos que nos acompañes por un largo tiempo.
                Tu usuario, {2}, ha sido registrado con exito.
                
                Aeropuerto Juan Casiano.'''.format(welcome, user_name+" "+user_sur, user))
        
        return ""
    
    except ValueError or mail.YagAddressError or SMTPAuthenticationError:
        return "yag no funcionando"

def edit_usuario(user_mail, user_name, user_sur, user):
    try:    
        # Se envía un correo al usuario informandole de la eliminación de este en la página
        yag.send(
            to=user_mail, 
            subject= "Edición de cuenta", 
            contents='''Hola {0},
                
                Nos dimos cuenta que acabaste de editar el usuario de tu cuenta. 
                Recuerda, tu nuevo usuario es: {1}. 
                
                Aeropuerto Juan Casiano.'''.format(user_name+" "+user_sur, user))
        
        return ""
    
    except ValueError or mail.YagAddressError or SMTPAuthenticationError:
        return "yag no funcionando"

def editar_mail(user_mail, user):
    try:    
        # Se envía un correo al usuario informandole de la eliminación de este en la página
        yag.send(
            to=user_mail, 
            subject= "Edición de cuenta", 
            contents='''Hola {0},
                
                Nos dimos cuenta que acabaste de editar el correo electrónico de tu cuenta. 
                Es este tu nuevo correo electrónico?
                
                Aeropuerto Juan Casiano.'''.format(user))
        
        return ""
    
    except ValueError or mail.YagAddressError or SMTPAuthenticationError:
        return "yag no funcionando"

def edit_contraseña(user_mail, user, user_pwd):
    try:    
        # Se envía un correo al usuario informandole de la eliminación de este en la página
        yag.send(
            to=user_mail, 
            subject= "Recuperar Contraseña", 
            contents='''Hola {0},
                
                ¿Se te olvidó tu contraseña?
                Tu contraseña temporal es: {1}.
                Recuerda cambiarla lo más antes posible.
                
                Aeropuerto Juan Casiano.'''.format(user, user_pwd))
        
        return ""
    
    except ValueError or mail.YagAddressError or SMTPAuthenticationError:
        return "yag no funcionando"

def goodbye_mail(user_mail, user_name, user_sur, user):
    try:    
        # Se envía un correo al usuario informandole de la eliminación de este en la página
        yag.send(
            to=user_mail, 
            subject= "Eliminación de cuenta: {0}".format(user), 
            contents='''Hola {0},
                
                Nos entristece dejarte ir, pero al parecer nuestros caminos hasta aquí han llegado. 
                
                Esperamos que sigas volando con nosotros.
                Aeropuerto Juan Casiano.'''.format(user_name+" "+user_sur))
        
        return ""
    
    except ValueError or mail.YagAddressError or SMTPAuthenticationError:
        return "yag no funcionando"
