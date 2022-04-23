# my Crypto

## Descripción
SPA de consulta de la lista de últimos movimientos de compra/venta de criptos (LISTA MOVIMIENTOS), registro de nuevo movimiento (NUEVO MOVIMIENTO) y actualización del estado de su inversión (STATUS).

# Instrucciones para ejecutar la aplicación 

## Crear y activar un entorno virtual (opcional)
Fichero .env
Copiar el fichero .env_template, renombrarlo a .env y elegir una de las opciones de FLASK_ENV (FLASK_ENV=environment)

Crear el entorno virtual en la consola con el comando:

```
python -m venv venv
```
Activar el entorno virtual en la consola 
(comando alternativo para linux/mac: venv/bin/activate):

```
venv\Scripts\activate
```

Revisar fichero .env
    FLASK_APP=my_crypto
    FLASK_ENV=development
    API_KEY=620B201C-09FA-4757-9A9E-E7E431EAEF68

## Instalar las dependencias
Fichero requirements
Para ello es necesario tener instalado pip.
Instalar con:

```
pip install -r requirements.txt
```

Con pip freeze revisa que todas las librerías esten instaladas.

## Base de datos
Crear una nueva vacía aquí con (crea_tablas.sql) - O bien haber entregado base de datos vacía como parte del repositorio

Verificar en db.py
    DATABASE_NAME = "my_crypto.db"
Verificar en config.py
    DATABASE_NAME="my_crypto/movimientos.db"

## Obtener un APIKEY
Puede obtener un APIKEY gratis en este link: 
https://www.coinapi.io/pricing?apikey

## Fichero .config
Copiar el fichero .config_template, renombrarlo a .config
Introducir el APIKEY en el campo indicado.

# START
En la terminal con el comando

```
flask run
``
Para salir CTRL + C


