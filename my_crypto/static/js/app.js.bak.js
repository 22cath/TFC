
// https://stackoverflow.com/questions/35549547/fetch-api-vs-xmlhttprequest
// https://hacks.mozilla.org/2015/03/this-api-is-so-fetching/
// https://stackoverflow.com/questions/45018338/javascript-fetch-api-how-to-save-output-to-variable-as-an-object-not-the-prom

// asignaciones en features funcionales de javascrip vanilla js 
/*fetch('https://jsonplaceholder.typicode.com/posts/1')
.then(res => res.json())
.then(data => obj = data)
.then(() => console.log(obj))*/

/* XMLhttpREquest - ejemplo
const peticionarioMovimientos = new XMLHttpRequest()
const requestAPI = new XMLHttpRequest()

function errorMessage(response, error) {
    const errorMessageDiv = document.querySelector("#error-message");
    const errorHTML = `<p>${error}: ${response.message}</p>`;
    errorMessageDiv.innerHTML = errorHTML;
}

/*function errorMessageForm(message) {
    const errorMessageDiv = document.querySelector("#mensaje_error");
    const errorHTML = `<p>${message}</p>`;
    errorMessageDiv.innerHTML = errorHTML;
} */


/*const listaMonedas = [
    "EUR",
    "BTC",
    "ETH",
    "BCH",
    "BNB",
    "LINK",
    "LUNA",
    "ATOM",
    "USDT",
];

function listaMovimientos() {
    const campos = ['fecha', 'hora', 'from_moneda', 'from_cantidad', 'to_moneda', 'to_cantidad']; 
    
    if (this.readyState === 4 && this.status === 200) {
        // traduce el texto recibido en un objeto de js con JSON.parse
        const movimientos = JSON.parse(this.responseText)

        const tbody = document.querySelector("#tbbody-movimientos")

        //tbody.innerHTML = ""

        for (let i = 0; i < movimientos.data.length; i++) {
            const fila = document.createElement('tr')
            const movimiento = movimientos.data[i]
            
            for (const campo of campos) {
                const celda = document.createElement('td')
                celda.innerHTML = movimiento[campo]
                fila.appendChild(celda)
            }
            tbody.appendChild(fila)
        }
    } else {
        alert("Ups...Se ha producido un error al cargar los movimientos.")
    }
}
function pideMovimientosHttp() {    
    peticionarioMovimientos.open("GET", "api/v1/movimientos", true)
    peticionarioMovimientos.onload = listaMovimientos
    peticionarioMovimientos.send()  
    }

pideMovimientosHttp()
*/
/*
function listaMovimientos() {
    const campos = ['fecha', 'hora', 'from_moneda', 'from_cantidad', 'to_moneda', 'to_cantidad'];
    let url = 'api/v1/movimientos';
    fetch(url).then((res) => { return res.json() })
        .then((movimientos) => {
            if (movimientos["status"] == "success") {
                movimientos["data"].forEach(function (movimiento) {
                    const tbody = document.querySelector("#tbbody-movimientos");
                    const fila = document.createElement('tr');
                    for (const campo of campos) {
                        const celda = document.createElement('td');
                        celda.innerHTML = movimiento[campo];
                        fila.appendChild(celda);
                    }
                    tbody.appendChild(fila);
                })
            } 
        //else {
        //    alert("Ups...Se ha producido un error al cargar los movimientos.");
        //}
        });
}
/*
function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
    }
    url = "/api/v1/movimientos"
    httpGet(url) 
}
*/

// VALIDACION FORMULARIO
// https://parzibyte.me/blog/2021/04/12/validar-formularios-javascript/