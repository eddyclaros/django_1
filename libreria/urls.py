from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
]