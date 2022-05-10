CREATE TABLE IF NOT EXISTS movimientos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha VARCHAR(10) NOT NULL,
    hora VARCHAR(12) NOT NULL, 
    from_moneda VARCHAR(5) NOT NULL,
    from_cantidad DECIMAL NOT NULL,
    to_moneda VARCHAR(5) NOT NULL,
    to_cantidad DECIMAL NOT NULL
)

