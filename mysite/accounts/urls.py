from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('toggle-admin/<int:user_id>/', views.toggle_admin, name='toggle_admin'),
]