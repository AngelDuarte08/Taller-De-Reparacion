from flask import Blueprint, render_template, request, session, url_for, redirect

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route("/Registrar")
def registrar():
    return render_template("registrar.html")