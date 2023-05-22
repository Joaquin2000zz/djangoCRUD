from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('store/', views.store),
    path('edit/<id>', views.edit),
    path('editP/', views.editP),
    path('delete/<id>', views.delete)
]