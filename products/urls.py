
from django.contrib import admin
from django.urls import path
from products import views
urlpatterns = [
    path('', views.home), 
    path('inventory/', views.inventory), 
    path("delete/<int:id>",views.delete),
    path("inventory/details/<int:id>", views.details),
    path("create/", views.create),
    path("edit/<int:id>",views.edit)
    
    

    
]
