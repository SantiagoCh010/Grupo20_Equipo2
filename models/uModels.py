import db
from werkzeug.security import generate_password_hash, check_password_hash

class User():
    nombres = ""
    apellidos = ""
    sexo = ""
    fecha_nacimiento = ""
    email = ""
    usuario = ""
    contrasena = ""
    img_profile = ""
    usertype = ""

    def __init__(self, pnombre, padellido, psexo, pbirthday, pemail ,pusuario, pcontrasena, pimg, ptype):
        self.nombre = pnombre
        self.apellido = padellido
        self.sexo = psexo
        self.fecha_nacimiento = pbirthday
        self.email = pemail
        self.usuario = pusuario
        self.contrasena = pcontrasena
        self.img_profile = pimg
        self.usertype = ptype
    
    @classmethod
    def cargar(cls, pusuario):
        sql = '''SELECT nombres, apellidos, sexo, fecha_nacimiento, email, usuario, img_profile, usertype 
               FROM Usuario WHERE usuario = ?;'''
        resultado = db.ejecutar_select(sql, [ pusuario ])
        if resultado:
            if len(resultado)>0:
                return cls(resultado[0]["nombres"], resultado[0]["apellidos"], resultado[0]["sexo"],
                resultado[0]["fecha_nacimiento"], resultado[0]["email"], resultado[0]["usuario"], 
                '********' , resultado[0]["img_profile"], resultado[0]["usertype"])
        
        return None

    def autentificar(self):
        sql = "SELECT * FROM Usuario WHERE usuario = ?;"
        obj = db.ejecutar_select(sql, [ self.usuario ])
        if obj:
            if len(obj) > 0:
                if check_password_hash(obj[0]["contrasena"], self.contrasena):
                    return True
            
            return False
    
    def insertar(self):
        sql = '''INSERT INTO Usuario (nombres, apellidos, sexo, fecha_nacimiento, email, 
        usuario, contrasena, usertype) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''
        hashed_pwd = generate_password_hash(self.contrasena, method='pbkdf2:sha256', salt_length=15)
        
        afectadas = db.ejecutar_insert(sql, [self.nombre, self.apellido, self.sexo, self.fecha_nacimiento,
        self.email, self.usuario, hashed_pwd, self.usertype])
        return ( afectadas > 0 )

    def eliminar(self):
        sql = '''DELETE FROM Usuario WHERE usuario = ? AND email = ?'''
        afectadas = db.ejecutar_insert(sql, [self.usuario, self.email])
        return ( afectadas > 0 )

    def editar(self, usuario):
        sql = '''UPDATE Usuario SET nombres = ?, apellidos = ?, sexo = ?, fecha_nacimiento = ?, 
        email = ?, usuario = ?, img_profile = ? WHERE usuario = ?'''
        afectadas = db.ejecutar_insert(sql, [self.nombre, self.apellido, self.sexo, self.fecha_nacimiento,
        self.email, self.usuario, self.img_profile, usuario])
        return ( afectadas > 0 )

    @staticmethod
    def info_usuario(usuario):
        sql = "SELECT * FROM Usuario WHERE usuario = ?;"
        return db.ejecutar_select(sql, [usuario])
    
    @staticmethod
    def ver_usuarios(nombre, usertype):
        if nombre and not usertype: 
            return db.ejecutar_select("SELECT * FROM Usuario WHERE nombres = ?;", [nombre])
        if not nombre and usertype: 
            return db.ejecutar_select("SELECT * FROM Usuario WHERE usertype = ?;", [usertype])
        return db.ejecutar_select("SELECT * FROM Usuario WHERE nombres = ? AND usertype = ?;", [nombre, usertype])
        
    @staticmethod
    def usuarios_all():
        sql = "SELECT * FROM Usuario ORDER BY usuario;"
        return db.ejecutar_select(sql, None)
    
    @staticmethod
    def unique(field, value):
        sql = "SELECT " + field + " FROM Usuario WHERE " + field + " = ?;"
        obj = db.ejecutar_select(sql, [ value ])
        if obj:
            if len(obj) > 0:
                return "El " + field + " ya esta en uso"
        
        return ""

class Deletes():
    admin = ""
    nombre = ""
    email = ""
    motivo = ""

    def __init__(self, padmin, pnombre, pemail, pmotivo):
        self.admin = padmin
        self.nombre = pnombre
        self.email = pemail
        self.motivo = pmotivo

    def insertar_del(self):
        sql = '''INSERT INTO UsuariosEliminados (adminID, nombre_completo, email, motivo)
              VALUES (?, ?, ?, ?);'''
        afectadas = db.ejecutar_insert(sql, [self.admin, self.nombre, self.email, self.motivo])
        return ( afectadas > 0 )

class Admins():
    nombre = ""
    id = ""
    email = ""

    def __init__(self, pnombre, pid, pemail):
        self.nombre = pnombre
        self.id = pid
        self.pemail = pemail

    @classmethod
    def cargar(cls, padmin):
        slq = '''SELECT nombre_completo, adminID, email FROM Administradores WHERE adminID = ?;'''
        resultado = db.ejecutar_select(slq, padmin)
        if resultado:
            if len(resultado)>0:
                return cls(resultado[0]["nombre_completo"], resultado[0]["adminID"], resultado[0]["email"])
    
    def insertar_admin(self):
        sql = '''INSERT INTO Administradores (nombre_completo, adminID, email) VALUES (?, ?, ?);'''
        afectadas = db.ejecutar_insert(sql, [self.nombre, self.id, self.email])
        return ( afectadas > 0 )
    
    def editar_admin(self):
        sql = '''UPDATE Administradores SET nombre_completo = ?, adminID = ?, email = ?, 
              WHERE adminID = ?;'''
        afectadas = db.ejecutar_insert(sql, [self.nombre, self.id, self.email])
        return ( afectadas > 0 )
    
    def eliminar_admin(self):
        sql = '''DELETE FROM Administradores WHERE adminID = ?;'''
        afectadas = db.ejecutar_insert(sql, [self.id])
        return ( afectadas > 0 )

class Pilotos():
    nombre = ""
    id = ""
    email = ""

    def __init__(self, pnombre, pid, pemail):
        self.nombre = pnombre
        self.id = pid
        self.email = pemail

    @classmethod
    def cargar(cls, pnombre):
        slq = '''SELECT * FROM Pilotos WHERE pilotoID = ?;'''
        resultado = db.ejecutar_select(slq, [pnombre])
        if resultado:
            if len(resultado)>0:
                return cls(resultado[0]["nombre_completo"], resultado[0]["pilotoID"], resultado[0]["email"])
    
    def insertar_piloto(self):
        sql = '''INSERT INTO Pilotos (nombre_completo, pilotoID, email) VALUES (?, ?, ?);'''
        afectadas = db.ejecutar_insert(sql, [self.nombre, self.id, self.email])
        return ( afectadas > 0 )
    
    def editar_piloto(self):
        sql = '''UPDATE Pilotos SET nombre_completo = ?, pilotoID = ?, email = ?, 
              WHERE pilotoID = ?;'''
        afectadas = db.ejecutar_insert(sql, [self.nombre, self.id, self.email])
        return ( afectadas > 0 )
    
    def eliminar_piloto(self):
        sql = '''DELETE FROM Pilotos WHERE pilotoID = ?;'''
        afectadas = db.ejecutar_insert(sql, [self.id])
        return ( afectadas > 0 ) 
    
