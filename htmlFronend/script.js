// import data from './src/callback/challenge.js'

const uno = document.getElementById('1');
const dos = document.getElementById('2');
const rta = document.getElementById('rta');
console.log(data);

function calcular(){
    
    let a = +uno.getAttribute('value')
    console.log(a,'Andy')
    //console.log(uno.value)
    const rtas = +uno.value+ +dos.value;
    rta.innerText = "Resultado " + rtas;
    // let info = data;
    // console.log(data);
    // console.log(info);
}   

