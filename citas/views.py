from django.shortcuts import render, get_object_or_404
from .models import Citar
from django.utils import timezone

# Create your views here.
def listar_citas(request):
    citasprogramadas = Citar.objects.filter(realizada=False, fecha_cita__lte=timezone.now())#.order_by('fecha_cita'))
    return render(request, 'citas/listar.html', {'citas': citasprogramadas})

def detalle_cita(request, pk):
    cit = get_object_or_404(Citar, pk=pk)
    return render(request, 'citas/detalle.html', {'cita': cit})
