
from django.urls import path
from quotes import views 

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('create_quote//', views.create_quote, name='create_quote'),
    path('create_author/', views.create_author, name='create_author'),
]
