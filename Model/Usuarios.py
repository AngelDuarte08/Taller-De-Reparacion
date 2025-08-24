from Database.Database import Database
class Usuario():
    def __init__(self):
        self.__db = Database()
        self.__collection = "Usuarios"
        self.__idUser = ""
        self.__clave = ""
        self.__psswd = ""
        self.__usuario = ""
        self.__rol = ""

    def login(self, user, psswd):
        documento = {"Usuario": user, "Contrasena": psswd}
        resultaDB = self.__db.buscar(self.__collection, documento, uno=True)
        return resultaDB

    
    def registrar(self, nombres, apellidos, clave, psswd, rol):
        documento = {"Nombre":nombres, "Apellidos":apellidos, "Usuario": clave, "Contrasena":psswd, "Rol": rol}
        self.__db.insertar(documento, self.__collection) 
        

    def consultar():
        pass

    def eliminar():
        pass