from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', login_required(views.notes), name='notes'),
    path('add/', login_required(views.add), name='add'),
    path('edit/<int:note_id>/', login_required(views.edit), name='edit'),
    path('delete/<int:note_id>/', login_required(views.delete), name='delete'),

    # authentication urls
    path('register/', views.createUser, name='create-user'),
    path('login', auth_views.LoginView.as_view(template_name = 'index/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
]