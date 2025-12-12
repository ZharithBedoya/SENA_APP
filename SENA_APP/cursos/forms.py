from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar cursos"""

    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'programa',
            'instructor_coordinador',
            'instructores',
            'aprendices',
            'fecha_inicio',
            'fecha_fin',
            'horario',
            'aula',
            'cupos_maximos',
            'estado',
            'observaciones',
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'programa': forms.Select(attrs={'class': 'form-select'}),
            'instructor_coordinador': forms.Select(attrs={'class': 'form-select'}),
            'instructores': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'aprendices': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'aula': forms.TextInput(attrs={'class': 'form-control'}),
            'cupos_maximos': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'instructor_coordinador': 'Instructor Coordinador',
            'cupos_maximos': 'Cupos Máximos',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Finalización',
        }
