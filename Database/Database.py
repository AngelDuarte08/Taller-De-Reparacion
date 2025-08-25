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
        
    def buscar(self, collection, filtro=None, uno=False):
        self.__collection = self.__db[collection]

        if filtro is None:
            filtro = {}

        if uno:
            # Devuelve solo un documento
            resultado = self.__collection.find_one(filtro)
            if resultado:
                print("Consulta exitosa (un documento)")
                return resultado
            else:
                print("No se encontró ningún documento")
                return None
        else:
            # Devuelve todos los documentos como lista
            resultados = list(self.__collection.find(filtro))
            if resultados:
                print("Consulta exitosa (varios documentos)")
                return resultados
            else:
                print("No se encontraron documentos")
                return []


    def actualizar(self, filtro, actualizacion, collection):
        self.__collection = self.__db[collection]
        resultado = self.__collection.update_one(filtro, actualizacion)
        print("Los datos se actualizaron correctamente")
        print("Matched:", resultado.matched_count, "Modified:", resultado.modified_count)
