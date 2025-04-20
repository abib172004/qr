from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_scan, name='page_scan'),
    path('verifier/', views.verifier_visiteur, name='verifier_visiteur'),
    path('enregistrer/', views.enregistrer_nom, name='enregistrer_nom'),
]