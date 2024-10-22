from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:note_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('<int:note_id>/delete/', views.delete, name='delete'),
    path('<int:note_id>/edit/', views.edit, name='edit'),
]
