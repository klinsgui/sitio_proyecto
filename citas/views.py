from django.shortcuts import render, get_object_or_404
from .models import Citar
from django.utils import timezone
from .forms import CitasFormularios
from django.shortcuts import redirect
from datetime import date
import time

# Create your views here.
def listar_citas(request):
    citasprogramadas = Citar.objects.filter(realizada=False, fecha_cita__lte = date.today())#.order_by('fecha_cita'))
    return render(request, 'citas/listar.html', {'citas': citasprogramadas})

def detalle_cita(request, pk):
    cit = get_object_or_404(Citar, pk=pk)
    return render(request, 'citas/detalle.html', {'cita': cit})

def cita_nueva(request):
    if request.method == "POST":
        form = CitasFormularios(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = request.user
            cita.save()
            return redirect('citas.views.detalle_cita', pk=cita.pk)
    else:
        form = CitasFormularios()
    return render(request, 'citas/editar.html', {'form': form})


def editar_cita(request, pk):
    cita = get_object_or_404(Citar, pk=pk)
    if request.method == "POST":
        form =  CitasFormularios(request.POST, instance=cita)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = request.user
            cita.save()
            return redirect('citas.views.detalle_cita', pk=cita.pk)
    else:
        form = CitasFormularios(instance=cita)
    return render(request, 'citas/editar.html', {'form': form})
