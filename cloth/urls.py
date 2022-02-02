from django.urls import path
from . import views
from . import models

apps_name = 'product'
urlpatterns = [
    path('product/', views.ProductListView.as_view(queryset = models.ProductCL.objects.all()),
    name = 'product'),
    path('product/dior', views.ProductListView.as_view(queryset = models.ProductCL.objects.filter(tag__name='Dior')),
    name = 'Dior'),
    path('product/gucci', views.ProductListView.as_view(queryset = models.ProductCL.objects.filter(tag__name='Gucci')),
    name = 'Gucci'),
    path('product/chanel', views.ProductListView.as_view(queryset = models.ProductCL.objects.filter(tag__name='Chanel')),
    name = 'Chanel'),
    path('product/celvincline', views.ProductListView.as_view(queryset = models.ProductCL.objects.filter(tag__name='Celvin Cline')),
    name = 'Celvin Cline'),
    path('create/', views.OrderCreateView.as_view(), name = 'create')
]