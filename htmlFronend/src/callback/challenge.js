import { XMLHttpRequest } from 'xmlhttprequest';
const API ='http://localhost:3000/api/user/AndyRCol'

function fetchData(urlApi,callback){
    let xhttp=new XMLHttpRequest();xhttp.open('GET',urlApi,true);
    xhttp.onreadystatechange=function(event){
        if(xhttp.readyState===4){
            if(xhttp.status===200){
                callback(null,JSON.parse(xhttp.responseText));
                console.log('Success');
            }else{
                const error=new Error('Error'+urlApi);return callback(error,null);
            }
        }
    }
xhttp.send();
}
fetchData(`${API}/`,function(error1,data1){
        if(error1)return console.error(error1);
        console.log(data1)
        return data1
       // console.table(profile);    
    }
    );



