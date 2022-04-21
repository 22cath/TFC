# from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY
from datetime import date
from datetime import datetime
import sqlite3

from flask import request
from config import URL_TASA_ESPECIFICA
# from criptos.errors import APIError, CONNECT_ERROR

DATABASE_NAME = "my_crypto.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS movimientos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha VARCHAR(10) NOT NULL,
                hora VARCHAR(12) NOT NULL, 
                from_moneda VARCHAR(5) NOT NULL,
                from_cantidad DECIMAL NOT NULL,
				to_moneda VARCHAR(5) NOT NULL,
                to_cantidad DECIMAL NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


def ultimo_id():
    db = get_db()
    cursor = db.cursor()
    # statement = """SELECT last_insert_rowid() AS "id" """

    statement = """SELECT seq AS "id" FROM sqlite_sequence WHERE name="movimientos" """
    cursor.execute(statement)
    return cursor.fetchone()["id"]


def insertar_movimiento(from_moneda, from_cantidad, to_moneda, to_cantidad):
    db = get_db()
    cursor = db.cursor()
    fecha = date.today()
    hora = datetime.now().strftime("%H:%M:%S.%f")[:-3]

    statement = (
        "INSERT INTO movimientos(fecha, hora, from_moneda, from_cantidad,"
        "to_moneda, to_cantidad) VALUES (?, ?, ?, ?, ?, ?)"
    )
    cursor.execute(statement, [fecha, hora, from_moneda, from_cantidad, to_moneda, to_cantidad])
    db.commit()
    return True


def get_todos_movimientos():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM movimientos"
    cursor.execute(statement)
    return cursor.fetchall()


def get_movimiento_by_id(id_):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM movimientos WHERE id = ?"
    cursor.execute(statement, [id_])
    return cursor.fetchall()


def get_saldo(moneda):
    """El saldo de una sola moneda"""
    db = get_db()
    cursor = db.cursor()
    statement1 = """SELECT Sum(from_cantidad) * ( -1 ) AS "Saldo"
        FROM   movimientos
        WHERE  from_moneda = ? """

    statement2 = """SELECT Sum(to_cantidad) AS "Saldo"
        FROM   movimientos
        WHERE  to_moneda = ? """

    statement = f"""SELECT Sum(saldo) As saldo
        FROM   ({statement1} UNION {statement2}) AS "C"; """

    cursor.execute(statement, [moneda, moneda])
    return cursor.fetchone()["saldo"]

def total_euros_invertidos():
    db = get_db()
    cursor = db.cursor()
    statement = """SELECT sum(from_cantidad) AS "total_invertido" FROM movimientos WHERE from_moneda = "EUR" """
    cursor.execute(statement)
    return cursor.fetchone()["total_invertido"]


def total_euros_comprados():
    db = get_db()
    cursor = db.cursor()
    statement = (
        """SELECT sum(to_cantidad) AS "total_comprado" FROM movimientos WHERE to_moneda = "EUR" """
    )
    cursor.execute(statement)
    return cursor.fetchone()["total_comprado"]



def actualiza_status(self, params):
    db = get_db()
    cursor = db.cursor()
    statement = ("""UPDATE status set invertido = ?, valor = ?""", params)
    cursor.execute(statement)
    return cursor.fetchall()

""""
class CriptoValorModel:
    def __init__(self, apikey, origen = "", destino = ""):
        self.apikey = apikey
        self.origen = origen
        self.destino = destino

        self.tasa = 0.0

    def obtener_tasa(self, time=""):
        try:
            respuesta = request.get((URL_TASA_ESPECIFICA.format),
                self.origen,
                self.destino,
                self.apikey
            )
        except:
            raise APIError(CONNECT_ERROR)            

        if respuesta.status_code != 200:
            #raise APIError(respuesta.status_code, respuesta.json()["error"])
            raise APIError(respuesta.status_code)

        self.tasa = round(respuesta.json()["rate"], 6)
"""