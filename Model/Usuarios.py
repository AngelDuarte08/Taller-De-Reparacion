from Database.Database import Database
class Usuario():
    def __init__(self):
        idUser = ""
        clave = ""
        psswd = ""
        usuario = ""
        rol = ""

    def login(self, user, psswd):
        documento = {"clave": user, "psswd": psswd}
        db = Database()
        resultaDB = db.buscar(documento, "Usuarios")
        return resultaDB

    
    def agregar():
        pass

    def consultar():
        pass

    def eliminar():
        pass