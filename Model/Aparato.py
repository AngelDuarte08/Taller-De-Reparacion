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
        json = {"Cliente" : cliente, "Telefono":tel, "Equipo" : equipo, "Memoria" : memoria, "Alamacenamiento" : almacenamiento, "Problema" : problema, "Fecha_recibido": fecha ,"Estatus" : "En diagnostico"}
        db = Database()
        db.insertar(json, "Aparatos")
    
    def consultar(self, filtro=None):
        db = Database()
        return db.buscar("Aparatos", filtro, uno=False)
    
        
    def entregar (self, telefono, costo, fecha):
        filtro = {"Telefono": telefono}
        actualizacion = {
            "$set": {
                "Costo_total": costo,
                "fecha": fecha,
                "Estatus": "Entregado"
            }
        }
        db = Database()
        db.actualizar(filtro, actualizacion, "Aparatos")

    def diagnostico(self, tel, cliente, descripcion, solucion, costo, fecha, tecnico):
        filtro = {"Cliente": cliente, "Telefono": tel}
        actualizacion = {
            "$set": {
                "Descripcion": descripcion,
                "Solucion": solucion,
                "Costo": costo,
                "Fecha_diagnostico": fecha,
                "Tecnico": tecnico,
                "Estatus": "En reparacion"
            }
        }
        db = Database()
        db.actualizar(filtro, actualizacion, "Aparatos")

