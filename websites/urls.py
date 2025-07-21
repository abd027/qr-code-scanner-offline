from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('qrcode/<str:pk>', views.qrcode, name="qrcode")
]
