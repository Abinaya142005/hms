from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patient_list, name='patient-list'),
    path('<int:patient_id>/', views.patient_detail, name='patient-detail'),
    path('create/', views.patient_create, name='patient-create'),
    path('<int:patient_id>/update/', views.patient_update, name='patient-update'),
    path('<int:patient_id>/delete/', views.patient_delete, name='patient-delete'),
]
