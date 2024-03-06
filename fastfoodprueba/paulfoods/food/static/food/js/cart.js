var nam= document.querySelector("#name");
var size= document.querySelector("#size");
var price= document.querySelector("#price");
var bill= document.querySelector("#total");
var rm= document.querySelector("#rm");


function shoppingcart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize =orders.length;
    nam.innerHTML='<h3>Name</h3>';
    size.innerHTML='<h3>Size</h3>';
    price.innerHTML='<h3>Price</h3>';
    rm.innerHTML='<h3>ELIMINAR</h3>';
 
 

    for(let i =0; i< cartSize; i++){
     rm.innerHTML+= '<h4><button class="del btn-danger" onClick="removeItem('+ i+ ')" style="position:relative">X</button></h4>';
      nam.innerHTML+= '<h4>' + orders[i][0]+'</h4>'
      size.innerHTML+= '<h4>' + orders[i][1]+'</h4>'
      price.innerHTML+= '<h4>' + orders[i][2]+'</h4>'
    }
    bill.innerHTML= 'Total: ' + total + ' $';
   }
   
   shoppingcart();



   function removeItem(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total)- Number(orders[n][2]);
    orders.splice(n,1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    shoppingcart();
  }


  var note = document.querySelector('#message');
  
  function order(){
    var msg = note.value;
    var orders= localStorage.getItem('orders');
    var ur = '/food/order';
    var orderData= {};
    orderData['orders']=orders;
    orderData['note']=msg;
    $.ajax({
        url:ur,
        type: "POST",
        data: orderData,
        success: function(data){
            window.location.replace('/food/succes')
            localStorage.setItem('orders', JSON.stringify([]));
            localStorage.setItem('total', 0);
        }
    })
  }