from flask import Blueprint, render_template, request, session, url_for, redirect

from Model.Usuarios import Usuario
import pymongo.errors

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/")
def index():
    session["id_user"] = ""
    return render_template("index.html")


@auth_bp.route("/Inicio", methods=["POST"])
def login():
    userLogin = request.form['usuario']
    psswdLogin = request.form['contrasena']

    try:
        usuario = Usuario()
        resultadoDB = usuario.login(userLogin, psswdLogin)

        if resultadoDB == None:
            error = "Usuario o contraseña incorecta"
            return render_template("index.html", error=error)
        else:
            session["id_user"] = str(resultadoDB["_id"])
            return render_template("Menu.html")
    except pymongo.errors.ServerSelectionTimeoutError:
        error = "No se pudo conectar con la base de datos. Intenta más tarde."
        return render_template("index.html", error=error)

    except Exception as e:
        error = f"Ocurrió un error inesperado: {str(e)}"
        return render_template("index.html", error=error)


@auth_bp.route("/Menu")
def menu():
    return render_template("Menu.html")