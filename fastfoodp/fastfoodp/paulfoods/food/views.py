from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    ctx ={'name': 'PAULFOODS', 'msg': 'Django project'}
    return render(request, 'foods/index.html', ctx)


def chicken(request):
    return HttpResponse('You are viewing chicken options')