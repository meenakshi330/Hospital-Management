from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('create', views.appointment_create, name='appointment_create'),
    path('<int:id>/edit', views.appointment_edit, name='appointment_edit'),
    path('<int:id>/delete', views.appointment_delete, name='appointment_delete'),
]