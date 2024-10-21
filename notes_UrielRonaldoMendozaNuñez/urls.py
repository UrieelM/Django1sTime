
# from django.urls import path
# from . import views

# app_name = "notes"
# urlpatterns = [
#     path('hola/', views.hola),
#     path('', views.list),
#     path("<int:note_id>/note", views.detail, name="detail")
# ]

from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:note_id>/', views.detail, name='detail'),
]
