var scart = document.querySelector('#scart');
var stotal = document.querySelector('#stotal');

function addsteak(sid){


    steakid= '#stea'+sid;
    var name= document.querySelector(steakid).innerHTML;
    var radio= 'steak'+sid;
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
  
  butto= '<button class="del btn-danger" onClick="removeSteak('+ cartSize+ ')">X</button>';
  stotal.innerHTML= 'Total: ' + total + ' $';
  scart.innerHTML+='<li>'+name+ ' '+ size + ': '+ price+' $'+butto+'</li>';
  
  }

  function sshoppingcart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =orders.length;
    scart.innerHTML= '';
    for(let i =0; i< cartSize; i++){
        butto= '<button class="del btn-danger" onClick="removeSteak('+ i+ ')">X</button>';
   scart.innerHTML+='<li>'+ orders[i][0]+ ' '+ orders[i][1] + ': '+ orders[i][2]+' $'+butto+'</li>';
    }
    stotal.innerHTML= 'Total: ' + total + ' $';
   }
   
   sshoppingcart();



   function removeSteak(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total)- Number(orders[n][2]);
    orders.splice(n,1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    sshoppingcart();
  }
  