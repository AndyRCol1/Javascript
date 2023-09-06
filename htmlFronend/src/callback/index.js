function sum(a,b){
    return c = a + b;
}

function mult(a,b){
    return c = a * b;
}

function rest(a,b){
    return c = a - b;
}

function div(a,b){
    return c = a / b;
}

function Calc(a, b, cb){
    return cb(a,b);
}

let a = 1
let b = 2
console.log("Suma",Calc(a,b,sum));
console.log("resta",Calc(a,b,rest));
console.log("Multiplicación",Calc(a,b,mult));
console.log("división",Calc(a,b,div));

setTimeout(function(){
    console.log("Hola JavaScript");
},2000);

function saludo(name){
    console.log("Hola " + name);
}

setTimeout(saludo,2000,"AndyRCol");