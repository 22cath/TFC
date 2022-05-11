import traceback
import os
import urllib.request
import json

from flask import render_template
from flask import jsonify
from flask import abort
from flask import request
from sqlite3 import Error

from my_crypto.db import create_tables
from my_crypto.db import insertar_movimiento
from my_crypto.db import get_todos_movimientos

# from my_crypto.db import get_movimiento_by_id
from my_crypto.db import get_saldo
from my_crypto.db import ultimo_id
from my_crypto.db import total_euros_invertidos
from my_crypto.db import total_euros_comprados
from my_crypto import app
from flask import Flask
#from flask_cors import CORS


#CORS(app, resources={r'/api/*': {'origins': '*'} }, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'OPTIONS'])
#cors.header('Access-Control-Allow-Origin: *')
#cors.header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS')
#cors.header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token')

#database_name = app.config.get("DATABASE_NAME")

@app.route("/")
def init():
    # return "Estoy funcionando"

    return render_template("index.html")


@app.route("/api/v1/movimientos", methods=["GET"])
def movimientos():
    try:
        movimientos = get_todos_movimientos()
    except Error:
        return (
            jsonify(
                {
                    "status": "fail",
                    "mensaje": "Ha habido un problema en la conexión a la base de datos",
                }
            ),
            400,
        )
    json_response = {"status": "success", "data": [dict(row) for row in movimientos]}
    return jsonify(json_response)


# @app.route("/api/v1/movimiento/<id_>", methods=["GET"])
# def movimiento(id_):
#     movimiento = get_movimiento_by_id(id_)
#     json_response = {"status": "success", "data": [dict(row) for row in movimiento]}
#     if len(movimiento) == 0:
#         abort(400)
#     return jsonify(json_response)

@app.route("/api/v1/tipo_cambio/<from_moneda>/<to_moneda>/<from_cantidad>", methods=["GET"])
def tasa_cambio(from_moneda, to_moneda, from_cantidad):
    api_key = os.environ["API_KEY"]
    api_url = f"https://rest.coinapi.io/v1/exchangerate/{from_moneda}/{to_moneda}?apikey={api_key}"

    try:
        response = urllib.request.urlopen(api_url)
    except BaseException:
        error_api_response = {
            "status": "fail",
            "mensaje": f"Se ha producido un error en la consulta a coinApi.io",
        }
        return jsonify(error_api_response), 400

    json_response = json.loads(response.read().decode("utf-8"))
    rate = json_response["rate"]
    json_response = {"status": "success", "data": {"tipo_cambio": rate}}
    no_saldo_response = {
        "status": "fail",
        "mensaje": f"No tiene suficiente saldo de {from_moneda}",
    }
    try:
        if from_moneda != "EUR" and get_saldo(from_moneda) < float(from_cantidad):
            return jsonify(no_saldo_response), 400
        else:
            return jsonify(json_response)
    except Error:
        return (
            jsonify(
                {
                    "status": "fail",
                    "mensaje": "Ha habido un problema en la conexión a la base de datos",
                }
            ),
            400,
        )



@app.route("/api/v1/movimiento", methods=["POST"])
def grabar_movimiento():
    nuevo_movimiento = request.get_json()
    json_response = {}
    from_moneda = nuevo_movimiento["from_moneda"]
    to_moneda = nuevo_movimiento["to_moneda"]
    ok = False
    id_ = -1

    if from_moneda == to_moneda:
        json_response = {
            "status": "fail",
            "mensaje": "Las monedas deben ser diferentes.",
        }
        return jsonify(json_response), 400
    try:
        if from_moneda != "EUR":
            saldo = get_saldo(from_moneda)
            if saldo is None:
                saldo = 0.0
            if float(nuevo_movimiento["from_cantidad"]) <= saldo:
                ok = insertar_movimiento(**nuevo_movimiento)
            else:
                json_response = {"status": "fail", "mensaje": "Saldo insuficiente"}
        else:  # EUR
            ok = insertar_movimiento(**nuevo_movimiento)

        if ok:
            id_ = ultimo_id()
            json_response = {
                "status": "success",
                "id": id_,
                "monedas": [from_moneda, to_moneda],
            }
            return jsonify(json_response), 201
        else:
            return jsonify(json_response), 200
    # Esta es la excepción padre, cuidado! captura todos los errores
    except BaseException as e:
        traceback.print_exc()
        return (
            jsonify(
                {
                    "status": "fail",
                    "mensaje": "Ha ocurrido un error.",
                }
            ),
            400,
        )


def valor_actual_criptos():
    monedas = {"BTC", "ETH", "BCH", "BNB", "LINK", "LUNA", "ATOM", "SOL", "USDT"}
    api_key = os.environ["API_KEY"]
    api_url = f"https://rest.coinapi.io/v1/exchangerate/EUR/?apikey={api_key}"
    response = urllib.request.urlopen(api_url)
    json_response = json.loads(response.read().decode("utf-8"))
    

    total = 0.0
    for rate in json_response["rates"]:
        if rate["asset_id_quote"] in monedas:
            saldo = get_saldo(rate["asset_id_quote"])
            if saldo is None:
                saldo = 0.0
            # print(rate["asset_id_quote"], saldo, (1 / rate["rate"]) * saldo)
            total += (1 / rate["rate"]) * saldo
    return total


@app.route("/api/v1/status", methods=["GET"])
def status():
    try:

        res = {"status": "success", "data": {"invertido": None, "valor_actual": None}}

        res["data"]["invertido"] = total_euros_invertidos()
        res["data"]["valor_actual"] = valor_actual_criptos() + total_euros_comprados()
        return jsonify(res)
    except BaseException as e:
        traceback.print_exc()
        error_api_response = {
            "status": "fail",
            "mensaje": f"Se ha producido un error en el cálculo del status.",
        }
        return jsonify(error_api_response), 400


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify({"status": "fail", "mensaje": "Mensaje de error"}), 400


