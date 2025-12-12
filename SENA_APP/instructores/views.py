from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages

from .models import Instructor
from .forms import InstructorForm

# Create your views here.

def instructores(request):
    lista_instructores = Instructor.objects.all() # Removed .values()
    
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return render(request, 'lista_instructores.html', context) # Using render shortcut

def detalle_instructor(request, id_instructor):
  instructor = get_object_or_404(Instructor, pk=id_instructor) # Using get_object_or_404
  context = {
    'instructor': instructor,
  }
  return render(request, 'detalle_instructores.html', context) # Using render shortcut

# Vistas Basadas en Clases (Corregidas)

class InstructorCreateView(CreateView):
    """Vista para crear un nuevo instructor."""
    model = Instructor
    form_class = InstructorForm
    template_name = 'crear_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorUpdateView(UpdateView):
    """Vista para actualizar un instructor existente."""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    # No se necesita pk_url_kwarg porque la URL ahora usa 'pk', que es el valor por defecto.
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorDeleteView(DeleteView):
    """Vista para eliminar un instructor."""
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    # No se necesita pk_url_kwarg porque la URL ahora usa 'pk'.
    
    def form_valid(self, form):
        # Usamos form_valid para añadir el mensaje de éxito antes de que se elimine el objeto.
        messages.success(
            self.request,
            f'El instructor {self.get_object().nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().form_valid(form)