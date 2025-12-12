from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from datetime import date # Import date
from .models import Programa
from .forms import ProgramaForm

# Vistas de Función (Refactorizadas)

def programas(request):
    lista_programas = Programa.objects.all()
    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return render(request, 'lista_programa.html', context)

def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, pk=programa_id)
    context = {
        'programa': programa,
    }
    return render(request, 'detalle_programa.html', context)

# Vistas Basadas en Clases para CRUD

class ProgramaCreateView(CreateView):
    """Vista para crear un nuevo programa."""
    model = Programa
    form_class = ProgramaForm
    template_name = 'crear_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    
    def form_valid(self, form):
        form.instance.fecha_creacion = date.today() # Set fecha_creacion to current date
        messages.success(
            self.request,
            f'El programa "{form.instance.nombre}" ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class ProgramaUpdateView(UpdateView):
    """Vista para actualizar un programa existente."""
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    pk_url_kwarg = 'programa_id'

    def form_valid(self, form):
        messages.success(
            self.request,
            f'El programa "{form.instance.nombre}" ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class ProgramaDeleteView(DeleteView):
    """Vista para eliminar un programa."""
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')
    pk_url_kwarg = 'programa_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programa'] = self.get_object()
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            f'El programa "{self.get_object().nombre}" ha sido eliminado exitosamente.'
        )
        return super().form_valid(form)
