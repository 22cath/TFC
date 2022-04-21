const peticionarioMovimientos = new XMLHttpRequest()
const requestAPI = new XMLHttpRequest()

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
*/
function calcular_tasa_cambio() {
    var infoHTML = document.querySelector("#info");
    var from_moneda = document.getElementById("moneda_origen").value;
    var to_moneda = document.getElementById("moneda_destino").value;
    var cantidad_origen = document.getElementById("cantidad_origen").value;

    let url = "/api/v1/tipo_cambio/" + from_moneda + "/" + to_moneda + "/" + cantidad_origen;
    fetch(url).then((res) => { return res.json() }).then(data => {
        if (data["status"] == "success") {
            document.getElementById("tasa").value = data["data"]["tipo_cambio"];

        } // TODO: else error


    });


}
