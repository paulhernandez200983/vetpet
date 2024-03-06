from email import message
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chicken1
from .models import Burger1
from .models import Drink1
from .models import Steak1
from .models import Pizza1
from .forms import NewUserForm
from django.contrib.auth import authenticate,login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    request.session.set_expiry(0)
    chickens= Chicken1.objects.all()
    ctx={'chickens':chickens,'active_link': 'index'}
    return render(request, 'foods/index.html', ctx)




def burger(request):
    request.session.set_expiry(0)
    burgers= Burger1.objects.all()
    chickens= Chicken1.objects.all()
    ctx = {'chickens':chickens,'burgers':burgers, 'active_link':'burger'}
    print(burgers)
    return render(request, 'foods/burger.html', ctx)

def drink(request):
    request.session.set_expiry(0)
    drinks= Drink1.objects.all()
    ctx = {'drinks':drinks}
    print(drinks)
    return render(request, 'foods/drinks.html', ctx)

def steak(request):
    request.session.set_expiry(0)
    steaks= Steak1.objects.all()
    chickens= Chicken1.objects.all()
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    
    # Obtener los elementos del carrito
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    print(steaks)
    print(chickens)
    return render(request, 'foods/steak.html', {'chickens': chickens, 'items_carrito': items_carrito})

def pizza(request):
    request.session.set_expiry(0)
    pizzas= Pizza1.objects.all()
    ctx = {'pizzas':pizzas}
    print(pizzas)
    return render(request, 'foods/pizza.html',ctx)

def contact(request):
    return render(request, 'foods/contact.html')

@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
     request.session['note']=request.POST.get('note')
     request.session['order']=request.POST.get('orders')
    
    ctx={'active_link': 'order'}
    return render(request, 'foods/order.html',ctx)

def succes(request):
    order= request.session['order']
    ctx= {'order': order}
    return render(request, 'foods/succes.html', ctx)

def tarjeta(request):
    
    
    return render(request, 'foods/tarjeta.html')
from django.shortcuts import render, redirect
from .forms import NewUserForm

def signup(request):
    ctx = {}
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirecciona a la página de inicio de sesión
        else:
            ctx['form'] = form
            return render(request, 'foods/signup.html', ctx)  # Retorna la página de registro con errores en el formulario
    else:
        form = NewUserForm()
        ctx['form'] = form
        return render(request, 'foods/signup.html', ctx)  # Retorna la página de registro con un formulario vacío



def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirecciona a la página de inicio después del inicio de sesión
        else:
            messages.info(request, 'Username or password are incorrect')
    ctx = {'active_link': 'login'}
    return render(request, 'foods/login.html', ctx)


def logOut(request):
    logout(request)
    return redirect('index')



def profile(request):
    user_data = None

    if request.method == 'POST':
        # Procesar el formulario y obtener los datos del usuario
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        # Puedes hacer algo con estos datos, como almacenarlos en el modelo del usuario

        # Puedes asignar los datos para mostrarlos en la plantilla
        user_data = {'username': username, 'email': email}

    return render(request, 'foods/pizza.html', {'user_data': user_data})


from django.shortcuts import render, get_object_or_404
from .models import Chicken1, ChickenReview

def detailsv(request, chicken_id):
    chicken = get_object_or_404(Chicken1, id=chicken_id)
    reviews = ChickenReview.objects.filter(chicken=chicken)
    return render(request, 'foods/details.html', {'chicken': chicken, 'reviews': reviews})


def reviews(request):
    cabo_reviews = [
        {"author": "John Doe", "rating": 5, "comment": "¡Increíble experiencia en Los Cabos! Altamente recomendado."},
        {"author": "Alice Smith", "rating": 4, "comment": "Los Cabos es un destino hermoso, definitivamente vale la pena visitarlo."},
        # Agrega más reseñas de Los Cabos aquí
    ]

    cancun_reviews = [
        {"author": "Emily Johnson", "rating": 5, "comment": "¡Cancún es el paraíso en la tierra! Playas impresionantes y excelente servicio."},
        {"author": "Michael Brown", "rating": 4, "comment": "Disfrutamos mucho nuestras vacaciones en Cancún. Volveremos pronto."},
        # Agrega más reseñas de Cancún aquí
    ]

    tulum_reviews = [
        {"author": "Sophia Garcia", "rating": 5, "comment": "Tulum es mágico. La combinación perfecta de naturaleza y cultura."},
        {"author": "David Martinez", "rating": 4, "comment": "Nos encantó la experiencia en Tulum. Recomendamos visitar las ruinas."},
        # Agrega más reseñas de Tulum aquí
    ]

    return render(request, 'foods/drinks.html', {
        'cabo_reviews': cabo_reviews,
        'cancun_reviews': cancun_reviews,
        'tulum_reviews': tulum_reviews
    })
    
from django.shortcuts import render, redirect
from .models import Order, Items
from django.contrib.auth.decorators import login_required
import json
@login_required
def checkout(request):
    # Obtener el usuario actual
    user = request.user
    
    # Crear un nuevo pedido para el usuario actual
    new_order = Order.objects.create(customer=user, number="123456", bill=0)  # Aquí puedes definir tu lógica para generar el número de pedido y el monto total
    
    # Obtener los productos del carrito del usuario
    cart_items = json.loads(request.session.get('#pcart', '[]'))
    
    total_bill = 0
    
    # Guardar los elementos del carrito en la base de datos
    for item in cart_items:
        product_name = item['name']
        product_price = item['price']
        product_size = item['size']
        
        # Crear un nuevo objeto Items y asociarlo con el pedido creado
        new_item = Items.objects.create(order=new_order, name=product_name, price=product_price, size=product_size)
        
        total_bill += product_price
    
    # Actualizar el monto total del pedido
    new_order.bill = total_bill
    new_order.save()
    
    # Limpiar el carrito después de realizar el pedido
    request.session['#pcart'] = json.dumps([])
    
    return redirect('order_success')  # Redirigir a una página de confirmación de pedido exitoso




def payment_processp(request):
   
    paypal_dict = {
        "business": "seller@example.com",
        "amount": "2000",
        "currency_code": "MXN",
        "item_name": "Viajes",
        "invoice": "unique-invoice-id",
       
        "return_url": "https://www.example.com/your-return-url/",
        "cancel_return": "https://www.example.com/your-cancel-url/",
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'foods/succes.html', {'form': form})


from django.shortcuts import render, redirect
from .models import WishlistItem

def add_to_wishlist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        WishlistItem.objects.create(name=name)
        return redirect('wishlist')  # Redirige a la vista de la lista de deseos
    return render(request, 'foods/chicken.html')


def wishlist(request):
    items = WishlistItem.objects.all()
    return render(request, 'foods/chicken.html', {'items': items})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Chicken1, Carrito, ItemCarrito
from .forms import AgregarPolloForm
from .models import CustomUser
@login_required
def agregar_al_carrito(request, chicken_id):
    pollo = get_object_or_404(Chicken1, pk=chicken_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, pollo=pollo)
    if not item_created:
        item.cantidad += 1
        item.save()
    from django.urls import reverse

    return redirect('food:chicken')

def ver_chickens(request):
    # Obtener todos los pollos
    chickens = Chicken1.objects.all()
    
    # Obtener el carrito del usuario actual
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    
    # Obtener los elementos del carrito
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    return render(request, 'foods/chicken.html', 'foods/steak.html', {'chickens': chickens, 'items_carrito': items_carrito})

def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, pk=item_id)
    item.delete()
    return redirect('food:chicken')

@login_required
def ver_chickens(request):
    # Obtener todos los pollos
    chickens = Chicken1.objects.all()
    
    # Obtener el carrito del usuario actual
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    
    # Obtener los elementos del carrito
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    return render(request, 'foods/chicken.html','foods/steak.html', {'chickens': chickens, 'items_carrito': items_carrito})


def chicken(request):
    request.session.set_expiry(0)
    chickens= Chicken1.objects.all()
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    
    # Obtener los elementos del carrito
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    ctx = {'chickens':chickens, 'active_link':'chicken'}
    print(chickens)
    cards_per_page = 4

    paginator = Paginator(chickens, cards_per_page)
    page = request.GET.get('page')

    try:
        chickens = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        chickens = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver the last page of results.
        chickens = paginator.page(paginator.num_pages)

    context = {
        'chickens': chickens,
        'page_obj': chickens,  # This is useful for rendering page navigation in the template
        'active_link': 'chicken',  # Add your active link logic here
    }
    return render(request, 'foods/chicken.html' , {'chickens': chickens, 'items_carrito': items_carrito})



def ver_carrito_y_pagar(request):
    # Obtener el carrito del usuario actual
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    
    # Obtener los elementos del carrito
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    # Calcular el total del carrito
    total_carrito = sum(item.pollo.priceM * item.cantidad for item in items_carrito)
    
    return render(request, 'foods/ver_carrito_y_pagar.html', {'items_carrito': items_carrito, 'total_carrito': total_carrito})


from .models import procesar_pago
from .forms import Payment  # Asumiendo que tienes un formulario para ingresar los detalles del pago

@login_required
def procesar_pago(request):
    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            # Procesar el pago y guardar los detalles en la base de datos
            amount = form.cleaned_data['amount']
            # Aquí podrías realizar la lógica de procesamiento del pago, como interactuar con una API de pago, etc.
            procesar_pago.objects.create(user=request.user, amount=amount)
            # Redirigir a una página de confirmación de pago o a cualquier otra página deseada
            return redirect('ruta_de_confirmacion_de_pago')
    else:
        form = Payment()
    return render(request, 'ruta_de_la_vista_para_el_formulario_de_pago.html', {'form': form})



from django.shortcuts import render
from django.conf import settings
from paypalrestsdk import Payment

def process_payment(request):
    paypal_client_id = 'AeetpAe5qdHU2LnDoKjcw-PWtDJGA2RCGAAQFupjPNuTAclwdayUODEkIf90apRdw9N1_FbrBTjE34U1'
    paypal_secret_key = 'EAIKtUqz9aS2JEi1Tw0__C3pWrz1FYumbNI1vlL08qTQarmHjUbW2jB_Ppa_MS7tuNnkSHxlrkClNvQl'
    
    # Lógica para iniciar el pago con PayPal
    # Aquí debes usar las credenciales de la API de PayPal
    # y configurar los detalles del pago
    payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:8000/payment/execute/",
            "cancel_url": "http://localhost:8000/payment/cancel/"
        },
        "transactions": [{
            "amount": {
                "total": "10.00",
                "currency": "USD"
            },
            "description": "Payment description"
        }]
    }, client_id=paypal_client_id, client_secret=paypal_secret_key)
    
    if payment.create():
        # Redireccionar al usuario a la página de PayPal para completar la transacción
        for link in payment.links:
            if link.method == "REDIRECT":
                return redirect(link.href)
    else:
        return render(request, 'payment/error.html', {'message': payment.error})
    
from django.urls import reverse

    
import uuid
def CheckOutp(request, chicken_id):

    chickens = Chicken1.objects.get(id=chicken_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': chickens.price,
        'item_name': chickens.name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'product_id': chicken.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'product_id': chicken.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': chicken,
        'paypal': paypal_payment
    }

    return render(request, 'checkout.html', context)

def PaymentSuccessful(request, product_id):

    product = chicken.objects.get(id=product_id)

    return render(request, 'payment-success.html', {'product': product})

def paymentFailed(request, product_id):

    product = chicken.objects.get(id=product_id)

    return render(request, 'payment-failed.html', {'product': product})


from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from paypalrestsdk import Payment
import paypalrestsdk

def ver_carrito_y_pagarp(request):
    paypal_client_id = 'AeetpAe5qdHU2LnDoKjcw-PWtDJGA2RCGAAQFupjPNuTAclwdayUODEkIf90apRdw9N1_FbrBTjE34U1'
    paypal_secret_key = 'EAIKtUqz9aS2JEi1Tw0__C3pWrz1FYumbNI1vlL08qTQarmHjUbW2jB_Ppa_MS7tuNnkSHxlrkClNvQl'
    
    # Obtener el carrito del usuario actual
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    
    # Obtener los elementos del carrito
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    # Calcular el total del carrito
    total_carrito = sum(item.pollo.priceM * item.cantidad for item in items_carrito)
    
    # Crear el pago de PayPal
    payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('food:succes')),
            "cancel_url": request.build_absolute_uri(reverse('food:succes'))
        },
        "transactions": [{
            "amount": {
                "total": str(total_carrito),
                "currency": "USD"
            },
            "description": "Pago por los productos del carrito"
        }]
    })
    from django.conf import settings
    # Autenticar con las credenciales de PayPal
    payment=paypalrestsdk.config ({
    "mode": settings.PAYPAL_MODE,
        "client_id": "AeetpAe5qdHU2LnDoKjcw-PWtDJGA2RCGAAQFupjPNuTAclwdayUODEkIf90apRdw9N1_FbrBTjE34U1",
        "client_secret": "EAIKtUqz9aS2JEi1Tw0__C3pWrz1FYumbNI1vlL08qTQarmHjUbW2jB_Ppa_MS7tuNnkSHxlrkClNvQl"
    })
    
    payment.config(**payment)

    # Crear el pago
    if payment.create():
        # Redirigir al usuario a la página de PayPal para realizar el pago
        for link in payment.links:
            if link.method == "REDIRECT":
                return redirect(link.href)
    else:
        # Manejar errores de manera adecuada
        error_message = payment.error['message'] if payment.error else "Error desconocido al crear el pago."
        return render(request, 'payment/error.html', {'message': error_message})
    
    
    
from django.shortcuts import redirect
from .models import ChickenReview

def add_review(request):
    if request.method == 'POST':
        chicken_id = request.POST.get('chicken_id')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        # Crea una nueva instancia de Review asociada al pollo específico
        ChickenReview.objects.create(chicken_id=chicken_id, rating=rating, comment=comment, user=request.user)
        return redirect('food:details', chicken_id=chicken_id)
    else:
        return redirect('index')  # Redirige a la página de inicio si la solicitud no es POST



from django.shortcuts import render
from paypalrestsdk import Payment
from django.conf import settings

def paymen(request):
    # Configura las credenciales de la cuenta de PayPal Sandbox
    client_id = settings.PAYPAL_CLIENT_ID
    client_secret = settings.PAYPAL_CLIENT_SECRET
    paypal_mode = settings.PAYPAL_MODE

    # Configura el objeto Payment de PayPal
    paypal_payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:8000/payment/execute/",
            "cancel_url": "http://localhost:8000/payment/cancel/"
        },
        "transactions": [{
            "amount": {
                "total": "10.00",
                "currency": "USD"
            },
            "description": "Compra de ejemplo"
        }]
    })

    # Autentica con las credenciales de PayPal Sandbox
    paypal_payment.set_client_id(client_id)
    paypal_payment.set_client_secret(client_secret)

    # Crea el pago
    if paypal_payment.create():
        for link in paypal_payment.links:
            if link.rel == 'approval_url':
                approval_url = link.href
                return render(request, 'payment/paypal_payment.html', {'approval_url': approval_url})
    else:
        return render(request, 'payment/payment_error.html')