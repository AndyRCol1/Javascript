const { resolve } = require('dns');
const { Observable } = require('rxjs');


const doSomething  = () => {
  return new Promise((resolve) => {
    resolve('valor 1');
});
}

const doSomething$ = () => {
  return new Observable(observer => {
    observer.next('valor 1 $');
    observer.next('valor 2 $');
    observer.next('valor 3 $');
    observer.next('valor 4 $');
    setTimeout(() => {
      observer.next('valor 5 $');
  },5000)
});
}

(async ()=> {
  const rta = await doSomething();
  console.log(rta) ;
} )();


(() => {
  const obs$ = doSomething$();
  obs$.subscribe(rta => {
    console.log(rta) ;
  })
})();
