from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.studenthome),
    path('courselist2/',views.courselist2),
    path('batchlist2/',views.batchlist2),
    path('admission/',views.admission),
    path('success/',views.success),
    path('updateprofile/',views.updateprofile),
    
]