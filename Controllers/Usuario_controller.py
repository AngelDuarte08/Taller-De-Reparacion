from flask import Blueprint, render_template, request, session, url_for, redirect

from Model.Usuarios import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route("/Registrar")
def registrar():
    return render_template("registrar.html")

@usuario_bp.route("/Registar Usuario", methods=["POST"])
def insertar_en_db():
    
    nombres = request.form["Nombre"]
    apellidos = request.form["Apellidos"]
    clave = request.form["Usuario"]
    psswd = request.form["Contrasena"]
    rol = request.form["Rol"]

    try:
        usuario = Usuario()
        usuario.registrar(nombres,
                        apellidos,
                        clave,
                        psswd,
                        rol)
    except:
        tipo = "error-mensaje"
        error = "No se puedo registar el usuario"
        return render_template("registrar.html", tipo=tipo, message= error)        
    
    finally:
        tipo = "success-mensaje"
        exito = "El usuario se registro con exito"
        return render_template("registrar.html", tipo=tipo ,message= exito)