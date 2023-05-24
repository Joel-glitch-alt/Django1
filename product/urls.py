
from django.urls import  path

from product.views import all_product_view, index_view
app_name = 'core'
urlpatterns = [
    path('',index_view, name= 'index'),
    path('all-product',all_product_view, name = 'all-product')
]
