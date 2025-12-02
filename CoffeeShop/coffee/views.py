from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Coffee, Order
from .forms import OrderForm

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html',{'coffee':coffee})

def order_coffee(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.coffee = coffee
            order.save()
            messages.success(request, "Order placed successfully!")
            return redirect('home')

    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form, 'coffee': coffee})
