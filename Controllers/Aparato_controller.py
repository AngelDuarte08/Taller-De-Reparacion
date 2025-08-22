from flask import Blueprint, render_template, request, session, url_for, redirect

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