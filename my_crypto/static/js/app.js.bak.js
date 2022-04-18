
// https://stackoverflow.com/questions/35549547/fetch-api-vs-xmlhttprequest
// https://hacks.mozilla.org/2015/03/this-api-is-so-fetching/
const peticionarioMovimientos = new XMLHttpRequest();
const requestAPI = new XMLHttpRequest();
// let movimientos;


function listaMovimientos() {
    const campos = ['fecha', 'hora', 'from_moneda', 'from_cantidad', 'to_moneda', 'to_cantidad']; 
    let url = 'http://127.0.0.1:5000/api/v1/movimientos';
    // var movimientos; 
    // https://stackoverflow.com/questions/45018338/javascript-fetch-api-how-to-save-output-to-variable-as-an-object-not-the-prom
    /*fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(res => res.json())
    .then(data => obj = data)
    .then(() => console.log(obj))*/

    /*

.then((response) => {
return response.json()
})
.then((albums) => {
albums.forEach(function (elem) {
tpl += '<a href="' + elem.url + '">'
+ '<img src="' + elem.thumbnailUrl + '"/>',
+ '</a>',
+ '<br/>',
+ '<span>' + elem.title + '</span>';
});
respuestaHTML.innerHTML = tpl;
});

    */
    // TODO: check status == success
    fetch(url).then((res) =>{return  res.json()})
    .then((movimientos) =>{movimientos["data"].forEach(function (elem){
        console.log("Un movimeinto");
        console.log(elem["from_moneda"]);
    }) });
    
    // this.readyState === 4 &&
    /*if (this.status === 200 ) {
        movimientos = JSON.parse(this.responseText);
       
        const tbody = document.querySelector("#tbbody-movimientos");
        tbody.innerHTML = "";

        for (let i = 0; i < movimientos.length; i++) {
            const fila = document.createElement('tr');

            const movimiento = movimientos[i];
            
            for (const campo of campos) {
                const celda = document.createElement('td');
                celda.innerHTML = movimiento[campo];
                fila.appendChild(celda);
            }
            tbody.appendChild(fila);
        }
    }*/ 
}


/*
// qué hago con la fecha + infoTasa devuelve un string - puedo calcular con ello?
function infoTasaEspecifica(){

    var infoHTML = document.querySelector("#info");
    var tasa = "";
    var asset_id_base = getElementById ('moneda_origen');
    var asset_id_quote = getElementById ('moneda_destino');

    fetch("https://rest.coinapi_.io/v1/exchangerate/{asset_id_base}/{asset_id_quote}?time{time}apikey={}")
        .then(response => respuesta.json())
        .then(respuestaDescodificada => {
             const tasa = respuestaDescodificada.rate;
             const fecha = respuestaDescodificada.time;
             $info.textContent = tasa;
             tasa =parseFloat(tasa,10);
             tasa = round(respuesta.json()["rate"], 6);
        })
        infoHTML.innerHTML = tasa;
}

//function cantidadDestino()





// function httpGet(theUrl) {
    //     var xmlHttp = new XMLHttpRequest();
    //     xmlHttp.open("GET", theUrl, false); // false for synchronous request
    //     xmlHttp.send(null);
    //     return xmlHttp.responseText;
    // }
    // url = "/api/v1/movimientos"
    // httpGet(url) }
//

*/

/*
var _table_ = document.createElement('table'),
    _tr_ = document.createElement('tr'),
    _th_ = document.createElement('th'),
    _td_ = document.createElement('td');


 function buildHtmlTable(arr) {
     var table = _table_.cloneNode(false),
         columns = addAllColumnHeaders(arr, table);
     for (var i=0, maxi=arr.length; i < maxi; ++i) {
         var tr = _tr_.cloneNode(false);
         for (var j=0, maxj=columns.length; j < maxj ; ++j) {
             var td = _td_.cloneNode(false);
                 cellValue = arr[i][columns[j]];
             td.appendChild(document.createTextNode(arr[i][columns[j]] || ''));
             tr.appendChild(td);
         }
         table.appendChild(tr);
     }
     return table;
 }
 
 // Adds a header row to the table and returns the set of columns.
 // Need to do union of keys from all records as some records may not contain
 // all records
 function addAllColumnHeaders(arr, table)
 {
     var columnSet = [],
         tr = _tr_.cloneNode(false);
     for (var i=0, l=arr.length; i < l; i++) {
         for (var key in arr[i]) {
             if (arr[i].hasOwnProperty(key) && columnSet.indexOf(key)===-1) {
                 columnSet.push(key);
                 var th = _th_.cloneNode(false);
                 th.appendChild(document.createTextNode(key));
                 tr.appendChild(th);
             }
         }
     }
     table.appendChild(tr);
     return columnSet;
 }

*/
/*document.body.appendChild(buildHtmlTable([
    {"name" : "abc", "age" : 50},
    {"age" : "25", "hobby" : "swimming"},
    {"name" : "xyz", "hobby" : "programming"}
]));*/