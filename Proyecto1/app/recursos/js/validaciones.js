function letras(tecla){
  if( tecla.keyCode>=65 && tecla.keyCode<=90  || tecla.keyCode>=97 && tecla.keyCode<=122 || tecla.keyCode==32){
       return true;
   }else{
       return false
   }
}


function email(tecla){
   
}


function ocultarRprove(){
  var oculta = document.getElementById("registroproveedor");
  oculta.style.display="none";
}

function ocultaventa(){
  var r = document.getElementById("registroventa");
  r.style.display="none";
}




function muestraventa(){
  var r = document.getElementById("registroventa");
  r.style.display="block";
}

function ocultarRSucursal(){
  var oculta = document.getElementById("registroSucursal");
  oculta.style.display="none";
}

function ocultapersonal(){
  var oculta = document.getElementById("registropersonal");
  oculta.style.display="none";
}

function ocultaproducto(){
  var oculta = document.getElementById("registroproducto");
  oculta.style.display="none";
}
function muestraproducto(){
  var oculta = document.getElementById("registroproducto");
  oculta.style.display="block";
}

function muestrapersonal(){
  var oculta = document.getElementById("registropersonal");
  oculta.style.display="block";
}

function muestraRSucursal(){
  var oculta = document.getElementById("registroSucursal");
  oculta.style.display="block";
}

function muestraRprove(){
  var oculta = document.getElementById("registroproveedor");
  oculta.style.display="block";
}

function oculta(){
  var oculta = document.getElementById("registro");
  oculta.style.display="none";
}

function ocultac(){
  var oculta = document.getElementById("divid");
  oculta.style.display="none";
}

function muestra2(){
  var mostrar2 = document.getElementById("modificacion");
  mostrar2.style.display="block";
}

function muestra(){
  var mostrar = document.getElementById("registro");
  mostrar.style.display="block";
}


function numeros(tecla){
    if(tecla.keyCode>="0".charCodeAt(0) && tecla.keyCode<="9".charCodeAt(0))
    {
        return true;
    }else
    {
        return false;
    }
}


function rola(tecla){
    if( tecla.keyCode>=65 && tecla.keyCode<=90  || tecla.keyCode>=97 && tecla.keyCode<=122 ||tecla.keyCode>="0".charCodeAt(0) && tecla.keyCode<="9".charCodeAt(0) || tecla.keyCode==32){
         return true;
     }else{
         return false
     }
}


var rola=1;

function validardecimal(tecla){
    if(rola==1){
        if(tecla.keyCode>=48 && tecla.keyCode<=57){
            return true;
        }else{
            if(tecla.keyCode==46){
                rola=0;
                return true;
            }else{
                return false;
            }
        }
    }
    if(rola==0){
        if(tecla.keyCode>=48 && tecla.keyCode<=57 ){
             rola=0;
                return true;
        }else{
            return false;
        }
    }
}


function contraseña(tecla){
    if( tecla.keyCode>=65 && tecla.keyCode<=90  || tecla.keyCode>=97 && tecla.keyCode<=122 ||tecla.keyCode>="0".charCodeAt(0) && tecla.keyCode<="9".charCodeAt(0) || tecla.keyCode==32){
         return true;
     }else{
         return false
     }
}
