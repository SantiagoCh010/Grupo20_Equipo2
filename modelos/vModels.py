import db

class Vuelos():
    codVuelos = 0
    codAvion = 0
    codPiloto = ""
    origen = ""
    destino = ""
    fechaVuelo = ""
    horaVuelo = ""
    estado = ""

    def __init__(self, idvuelo, idavion, idpilot, porigen, pdestino, pfecha, phora, pestado):
        self.codVuelos = idvuelo
        self.codAvion = idavion
        self.codPiloto = idpilot
        self.origen = porigen
        self.destino = pdestino
        self.fechaVuelo = pfecha
        self.horaVuelo = phora
        self.estado = pestado
    
    @classmethod
    def cargar(cls, idvuelo):
        sql = '''SELECT codVuelos, codAvion, codPiloto, ciudadOrigen, ciudadDestino, fechaVuelo, 
              horaVuelo, estado FROM Vuelos WHERE codVuelos = ?;'''
        resultado = db.ejecutar_select(sql, [ idvuelo ])
        if resultado:
            if len(resultado)>0:
                return cls(resultado[0]["codVuelos"], resultado[0]["codAvion"], resultado[0]["codPiloto"],
                resultado[0]["origen"], resultado[0]["destino"], resultado[0]["fechaVuelo"], 
                resultado[0]["horaVuelo"], resultado[0]["estado"])
        
        return None

    @staticmethod
    def vuelos_all():
        sql = "SELECT * FROM Vuelos ORDER BY codVuelos;"
        return db.ejecutar_select(sql, None)

    @staticmethod
    def ver_vuelos(idvuelo, fecha):
        if idvuelo and not fecha:
            return db.ejecutar_select("SELECT * FROM Vuelos WHERE codVuelos = ?;", [idvuelo])
        if not idvuelo and fecha:
            return db.ejecutar_select("SELECT * FROM Vuelos WHERE fechaVuelo = ?;", [fecha])
        return db.ejecutar_select("SELECT * FROM Vuelos WHERE codVuelos = ? AND fechaVuelo = ?;", [idvuelo, fecha])
    
    @staticmethod
    def buscarItinerario(codPiloto):
        sql = "SELECT * FROM Vuelos WHERE codPiloto= ?;"      
        return db.ejecutar_select(sql, [codPiloto])
