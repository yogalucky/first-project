
from django.contrib import admin
from django.urls import path
from app7.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',first,name='first'),
]
