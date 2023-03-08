from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout")
]

