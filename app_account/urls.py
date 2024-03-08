from django.urls import path
from . import views

app_name='app_account'
urlpatterns = [
    path('login/', views.user_login, name='user_login')
]
