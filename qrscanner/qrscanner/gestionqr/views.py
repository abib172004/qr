from django.shortcuts import render
from django.http import JsonResponse
from .models import Visiteur, Scan
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt

def page_scan(request):
    return render(request, "page_scan.html")

@csrf_exempt

def verifier_visiteur(request):
    donnees = json.loads(request.body)
    identifiant = donnees.get("identifiant")
    try:
        visiteur = Visiteur.objects.get(identifiant_appareil=identifiant)
        Scan.objects.create(visiteur=visiteur, ip=request.META.get("REMOTE_ADDR"))
        return JsonResponse({"nom": visiteur.nom})
    except Visiteur.DoesNotExist:
        return JsonResponse({"nom": None})

@csrf_exempt

def enregistrer_nom(request):
    donnees = json.loads(request.body)
    identifiant = donnees.get("identifiant")
    nom = donnees.get("nom")
    visiteur, cree = Visiteur.objects.get_or_create(identifiant_appareil=identifiant, defaults={"nom": nom})
    return JsonResponse({"status": "ok", "nom": visiteur.nom})