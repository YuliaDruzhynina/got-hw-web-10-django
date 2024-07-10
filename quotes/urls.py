
from django.urls import path
from quotes import views 

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("quotes/", views.main, name="login"),
    
]
