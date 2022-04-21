import traceback
import os
import urllib.request
import json

from flask import render_template
from flask import jsonify
from flask import abort
from flask import request

from my_crypto.db import create_tables
from my_crypto.db import insertar_movimiento
from my_crypto.db import get_todos_movimientos

# from my_crypto.db import get_movimiento_by_id
from my_crypto.db import get_saldo
from my_crypto.db import ultimo_id
from my_crypto.db import total_euros_invertidos
from my_crypto.db import total_euros_comprados
from my_crypto.db import actualiza_status
from my_crypto import app


@app.route("/")
def init():
    # return "Estoy funcionando"

    return render_template("index.html")


@app.route("/api/v1/movimientos", methods=["GET"])
def movimientos():
    movimientos = get_todos_movimientos()
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
    rate = round(json_response["rate"], 6)
    json_response = {"status": "success", "data": {"tipo_cambio": rate}}
    no_saldo_response = {
        "status": "fail",
        "mensaje": f"No tienes suficiente saldo de {from_moneda}",
    }
    print(from_moneda, from_cantidad, "Saldo", get_saldo(from_moneda))
    if float(from_cantidad) > get_saldo(from_moneda):
        return jsonify(no_saldo_response), 400
    else:
        return jsonify(json_response)


@app.route("/api/v1/movimiento", methods=["POST"])
def grabar_movimiento():
    nuevo_movimiento = request.get_json()
    json_response = {}
    from_moneda = nuevo_movimiento["from_moneda"]
    to_moneda = nuevo_movimiento["to_moneda"]
    ok = False
    id_ = -1

    if from_moneda == to_moneda:
        return (
            jsonify(
                {
                    "status": "fail",
                    "message": "Las monedas deben ser diferentes.",
                }
            ),
            400,
        )
    try:
        if from_moneda != "EUR":
            saldo = get_saldo(from_moneda)
            if saldo is None:
                saldo = 0.0
            if nuevo_movimiento["from_cantidad"] <= saldo:
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
            return (jsonify(json_response), 201)
        else:
            return (jsonify(json_response), 200)
    # Esta es la excepción padre, cuidado! captura todos los errores
    except BaseException as e:
        traceback.print_exc()
        return (
            jsonify(
                {
                    "status": "fail",
                    "message": "Ha ocurrido un error.",
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
    # import json

    # with open("my_crypto/rates.json") as f:
    #     json_response = json.load(f)

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
    res = {"status": "success", "data": {"invertido": None, "valor_actual": None}}
    res["data"]["invertido"] = total_euros_invertidos()
    saldo_euros = total_euros_comprados() - res["data"]["invertido"]
    # print(saldo_euros, total_euros_comprados(), valor_actual_criptos())
    res["data"]["valor_actual"] = valor_actual_criptos() + saldo_euros
    return jsonify(res)

"""
#def status():
#    datos = request.json
#    try:
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
"""


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify({"status": "fail", "mensaje": "Mensaje de error"}), 400
