from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Mock data
products = [
    {
        'title': 'One Flex point',
        'cost': '$1',
        'image': '/static/contractor/flex.jpg',
        'likes': '0'
    },
    {
        'title': 'Five Flex points',
        'cost': '$5',
        'image': '/static/contractor/flex.jpg',
    },
    {
        'title': '10 Flex points',
        'cost': '$9',
        'image': '/static/contractor/flex.jpg',
    }   
]

def home(request):
    context = {
        'products': products
        # 'products': Product.objects.all()
    }
    return render(request, 'contractor/home.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'products/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    # ordering = ['-date_posted'] # to order from newest to oldest
    paginate_by = 5

class UserProductListView(ListView):
    model = Product
    template_name = 'products/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    # ordering = ['-date_posted'] # to order from newest to oldest
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-date_posted')

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title'], ['description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title'], ['description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'contractor/about.html', {'title': 'About'})