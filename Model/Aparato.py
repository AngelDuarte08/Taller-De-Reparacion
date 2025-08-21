from Database.Database import Database
class Aparato():
    def __init__(self):
        idAparato = ""
        equipo = ""
        memoria = ""
        almacenamiento = ""
        problema = ""
        diagnostico = ""
        reparacion = ""
        costo = ""
        status = ""

    def recibir(self, cliente, almacenamiento, memoria, fecha, tel, problema):
        Json = {"Cliente": cliente, "kd":"", "Estatus":"En diagnostoico"}
        db = Database()
        db.insertar(Json)


    def cotizar(self, id):
        pass 
    
    def entregar():
        pass
#dxxd