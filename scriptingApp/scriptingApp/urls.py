from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.button,name="home"),
    path('output',views.output, name="script")
]
