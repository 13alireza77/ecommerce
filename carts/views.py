from django.shortcuts import render, redirect
from .models import cart
from products.models import Product


def cart_home(request):
    # del request.session['cart_id']
    # request.session['cart_id'] = "12"
    cart_obj, new_obj = cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, "carts/home.html", {})


def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    return redirect(product_obj.get_absolute_url())
