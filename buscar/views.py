from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
# Renombre el modelo importado
# se me ocurria que podia haber un conflicto de nombres
from .models import buscar as buscado

# Create your views here.
def buscar(request):
	return render(request, 'buscar/buscar.html', {})

def resultado(request):
    if request.POST:
        q = request.POST['search']
        # Aqui cambie el nombre ya que hace referencia al modelo
        videos = buscado.objects.filter(nombre__icontains=q)
        return render(request, 'buscar/resultado.html', {'videos': videos, 'query': q})
    else:
        return HttpResponse('Por favor envíe un mombre valido.')