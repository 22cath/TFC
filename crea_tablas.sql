CREATE TABLE IF NOT EXISTS "movimientos"(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL, 
    moneda_from TEXT NOT NULL,
    cantidad_from REAL NOT NULL,
    moneda_to TEXT NOT NULL,
    cantidad_to REAL NOT NULL
)


/*CREATE TABLE IF NOT EXISTS "movimientos"(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha VARCHAR(10) NOT NULL,
    hora VARCHAR(12) NOT NULL, 
    moneda_from VARCHAR(5) NOT NULL,
    cantidad_from DECIMAL NOT NULL,
    moneda_to VARCHAR(5) NOT NULL,
    cantidad_to DECIMAL NOT NULL
    */