from django.urls import path
from .views import (ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView, ProductDeleteView)
from . import views


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('post/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('post/new/', ProductCreateView.as_view(), name='product-create'),
    path('post/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete')
]

# <app>/<model>_<viewtype>.html