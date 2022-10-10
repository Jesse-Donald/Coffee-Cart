from ast import Delete
from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    print(request.POST)

    if request.method == 'POST':
        new_order = Order()
        new_order.name = request.POST.get('name')
        new_order.drink = request.POST.get('cat') + " : " + request.POST.get('type')
        new_order.milk = request.POST.get('milk')
        new_order.temperature = request.POST.get('temp')
        if request.POST.get('Caffination') == 'caffinated':
            new_order.decaf = True
        else:
            new_order.decaf = False
        new_order.strength = request.POST.get('strength')
        new_order.sugar = request.POST.get('sugar')
        new_order.completed = False
        new_order.save()
        print(Order.objects.all())

    return render(request, 'orderform.html')

def dashboard(request):
    if request.user.has_perm('coffeecart.vieworder'):
        data = Order.objects.all().order_by('completed')
        return render(request, 'dashboard.html', {'data': data})
    else:
        return redirect('/ordering')

def completeorder(request, id):
    order = Order.objects.filter(id = id)[0]
    order.completed = True
    order.save()
    print(order.completed)
    return redirect(dashboard)

def undocomplete(request, id):
    order = Order.objects.filter(id = id)[0]
    order.delete()
    return redirect(dashboard)