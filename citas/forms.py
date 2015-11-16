from django import forms
from .models import Citar

class CitasFormularios(forms.ModelForm):
    class Meta:
        model = Citar
        fields = ('paciente', 'edad','tipo_cita','descripcion_malestar', 'fecha_cita', 'medico', 'realizada',)
