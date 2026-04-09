from django.contrib import admin
from django.urls import include, path

from . import views

#for display image
from django.conf.urls.static import static
from django.conf import settings
media_url=settings.MEDIA_URL  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path ('login/',views.login),
    path('register/',views.register),
    path('adminhome/',include('adminapp.urls')),
    path('studenthome/',include('studentapp.urls')),
    path('courselist3/',views.courselist3),
    path('batchlist3/',views.batchlist3),
]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT) 


