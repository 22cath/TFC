// hardcodeamos los datos porque aun no tenemos implementada la 
// llamada a la API, ni siquiera tenemos base de datos

// Al mockear (mock es un tipo de harcoding que se utiliza en el 
// testeo de software )los datos

// cuando implementemos en el backend el metodo de movimientos en nuestra API,
// como el desarrollo del "pintado" de datos es INDEPENDIENTE a la API podremos
// integrar facilmente el resultado de llamar a movmientos, de tal manera que 
// se nos pintaría con los datos provenientes de la base de datos

const movimientos = [{
    fecha: '2022-01-01',
    hora: '23:45',
    tipo: 'ingreso',
    cantidad: '100',
    concepto: 'Pago de servicios'
},
{
    fecha: '2022-02-01',
    hora: '23:44',
    tipo: 'gasto',
    cantidad: '100',
    concepto: 'Compra de algo'
}
]

  //Hacer que pinte los movimientos en la tabla
// function httpGet(theUrl) {
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.open("GET", theUrl, false); // false for synchronous request
//     xmlHttp.send(null);
//     return xmlHttp.responseText;
// }
// url = "/api/v1/movimientos"
// httpGet(url)
