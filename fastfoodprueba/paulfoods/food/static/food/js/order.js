var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');



function addchicken(chickenId, name, desc, address, tel, priceM, priceL, datev) {
    var radio = 'chicken' + chickenId;
    var pri = document.getElementsByName(radio);

    var size, price;
    if (pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    } else {
        price = pri[1].value;
        size = 'L';
    }

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0.0;

    // Include chicken.datev in the order details
    var orderDetails = [name, size, price, datev];

    orders.push(orderDetails);
    localStorage.setItem('orders', JSON.stringify(orders));

    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    var butto = '<button class="del btn-danger" onClick="removeChicken(' + (orders.length - 1) + ')">X</button>';
    ptotal.innerHTML = 'Total: ' + total.toFixed(2) + ' $';
    // Include chicken.datev in the shopping cart list
    pcart.innerHTML += '<li>' + name + ' ' + size + ': ' + price + ' $ (' + datev + ')' + butto + '</li>';
}



function pshoppingcart(){
 var orders = JSON.parse(localStorage.getItem('orders'));
 var total = localStorage.getItem('total');
 var cartSize =orders.length;
 pcart.innerHTML= '';
 for(let i =0; i< cartSize; i++){
  butto= '<button class="del btn-danger" onClick="removeChicken('+ i+ ')">X</button>';
   pcart.innerHTML+='<li>'+ orders[i][0]+ ' '+ orders[i][1] + ': '+ orders[i][2]+' $'+' '+butto+'</li>';
 }
 ptotal.innerHTML= 'Total: ' + total + ' $';
}

pshoppingcart();



function removeChicken(n){
  var orders = JSON.parse(localStorage.getItem('orders'));
  var total = localStorage.getItem('total');
  total = Number(total)- Number(orders[n][2]);
  orders.splice(n,1);
  localStorage.setItem('orders', JSON.stringify(orders));
  localStorage.setItem('total', total);
  pshoppingcart();
}