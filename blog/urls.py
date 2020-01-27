from django.conf.urls import include, url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.post_list),
    path('inicio/', views.index, name="index"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('donaciones/', views.donaciones, name="donaciones"),
    path('contacto/', views.contacto, name="contacto"),
    path('formulario/', views.formulario, name="formulario"),
    path('accounts/', include('django.contrib.auth.urls')),
]
