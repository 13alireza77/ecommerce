from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            isinstance = get_object_or_404(Product, slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("product doesnt exist")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            isinstance = qs.first()
        except:
            raise Http404("!404!...")
        return isinstance


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured_detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        rquest = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = get_object_or_404(Product, pk=pk, featured=True)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
