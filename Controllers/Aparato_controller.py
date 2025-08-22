from flask import Blueprint, render_template, request, session, url_for, redirect

from Model.Aparato import Aparato

aparato_bp = Blueprint('aparato_bp', __name__)

@aparato_bp.route("/Recepcion")
def recepcion():
    return render_template("/recepcion.html")


@aparato_bp.route("/Diagnostico")
def diagnostico():
    return render_template("diagnostico.html")


@aparato_bp.route("/Entrega")
def entrega():
    return render_template("entrega.html")

@aparato_bp.route("/Estatus")
def estatus():
    return render_template("estatus.html")

@aparato_bp.route("/Insertar_recepcion", methods=["POST"])
def insertar_recepcion():

    cliente = request.form["Cliente"]
    telefono = request.form["tel"]
    equipo = request.form["Equipo"]
    memoria = request.form["Memoria"]
    almacenamiento = request.form["Almacenamiento"]
    problema = request.form["Problema"]
    fecha = request.form["Fecha"]

    try: 
        aparato = Aparato()
        aparato.recibir(cliente, 
                        telefono,
                        equipo,
                        memoria, 
                        almacenamiento, 
                        problema, 
                        fecha)
    except:
        tipo = "error-mensaje"
        error = "Hubo un problema al tratar de registar el equipo"
        return render_template("recepcion.html", tipo=tipo, message= error)        
    
    finally:
        tipo = "success-mensaje"
        exito = "El equipo se registro de manera correcta puede seguir"
        return render_template("recepcion.html", tipo=tipo ,message= exito)
