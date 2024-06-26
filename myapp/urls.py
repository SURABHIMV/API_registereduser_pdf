from django.urls import path
from myapp.views import *
# from ApiApplication.views import *
from myapp import views

urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('', views.Userview.as_view(), name='ffsfs'),
    path('logout', views.LogoutView.as_view(), name='jjkk')
]
