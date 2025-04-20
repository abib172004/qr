from django.db import models

class Visiteur(models.Model):
    identifiant_appareil = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

class Scan(models.Model):
    visiteur = models.ForeignKey(Visiteur, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    moment = models.DateTimeField(auto_now_add=True)