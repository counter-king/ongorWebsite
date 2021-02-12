from django.urls import path
from .import views
from .views import Order, Gallery

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    # path('order/', views.order, name="order"),
    path('order/', Order.as_view(), name='order'),
    path('gallery/', Gallery.as_view(), name='gallery'),
]