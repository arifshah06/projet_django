from django.shortcuts import render
from django.http import JsonResponse
from public.models import Compte

def index(request):
    Comptes = Compte.objects.all()

    return JsonResponse([compte.serialize() for compte in Comptes], safe=False)
