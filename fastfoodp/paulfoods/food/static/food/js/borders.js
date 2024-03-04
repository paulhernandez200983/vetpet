var bcart = document.querySelector('#bcart');
var btotal = document.querySelector('#btotal');






function addburger(bid){


  burgerid= '#burg'+bid;
  var name= document.querySelector(burgerid).innerHTML;
  var radio= 'burger'+bid;
  var pri = document.getElementsByName(radio);
  var size, price ;
  if(pri[0].checked){
   price=pri[0].value;
   size = 'M';

  }else{
     price=pri[1].value;
     size = 'L';
    

  }


var orders = JSON.parse(localStorage.getItem('orders'));
 total= localStorage.getItem('total');
var cartSize = orders.length;
orders[cartSize]= [name, size, price];
localStorage.setItem('orders', JSON.stringify(orders));


total=Number(total)+ Number(price);
localStorage.setItem('total',total);

var cart= document.querySelector("#cart");
cart.innerHTML=orders.length;

butto= '<button class="del btn-danger" onClick="removeBurger('+ cartSize+ ')">X</button>';
btotal.innerHTML= 'Total: ' + total + ' $';
bcart.innerHTML+='<li>'+name+ ' '+ size + ': '+ price+' $'+butto+'</li>';

}


function bshoppingcart(){
 var orders = JSON.parse(localStorage.getItem('orders'));
 var total = localStorage.getItem('total');
 var cartSize =orders.length;
 bcart.innerHTML= '';
 for(let i =0; i< cartSize; i++){
    butto= '<button class="del btn-danger" onClick="removeBurger('+ i+ ')">X</button>';
    bcart.innerHTML+='<li>'+ orders[i][0]+ ' '+ orders[i][1] + ': '+ orders[i][2]+' $'+butto+'</li>';
 }
 btotal.innerHTML= 'Total: ' + total + ' $';
}

bshoppingcart();


function removeBurger(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total)- Number(orders[n][2]);
    orders.splice(n,1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    bshoppingcart();
  }