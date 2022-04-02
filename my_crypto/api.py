from crypt import methods
from flask import render_template, request, jsonify
import sqlite3
from my_crypto.db import create_tables
from my_crypto.db import insertar_movimiento
from my_crypto.db import actualiza_status
from my_crypto.db import get_todos_movimientos

from my_crypto import app

# ruta_db = app.config['movimientos.db']

@app.route("/")
def init():
    # return "Estoy funcionando"
    return render_template("index.html")

@app.route("/api/v1/movimientos", methods=["GET"])
def movimientos():
    movimientos = get_todos_movimientos()
    return jsonify(movimientos)

@app.route("/api/v1/movimiento", methods=["GET", "POST"])
def nuevo_movimiento():
    form = NuevoMovimientoForm()
    if request.method == "GET":
            return render_template("nuevo_movimiento.html", formulario=form)
    else:
        #validar antes de dar opcion de confirmacion definitiva
        if form.validate():
            # si moneda_from != EUR entonces validar que hay suficiente saldo de cripto antes de la compra
            # falta añadir un wallet con esta info en la misma página?
            # fecha & hora = reloj del ordenador
            moneda_from = str(form.moneda_from.data)
            cantidad_from > saldo_moneda_from.data
            moneda_to = str(form.moneda_to.data)
            # consultar exchange rate desde servidor
            # calcular importe resultante cantidad_to
            # grabar en el form para confirmacion del usuario
            try:
                nuevo_movimiento = insertar_movimiento()
                return jsonify({
                    "status": "success"                  
                    }), 201
            except sqlite3.Error as e:
                return jsonify({ "status": "fail",
                    "message": f"Saldo insuficiente en esta moneda. Prueba con otra por favor.: {e}"
                    }), 200
        else:
            if form.validate():
                try:
                    nuevo_movimiento = insertar_movimiento()
                    return jsonify({
                        "status": "success"                  
                        }), 201
                except sqlite3.Error as e:
                    return jsonify({ "status": "fail",
                        "message": f"Se ha producido un error. Inténtelo en unos instantes.: {e}"
                        }), 400
            return render_template("nuevo_formulario.html", formulario=form, id=id)

@app.route("/api/v1/status", methods=["UPDATE"])
def status():
    status = actualiza_status()
    datos = request.json
    try:
        datos = actualiza_status()
        return jsonify({
            "status": "success",
            "data":actualiza_status(datos['invertido'], datos['valor'])
            }), 200
    except sqlite3.Error as e:
        return jsonify({ 
            "status": "fail",
            "message": f"Se ha producido un error. Inténtelo en unos instantes. {e}"
        }), 400

@app.route("/api/v1/tasa_conversion/<origen>/<destino>/<cantidad>",  methods=["GET"])
def tasa_cambio(origen, destino, cantidad):
    #request.get(..)
    #return jsonify({
    #   "status": "success",
    #   "valor_cambio":})