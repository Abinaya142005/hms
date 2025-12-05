from django.urls import path
from . import views

app_name = 'prescriptions'

urlpatterns = [
    path('', views.prescription_list, name='prescription-list'),
    path('<int:prescription_id>/', views.prescription_detail, name='prescription-detail'),
    path('patient/<int:patient_id>/create/', views.prescription_create, name='prescription-create'),
    path('<int:prescription_id>/update/', views.prescription_update, name='prescription-update'),
    path('<int:prescription_id>/delete/', views.prescription_delete, name='prescription-delete'),
]
