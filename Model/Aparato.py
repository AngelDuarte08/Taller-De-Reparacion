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
    def recibir (self, cliente, equipo, memoria, almacenamiento, problema, estatus):
        json = {"Cliente" : cliente, "Equipo" : equipo, "Memoria" : memoria, "Alamacenamiento" : almacenamiento, "Problema" : problema, "Estatus" : "En diagnostico"}
        db = Database()
        db.insertar(json, "collection")
    
    def cotizar (self, diagnostico, reparacion, costo , id, estatus):
        json = {"_id": ObjectId(id)},{"$set":{"Diagnostico" : diagnostico, "Reparacion" : reparacion, "Costo" : costo, "Estatus" : "En reparacion"}}
        db = Database()
        db.insertar(json, "collection")
    
        
    def entregar (self, id, status):
        json = {"_id": ObjectId(id)},{"$set":{ "Estatus" : "Entregado"}}
        db = Database()
        db.insertar(json, "collection")

