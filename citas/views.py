from django.shortcuts import render

# Create your views here.
def listar_citas(request):
    return render(request, 'citas/listar.html', {})
