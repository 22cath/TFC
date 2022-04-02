# Registro de transacciones de criptomonedas 
Aplicación web de consulta de inversiones y compra/venta de criptos,
para simular movimientos y ver si podemos hacer crecer nuestra inversión en euros o no. 
Esta aplicación tiene varias opciones:
- visualizar el listado de los últimos movimientos
- grabar nuevos movimientos con el botón MAS, 
- consultar valor actual (exchange rate) y verlo en la pantalla como PU precio unitario
- convertir con el boton CALCULAR un importe de la moneda x a la moneda y según el
    valor actual que indica la api de coinmarketcap
- si el usuario decide realizar la compra, pulsando el botón OK, 
    se graba el movimiento en el listado de movimientos
- para cada grabación de una compra/venta se actualiza el cálculo Estado de la inversión
- este apartado de Estado de la inversión se puede actualizar cuando quiere 
    (botón ACTUALIZAR)

# Instalar 

entorno virtual  
Fichero .env
Copiar el fichero .env_template, renombrarlo a .env y elegir una de las opciones de FLASK_ENV
Activar el entorno virtual con venv\Scripts\activate

fichero .config
Copiar el fichero .config_template, renombrarlo a .config

Fichero requirements
Para ello es necesario tener instalado pip.
Instalar con pip install -r requirement.txt
Con pip freeze revisa que todas las librerías instaladas.

# Base de datos
Crear una nueva vacía aqui con (crea_tablas.sql) - O bien haber entregado base de datos vacía como parte del repositorio

# START
En la terminal con el comando flask run
Para salir CTRL + C


