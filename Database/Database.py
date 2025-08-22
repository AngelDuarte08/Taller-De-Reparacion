#Librerias
from pymongo import MongoClient, errors

class Database():
    def __init__(self):
        self.__uri = "mongodb://SML:200235SML@31.97.102.106:27017/DiegoTech"
        try:
            self.__cliente = MongoClient(self.__uri, serverSelectionTimeoutMS=5000)
            # Probar conexión
            self.__cliente.admin.command("ping")
            print("Conectado a MongoDB")
            self.__db = self.__cliente['DiegoTech']
        except errors.ServerSelectionTimeoutError as e:
            print("No se pudo conectar a MongoDB:", e)
            self.__db = None
        #Coleccion
        self.__collection = None

    def insertar(self, documento, collection):
        self.__collection = self.__db[collection]
        resultado = self.__collection.insert_one(documento)
        print("Se realizo con exito la insercion de datos")
        
    def buscar(self, documento, collection):
        self.__collection = self.__db[collection]
        resultado = self.__collection.find_one(documento)
        if resultado:
            print("consulta exitosa")
            return resultado
        else:
            print("no se encontró ningún documento")
            return None

    def actualizar(self, docuemto, collection):
        self.__collection = self.__db[collection]
        self.__collection.update_one(docuemto)
        print("Los datos se atualizaron correctamente")