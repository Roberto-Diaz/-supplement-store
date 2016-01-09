function letras(tecla){
  if( tecla.keyCode>=65 && tecla.keyCode<=90  || tecla.keyCode>=97 && tecla.keyCode<=122 || tecla.keyCode==32){
       return true;
   }else{
       return false
   }
}



function oculta(){
  var oculta = document.getElementById("registro");
  oculta.style.display="none";
  var oculta2 = document.getElementById("modificacion");
  oculta2.style.display="none";
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
