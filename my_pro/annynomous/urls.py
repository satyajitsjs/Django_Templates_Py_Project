from django.contrib import admin
from django.urls import path
from annynomous import views as v

urlpatterns = [
    path('update',v.update),
    path('viewc/',v.viewc),
    path('viewf/',v.viewf),
    path('viewdata/',v.viewdata),
    path('',v.index),
    path('index',v.index),
    path('register',v.register),
    path('login/',v.login),
    path('about',v.about),
    path('contact',v.contact),
    path('feedback',v.feedback),
    path('gallery/',v.gallery),

]
