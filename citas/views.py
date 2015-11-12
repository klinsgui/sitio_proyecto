from django.shortcuts import render
from .models import Citar
from django.utils import timezone

# Create your views here.
def listar_citas(request):
    citasprogramadas = Citar.objects.filter(realizada=False, fecha_cita=timezone.now())#.order_by('fecha_cita'))
    return render(request, 'citas/listar.html', {'citas': citasprogramadas})
