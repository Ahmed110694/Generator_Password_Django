from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def about (request):
    return render(request,'Generator/about.html')

def home (request):
    return render(request,'Generator/home.html')

def password (request):

    charactere = list('abcdefghjklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactere.extend(list('ABCDEFGHIJKLMNOPQRSTUWXYZ'))

    if request.GET.get('numbers'):
        charactere.extend(list('0123456789'))

    if request.GET.get('special'):
        charactere.extend(list('&#[]{}()\|'))

    charx=''
    length =int (request.GET.get('length',15))

    for x in range(length):
        charx += random.choice(charactere)

    return  render (request,'Generator/password.html',{'password':charx})


