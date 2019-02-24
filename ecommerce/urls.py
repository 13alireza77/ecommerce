"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import homePage, aboutPage, contactPage, loginPage, registerPge
from django.views.generic import TemplateView

# from products.views import ProductListView, product_list_view, product_detail_view, ProductDetailView, \
#     ProductFeaturedListView, ProductFeaturedDetailView,ProductDetailSlugView

urlpatterns = [
    path('', homePage, name='home'),
    path('contact/', contactPage, name='contact'),
    path('login/', loginPage, name='login'),
    path('register/', registerPge, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('about/', aboutPage, name='about'),
    path('admin/', admin.site.urls),
    url(r'^products/', include(("products.urls", 'products'), namespace='products')),
    url(r'^cart/', include(("carts.urls", 'cart'), namespace='cart')),
    url(r'^search/', include(("search.urls", 'search'), namespace='serach')),
    # path('products/', ProductListView.as_view()),
    # path('products_fbv/', product_list_view),
    # path('products/(?P<pk>/d+)/', ProductDetailView.as_view()),
    # # path('products_fbv/(?P<pk>/d+)/', product_detail_view),
    # # path('products/(?P<pk>\d+)/', ProductDetailView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
