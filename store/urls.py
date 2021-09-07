from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('create/', views.ProductPostCreateView.as_view(), name='create_post'),
    path('update/<int:pk>', views.ProductPostUpdateView.as_view(), name='update_post'),
    path('account/', views.ProductPostAccountView.as_view(), name='account_view'),
    path('delete/<int:pk>', views.ProductPostDeleteView.as_view(), name='delete_post'),
    path('cart/', views.CartView.as_view(), name='cart_view')
]