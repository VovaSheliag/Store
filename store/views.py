from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Product, Cart, User
from .forms import PostFrom


class MainPageView(ListView):
    model = Product
    template_name = 'store/products.html'


# class ProductPostDetailView(DetailView):
#     model = Product
#     template_name = 'store/account.html'


class ProductPostAccountView(ListView):
    model = Product
    template_name = 'store/account.html'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class ProductPostCreateView(CreateView):
    model = Product
    form_class = PostFrom
    template_name = 'store/create_post.html'


class ProductPostUpdateView(UpdateView):
    model = Product
    form_class = PostFrom
    template_name = 'store/update_post.html'


class ProductPostDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('account_view')
    template_name = 'store/delete_post.html'


class CartView(ListView):
    model = Cart
    template_name = 'store/cart.html'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
