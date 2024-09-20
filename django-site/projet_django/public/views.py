from django.shortcuts import render
from public.models import Compte

# Create your views here.

def website(request):
    Comptes = Compte.objects.all()
    return render(request, 'index.html', {'Comptes':Comptes})

# Define other views (e.g., contact, product) similarly
