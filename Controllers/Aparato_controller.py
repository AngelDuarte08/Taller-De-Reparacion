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
    try:
        aparato = Aparato()
        resultadoDB = aparato.consultar()
        return render_template("estatus.html", estatus_list= resultadoDB)
    except:
        pass

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

@aparato_bp.route("/Insertar_diagnostico", methods=["POST"])
def insertar_diagnostico():

    telefono = request.form["tel"]
    cliente = request.form["cliente"]
    descripcion = request.form["descripcion"]
    solucion = request.form["solucion"]
    costo = request.form["costo"]
    fecha = request.form["fecha"]
    tecnico = request.form["usuario"]

    try: 
        aparato = Aparato()
        aparato.diagnostico(telefono, cliente, descripcion, solucion, costo, fecha, tecnico)
    
    except:
        tipo = "error-mensaje"
        error = "El diagnostico no se puede registar"
        return render_template("diagnostico.html", tipo=tipo, message=error)
    
    finally:
        tipo = "success-mensaje"
        exito = "El diagnistico se guardo correctamente"
        return render_template("diagnostico.html", tipo=tipo, message=exito )
    
@aparato_bp.route("/insertar_entrega", methods=["POST"])
def insertar_enterga():

    telefono = request.form["tel"]
    costo = request.form["Costo"]
    fecha = request.form["Fecha"]

    try: 
        aparato = Aparato()
        aparato.entregar(telefono, costo, fecha)

    except:
        tipo = "error-mensaje"
        error = "No se puede regristrar la entega"
        return render_template("entrega.html", tipo=tipo, message=error)
    
    finally:
        tipo = "success-mensaje"
        exito = "El registro de la entrega correcto, puede entregar el equipo"
        return render_template("entrega.html", tipo=tipo, message=exito )
    
@aparato_bp.route("/Buscar_estatus" , methods=["POST"])
def buscar_estatus():

    tel = request.form["tel"]
    filtro = {"Telefono": tel}

    if not tel:
        return redirect(url_for("aparato_bp.estatus"))
    else: 
        try: 
            aparato = Aparato()
            resultadoDB = aparato.consultar(filtro)

            return render_template("estatus.html", estatus_list= resultadoDB)            

        except:
            tipo = "error-mensaje"
            error = "Cliente no encontrado"
            return render_template("estatus.html", tipo=tipo, message= error)