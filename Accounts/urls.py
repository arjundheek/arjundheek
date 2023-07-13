from django.urls import path
from . import views

app_name = 'Accounts'

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('delete/', views.account_delete, name='account_delete'),
    path('delete-user/', views.delete_user, name='delete_user'),
    path('renewal/', views.account_renewal, name='account_renewal')
]
