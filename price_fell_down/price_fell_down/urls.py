from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.button, name='button')
    #path('admin/', admin.site.urls),
    
]
