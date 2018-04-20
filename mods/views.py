from django.shortcuts import render
from mods.models import User, Cart, Product


# Create your views here.
def post_list(request):
    return render(request, 'mods/post_list.html', {})


User.userOb.all()
Cart.cartOb.all()
Product.productOb.all()