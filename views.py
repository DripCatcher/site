from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def cards(request):
    name = request.GET['name']
    cardn = request.GET['card_number']
    cardt = request.GET['card_type']
    date = request.GET['exp_date']
    cvv = request.GET['cvv']
    return render(request, 'main/cards.html', {'card_number': cardn, 'name': name, 'card_type': cardt, 'exp_date': date, 'cvv': cvv})