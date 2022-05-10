# my Crypto

## Descripción
SPA de consulta de la lista de últimos movimientos de compra/venta de criptos (LISTA MOVIMIENTOS), registro de nuevo movimiento (NUEVO MOVIMIENTO) y actualización del estado de su inversión (STATUS).

# Instrucciones para ejecutar la aplicación 

## Crear y activar un entorno virtual (opcional)

Copiar el fichero .env_template, renombrarlo a .env y elegir una de las opciones de FLASK_ENV (FLASK_ENV=development)

Crear el entorno virtual en la consola con el comando:

```
python -m venv venv
```
Activar el entorno virtual en la consola 
(comando alternativo para linux/mac: venv/bin/activate):

```
venv\Scripts\activate
```

## Instalar las dependencias
Fichero requirements - 
Para ello es necesario tener instalado pip.

Instalar con:

```
pip install -r requirements.txt
```

Con el comando pip freeze revisar que todas las librerías esten instaladas.

## Crear la base de datos con el nombre  my_crypto.db en la terminal
```
cd FLASK_JS
```
```
sqlite3 my_crypto.db
```
```
.read crea_tablas.sql
```

Para comprobar que la instalacion ha ido bien:
```
.tables
```
```
.schema
```
```
select count (*) from movimientos;  
```

Para salir:
```
.q
```

## Obtener un APIKEY
Puede obtener un APIKEY gratis en este link: 
https://www.coinapi.io/pricing?apikey

## Fichero .env
Copiar el fichero .env_template, renombrarlo a .env
Introducir el APIKEY en el campo indicado.

# START
En la terminal con el comando

```
flask run
```
Para salir 
```
CTRL + C
```


