from django.conf.urls import url, include
from django.urls import path
from .views import ProductListView, product_list_view, product_detail_view, ProductDetailView, \
    ProductFeaturedListView, ProductFeaturedDetailView, ProductDetailSlugView

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
