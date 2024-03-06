var zcart = document.querySelector('#zcart');
var ztotal = document.querySelector('#ztotal');

function addpizza(zid){


    pizzaid= '#pizz'+zid;
    var name= document.querySelector(pizzaid).innerHTML;
    var radio= 'pizza'+zid;
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
  
  butto= '<button class="del btn-danger" onClick="removePizza('+ cartSize+ ')">X</button>';
  ztotal.innerHTML= 'Total: ' + total + ' $';
  zcart.innerHTML+='<li>'+name+ ' '+ size + ': '+ price+' $'+butto+'</li>';
  
  }

  function zshoppingcart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =orders.length;
    zcart.innerHTML= '';
    for(let i =0; i< cartSize; i++){
        butto= '<button class="del btn-danger" onClick="removePizza('+ i+ ')">X</button>';
        zcart.innerHTML+='<li>'+ orders[i][0]+ ' '+ orders[i][1] + ': '+ orders[i][2]+' $'+butto+'</li>';
    }
    ztotal.innerHTML= 'Total: ' + total + ' $';
   }
   
   zshoppingcart();


   function removePizza(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total)- Number(orders[n][2]);
    orders.splice(n,1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    zshoppingcart();
  }
  

