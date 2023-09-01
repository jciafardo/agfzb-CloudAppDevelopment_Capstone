from . import views
from django.urls import path

# Urls for accounts pages
urlpatterns = [
    path('login', views.login_page, name='login_page'),
    path('register', views.register_page, name='register_page'),
    path('accounts', views.accounts, name='accounts'),
    path('logout', views.logout_page, name='logout_page')

]