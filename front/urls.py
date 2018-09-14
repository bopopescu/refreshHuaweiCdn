from django.urls import path
from . import  views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'login/', views.login, name='login'),
    path('work/', views.work, name='work'),
    path('refreshlog/<int:page>', views.refresh_log, name='refresh_log'),
    path('logout/', views.logout, name='logout'),
    path('connect/admin/', views.connect_admin, name='connect_admin'),
]