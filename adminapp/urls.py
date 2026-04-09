from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.adminhome),
    path('courseentry/',views.courseentry),
    path('courselist/',views.courselist),
    path('studentlist/',views.studentlist),
    path('adminlogout/',views.adminlogout),
    path('batchentry/',views.batchentry),
    path('batchlist1/',views.batchlist1),
    path('editcourse/',views.editcourse),
]