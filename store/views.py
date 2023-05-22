from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "store.html", {'products': products})

def store(request):
    action = request.POST.get('btn-add')
    name = request.POST.get('name')
    price = request.POST.get('price')
    if action == 'addProduct':
        if Product.objects.get(name=name):
            messages.warning(request, 'Already exists a product with name {}.'.format(name))
        else:
            Product.objects.create(name=name, price=price)
            messages.success(request, 'Product named {} created successfully.'.format(name))
    return redirect('/')

def edit(request, id):
    product = Product.objects.get(id=id)
    print(product, id)
    #name = request.POST['name']
    #price = request.POST['price']
    if not product:
        messages.warning(request, 'Does not exist a product with id {}.'.format(id))
        return redirect('/')
    else:
        return render(request, "edit.html", {'product': product})

def editP(request):
    action = request.POST.get('btn-add')
    id = request.POST.get('id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    if action == 'editProduct':
        product = Product.objects.get(id=id)
        product.name = name
        product.price = price
        product.save()
        messages.success(request, 'Product named {} edited successfully.'.format(name))
    return redirect('/')

def delete(request, id):
    product = Product.objects.get(id=id)
    if not product:
        messages.warning(request, 'The product with id {} does not exists.'.format(id))
    else:
        product.delete()
        messages.success(request, 'Product with id {} created successfully.'.format(id))
    return redirect('/')
