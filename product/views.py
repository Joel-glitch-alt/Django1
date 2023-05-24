from django.shortcuts import render

from product.models import Product

# Create your views here.

def index_view(request):
    template_name = 'index.html'
    context = {}
    return render(request,template_name,context)



def all_product_view(request):
    template_name = 'all_product.html'
    product = Product.objects.all()
    context = {
        'product_key': product
    }
    return render(request,template_name,context)
