from django.urls import path
from .views import doctors_list,doctor_edit, doctor_create, doctor_delete,DoctorListCreateApiView
  
urlpatterns = [
      path('', doctors_list),
      path('<int:pk>/edit', doctor_edit),
      path('create', doctor_create),
      path('<int:pk>/delete', doctor_delete),
      path('api', DoctorListCreateApiView.as_view())
  ]
