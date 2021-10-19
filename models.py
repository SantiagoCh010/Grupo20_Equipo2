import bd

class usuario():
    nombres = ''
    apellidos = ''
    sexo = ''
    fecha_nacimiento = ''
    correo = ''
    usuarioID = ''
    contrasena = ''
    
    def __init__(self, pnombres, papellidos, psexo, pfecha_nacimiento, pcorreo, pusuarioID, pcontrasena):
        self.nombres = pnombres
        self.papellidos = papellidos
        self.sexo = psexo
        self.fecha_nacimiento = pfecha_nacimiento
        self.correo = pcorreo
        self.usuarioID = pusuarioID
        self.contrasena = pcontrasena

    # Para esta función primero se debe colocar un boton de buscar en el template de edición de usuario del rol SuperAdmin, 
    # para saber cual de todos los ingresos es el que se quiere modificar 
    @classmethod
    def buscar(cls, pusuarioID):
        sql = "SELECT * FROM usuario WHERE usuarioID = ?;"
        resultado = bd.ejecutar_select(sql, [ pusuarioID ])
        if resultado:
            if len(resultado)>0:
                return cls(resultado[0]["nombres"], resultado[0]["apellidos"], 
                            resultado[0]["sexo"], resultado[0]["fecha_nacimiento"],
                            resultado[0]["correo"], resultado[0]["usuarioID"], resultado[0]["contrasena"])
            return None
    
    # Esta función sirve tanto para cuando el SuperAdmin va a crear un nuevo usuario,
    # como cuando un usuario nuevo se va a registrar
    def insertar(self):
        sql = "INSERT INTO usuario (nombres, apellidos, sexo, fecha_nacimiento, correo, usuarioID, contrasena) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.nombres, self.apellidos, self.sexo, self.fecha_nacimiento, self.correo, self.usuarioID, self.contrasena ])
        return (afectadas > 0)

    # Esta función sirve para que el SuperAdmin elimine un usuario
    def eliminar(self):
        sql = "DELETE usuario WHERE usuarioID = ?;"
        afectadas = bd.ejecutar_insert(sql, [ self.usuarioID ])
        return (afectadas > 0)

    # Esta función sirve tanto para cuando el SuperAdmin va a modificar un usuario,
    # como cuando un usuario va a actualizar su información (favor verificar estas líneas)
    def modificar(self):
        sql = "UPGRADE * SET usuario (nombres, apellidos, sexo, fecha_nacimiento, correo, usuarioID, contrasena) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.nombres, self.apellidos, self.sexo, self.fecha_nacimiento, self.correo, self.usuarioID, self.contrasena ])
        return (afectadas > 0)


class piloto():
    cod_piloto = 0
    nombres = ''
    apellidos = ''
    usuarioID = ''
    sexo = ''
    fecha_nacimiento = ''
    correo = ''
        
    def __init__(self, pcod_piloto, pnombres, papellidos, pusuarioID, psexo, pfecha_nacimiento, pcorreo):
        self.cod_piloto = pcod_piloto
        self.nombres = pnombres
        self.papellidos = papellidos
        self.usuarioID = pusuarioID
        self.sexo = psexo
        self.fecha_nacimiento = pfecha_nacimiento
        self.correo = pcorreo
        

    # Para esta función primero se debe colocar un boton de buscar en el template de edición de usuario del rol SuperAdmin, 
    # para saber cual de todos los ingresos es el que se quiere modificar 
    @classmethod
    def buscar(cls, pcod_piloto):
        sql = "SELECT * FROM piloto WHERE cod_piloto = ?;"
        resultado = bd.ejecutar_select(sql, [ pcod_piloto ])
        if resultado:
            if len(resultado)>0:
                return cls(pcod_piloto, resultado[0]["nombres"], resultado[0]["apellidos"], 
                            resultado[0]["usuarioID"], resultado[0]["sexo"], 
                            resultado[0]["fecha_nacimiento"], resultado[0]["correo"])
            return None
    
    # Esta función sirve tanto para cuando el SuperAdmin va a crear un nuevo piloto
    def insertar(self):
        sql = "INSERT INTO piloto (cod_piloto, nombres, apellidos, usuarioID, sexo, fecha_nacimiento, correo) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [self.cod_piloto, self.nombres, self.apellidos, self.usuarioID, self.sexo, self.fecha_nacimiento, self.correo ])
        return (afectadas > 0)

    # Esta función sirve para que el SuperAdmin elimine un piloto
    def eliminar(self):
        sql = "DELETE piloto WHERE cod_piloto = ?;"
        afectadas = bd.ejecutar_insert(sql, [ self.cod_piloto ])
        return (afectadas > 0)

    # Esta función sirve tanto para cuando el SuperAdmin va a modificar un piloto, (favor verificar estas líneas)
    def modificar(self):
        sql = "UPGRADE * SET piloto (cod_piloto, nombres, apellidos, usuarioID, sexo, fecha_nacimiento, correo) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [self.cod_piloto, self.nombres, self.apellidos, self.usuarioID, self.sexo, self.fecha_nacimiento, self.correo ])
        return (afectadas > 0)


class super_Admin():
    nombres = ''
    apellidos = ''
    sexo = ''
    fecha_nacimiento = ''
    correo = ''
    usuarioID = ''
    contrasena = ''
    
    def __init__(self, pnombres, papellidos, psexo, pfecha_nacimiento, pcorreo, pusuarioID, pcontrasena):
        self.nombres = pnombres
        self.papellidos = papellidos
        self.sexo = psexo
        self.fecha_nacimiento = pfecha_nacimiento
        self.correo = pcorreo
        self.usuarioID = pusuarioID
        self.contrasena = pcontrasena

    # Para esta función primero se debe colocar un boton de buscar en el template de edición de usuario del rol SuperAdmin, 
    # para saber cual de todos los ingresos es el que se quiere modificar 
    @classmethod
    def buscar(cls, pusuarioID):
        sql = "SELECT * FROM super_administrador WHERE usuarioID = ?;"
        resultado = bd.ejecutar_select(sql, [ pusuarioID ])
        if resultado:
            if len(resultado)>0:
                return cls(resultado[0]["nombres"], resultado[0]["apellidos"], 
                            resultado[0]["sexo"], resultado[0]["fecha_nacimiento"],
                            resultado[0]["correo"], resultado[0]["usuarioID"], resultado[0]["contrasena"])
            return None
    
    # Esta función sirve para crear un nuevo usuario_superAdmin
    def insertar(self):
        sql = "INSERT INTO super_administrador (nombres, apellidos, sexo, fecha_nacimiento, correo, usuarioID, contrasena) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.nombres, self.apellidos, self.sexo, self.fecha_nacimiento, self.correo, self.usuarioID, self.contrasena ])
        return (afectadas > 0)

    # Esta función sirve para que el SuperAdmin elimine un usuario_superAdmin
    def eliminar(self):
        sql = "DELETE super_administrador WHERE usuarioID = ?;"
        afectadas = bd.ejecutar_insert(sql, [ self.usuarioID ])
        return (afectadas > 0)

    # Esta función sirve tanto para cuando el SuperAdmin va a modificar un usuario_superAdmin, (favor verificar estas líneas)
    def modificar(self):
        sql = "UPGRADE * SET super_administrador (nombres, apellidos, sexo, fecha_nacimiento, correo, usuarioID, contrasena) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.nombres, self.apellidos, self.sexo, self.fecha_nacimiento, self.correo, self.usuarioID, self.contrasena ])
        return (afectadas > 0)


class comentario():
    num_comentario = 0
    usuarioID = ''
    cod_vuelo = 0
    comentario = ''
    
    def __init__(self, pnum_comentario, pusuarioID, pcod_vuelo, pcomentario):
        self.num_comentario = pnum_comentario
        self.usuarioID = pusuarioID
        self.cod_vuelo = pcod_vuelo
        self.comentario = pcomentario
        
       
    # Para esta función primero se debe colocar un boton de buscar en el template de comentarios
    @classmethod
    def buscar(cls, pnum_comentario):
        sql = "SELECT * FROM comentarios WHERE num_comentario = ?;"
        resultado = bd.ejecutar_select(sql, [ pnum_comentario ])
        if resultado:
            if len(resultado)>0:
                return cls(pnum_comentario, resultado[0]["usuarioID"], resultado[0]["cod_vuelos"], resultado[0]["comentario"])
            return None
    
    # Esta función sirve agregar un nuevo comentario
    def insertar(self):
        sql = "INSERT INTO comentarios (num_comentario, usuarioID, cod_vuelos, comentario) VALUES (?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.num_comentario, self.usuarioID, self.cod_vuelo, self.comentario ])
        return (afectadas > 0)

    # Esta función sirve para que el SuperAdmin elimine un usuario
    def eliminar(self):
        sql = "DELETE comentarios WHERE num_comentario = ?;"
        afectadas = bd.ejecutar_insert(sql, [ self.num_comentario ])
        return (afectadas > 0)

    # Esta función sirve tanto para cuando el SuperAdmin va a modificar un comentario, (favor verificar estas líneas)
    def modificar(self):
        sql = "UPGRADE * SET comentarios (num_comentario, usuarioID, cod_vuelos, comentario) VALUES (?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.num_comentario, self.usuarioID, self.cod_vuelo, self.comentario ])
        return (afectadas > 0)


    
class reservas():
    cod_reserva = 0
    usuarioID = ''
    origen = ''
    destino = ''
    fecha_vuelo = ''
    num_personas = 0
    cod_vuelo = ''

    
    def __init__(self, pcod_reserva, pusuarioID, porigen, pdestino, pfecha_vuelo, pnum_personas,  pcod_vuelo):
        self.cod_reserva = pcod_reserva
        self.usuarioID = pusuarioID
        self.origen = porigen
        self.destino = pdestino
        self.pfecha_vuelo = pfecha_vuelo
        self.num_personas = pnum_personas
        self.cod_vuelo = pcod_vuelo

    # Para esta función buscar una reserva
    @classmethod
    def buscar(cls, pcod_reserva):
        sql = "SELECT * FROM reserva_vuelos WHERE usuarioID = ?;"
        resultado = bd.ejecutar_select(sql, [ pcod_reserva ])
        if resultado:
            if len(resultado)>0:
                return cls(pcod_reserva, resultado[0]["usuarioID"],
                            resultado[0]["origen"], resultado[0]["destino"], 
                            resultado[0]["fecha_vuelo"],
                            resultado[0]["num_peronas"],  resultado[0]["cod_vuelo"])
            return None
    
    # Esta función sirve tanto para cuando el usuario/SuperAdmin cree una reserva
    def insertar(self):
        sql = "INSERT INTO reserva_vuelos (cod_reserva, usuarioID, origen, destino, fecha_vuelo, num_personas, cod_vuelo) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.cod_reserva, self.usuarioID, self.origen, self.destino, self.fecha_vuelo, self.num_personas, self.cod_vuelo ])
        return (afectadas > 0)

    # Esta función sirve para que el SuperAdmin elimine una reserva
    def eliminar(self):
        sql = "DELETE reserva_vuelos WHERE cod_reserva = ?;"
        afectadas = bd.ejecutar_insert(sql, [ self.cod_reserva ])
        return (afectadas > 0)

    # Esta función sirve para que el SuperAdmin modifique una reserva, (favor verificar estas líneas)
    def modificar(self):
        sql = "UPGRADE * SET reserva_vuelos cod_reserva, usuarioID, origen, destino, fecha_vuelo, num_personas, cod_vuelo) VALUES (?, ?, ?, ?, ?, ?, ?);"
        afectadas = bd.ejecutar_insert(sql, [ self.cod_reserva, self.usuarioID, self.origen, self.destino, self.fecha_vuelo, self.num_personas, self.cod_vuelo ])
        return (afectadas > 0)

