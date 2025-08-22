from Database.Database import Database
from bson.objectid import ObjectId

class Aparato ():
    def __init__ (self):
        self.__id_equipo = ""
        self.__equipo = ""
        self.__memoria = ""
        self.__almacemiento = ""
        self.__problema = ""
        self.__diagnostico = ""
        self.__reparacion = ""
        self.__costo = ""
        self.__estatus = ""
    def recibir (self, cliente, tel , equipo, memoria, almacenamiento, problema, fecha):
        json = {"Cliente" : cliente, "Telefono":tel, "Equipo" : equipo, "Memoria" : memoria, "Alamacenamiento" : almacenamiento, "Problema" : problema, "Fecha_recibido ": fecha ,"Estatus" : "En diagnostico"}
        db = Database()
        db.insertar(json, "Aparatos")
    
    def cotizar (self, diagnostico, reparacion, costo , id, estatus):
        json = {"_id": ObjectId(id)},{"$set":{"Diagnostico" : diagnostico, "Reparacion" : reparacion, "Costo" : costo, estatus : "En reparacion"}}
        db = Database()
        db.insertar(json, "Aparatos")
    
        
    def entregar (self, id, estatus):
        json = {"_id": ObjectId(id)},{"$set":{ estatus : "Entregado"}}
        db = Database()
        db.insertar(json, "Aparatos")

    def diagnostico(self, tel, cliente, descripcion, solucion, costo, fecha, tecnico):
        filtro = {"Cliente": cliente, "Telefono": tel}
        actualizacion = {
            "$set": {
                "Descripcion": descripcion,
                "Solucion": solucion,
                "Costo": costo,
                "Fecha_diagnostico": fecha,
                "Tecnico": tecnico
            }
        }
        db = Database()
        db.actualizar(filtro, actualizacion, "Aparatos")

