const peticionarioMovimientos = new XMLHttpRequest();
const peticionarioUpdate = new XMLHttpRequest();


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
        alert("Ups...Se ha producido un error al cargar los movimientos.");
    }
}
function pideMovimientosHttp() {    
    peticionarioMovimientos.open("GET", "api/v1/movimientos", true)
    peticionarioMovimientos.onload = listaMovimientos
    peticionarioMovimientos.send()  
}

pideMovimientosHttp()

/*  TODO revisar conexion html y js: nombre funcion en boton calcular de html?
        function calcular(){
            validarInputsBotonCalcular()
            calcular_tasa_cambio();
            validarSaldoSuficiente()
            calcular_cantidad_destino()
        }
    TODO revisar function validarInputsBotonCalcular() y comprobación saldo suficiente*/

function calcular_tasa_cambio() {
    var infoHTML = document.querySelector("#info");
    var from_moneda = document.getElementById("moneda_origen").value;
    var to_moneda = document.getElementById("moneda_destino").value;
    var cantidad_origen = document.getElementById("cantidad_origen").value;
    var cantidad_destino = document.getElementById("cantidad_destino").value;

    let url = "/api/v1/tipo_cambio/" + from_moneda + "/" + to_moneda + "/" + cantidad_origen;
    fetch(url).then((res) => { return res.json() }).then(data => {
        if (data["status"] == "success") {
            document.getElementById("tasa").value = data["data"]["tipo_cambio"];
            document.getElementById("cantidad_destino").value = 1/(1/data)*document.getElementById("moneda_origen").value;
        } 
        else { 
        alert ("Ups...Se ha producido un error en la consulta.");
        }
    });
}
   
function validarInputsBotonCalcular() {
    const $formulario = document.querySelector("#formulario"),
        $origen = document.querySelector("#moneda_origen"),
        $destino = document.querySelector("#moneda_destino"),
        $cantidad = document.querySelector("#cantidad_origen");

    $formulario.onsubmit = evento => {
        evento.preventDefault();

        const origen = $origen.value,
            destino = $destino.value,
            cantidad = $cantidad.value;
            //saldo = ["saldo"];
        if (
            origen === destino
        ){
            alert("Las monedas de origen y destino deben ser diferentes.");
            return;
        } 
        if (
            origen == "default" ||
            cantidad == "" ||
            destino == "default"
        ){
            alert("Por favor, rellene todos los campos señalados con un asterisco (*).");
            return;
        }
        if (
            cantidad < 0 ||
            cantidad != num ||
            cantidad == null
        ){
            alert("Introduzca un número VÁLIDO por favor.");
            return;
        }/*
        if (cantidad.value < ["saldo"]){
            alert ( f"No tiene suficiente saldo de {{from_moneda}}.");
            return;
        } */ 
        
        calcular_tasa_cambio();
        $formulario.submit();
    }
}

function resetearFormulario(){
    document.getElementById("moneda_origen").value = "default";
    document.getElementById("moneda_destino").value= "default";
    document.getElementById("cantidad_origen").value = "";
    document.getElementById("cantidad_destino").value= "";
}

function defineFecha(date) {
    return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
}
function defineHora(date) {
    return `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
}

function confirmar(ev){
    ev.preventDefault();

    const fecha = document.getElementById("fecha").value;
    const hora = document.getElementById("hora").value;
    const idMov = document.querySelector("#id").value;
    const from_moneda = document.getElementById("moneda_origen").value;
    const to_moneda = document.getElementById("moneda_destino").value;
    const cantidad_origen = document.getElementById("cantidad_origen").value;
    const cantidad_destino = document.getElementById("cantidad_destino").value;
    let currentDate = new Date();

    const movimiento = {
        //fecha: defineFecha(currentDate),
        //hora: defineHora(currentDate),
        
        fecha: fecha,
        hora : hora,
        idMov : id,
        origen:document.querySelector("#moneda_origen").value,
        importe: document.querySelector("#cantidad_origen").value,
        destino: document.querySelector("#moneda_origen").value,
        importe: document.querySelector("#cantidad_destino").value,
    };
    
    peticionarioUpdate.open("POST", `http:localhost:5000/api/v1/movimiento/${id}`, true);
    peticionarioUpdate.setRequestHeader("Content-Type", "application/json");
    peticionarioUpdate.onload = peticionarioUpdate;
    peticionarioUpdate.send(JSON.stringify(movimiento));
    resetearFormulario();
    };   


function cargaStatus() {
    //const section_status = document.querySelector(#status);
    //section_status.classList.remove("disable");

    const euro = document.querySelector("#eur_invertidos");
    const valor = document.querySelector("#valor_criptos_eur");
    const resultado = document.querySelector("#resultado");
   
    let url = "/api/v1/status";
    fetch(url).then((res) => { return res.JSONparse() }).then(data => {
        if (data["status"] == "success") {
            document.getElementById("eur_invertidos").value = data["data"]["eur_invertidos"];
            document.getElementById("valor_criptos_eur").value = data["data"]["valor_criptos_eur"];
            document.getElementById("resultado").value = data["data"]["valor_criptos_eur"] - data["data"]["eur_invertidos"];
            if (resultado < 0) {
                statusResultado.style.color = "red";
            }      
        } else {
            alert("Se ha producido un error. Inténtelo en unos instantes.");
        };
    });
}