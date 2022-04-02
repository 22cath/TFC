import sqlite3

DATABASE_NAME = "movimientos.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS movimientos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha VARCHAR(10) NOT NULL,
                hora VARCHAR(12) NOT NULL, 
                moneda_from VARCHAR(5) NOT NULL,
                cantidad_from DECIMAL NOT NULL,
				moneda_to VARCHAR(5) NOT NULL,
                cantidad_to DECIMAL NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


def insertar_movimiento(fecha, hora, moneda_from, cantidad_from, moneda_to, cantidad_to):
    db = get_db()
    cursor = db.cursor()
    statement = (
        "INSERT INTO movimientos(fecha, hora, moneda_from, cantidad_from,"
        "moneda_to, cantidad_to) VALUES (?, ?, ?, ?, ?, ?)"
    )
    cursor.execute(statement, [fecha, hora, moneda_from, cantidad_from, moneda_to, cantidad_to])
    db.commit()
    return True


def get_todos_movimientos():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM movimientos"
    cursor.execute(statement)
    return cursor.fetchall()


def actualiza_status(self, params):
    db = get_db()
    cursor = db.cursor()
    statement = ("""UPDATE status set invertido = ?, valor = ?""", params)
    cursor.execute(statement)
    return cursor.fetchall()
