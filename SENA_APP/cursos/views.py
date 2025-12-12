from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Curso
from .forms import CursoForm

# Vistas de Función (Refactorizadas)
def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
    }
    return render(request, 'lista_cursos.html', context)

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    return render(request, 'detalle_curso.html', context)

# Vistas Basadas en Clases para CRUD
class CursoCreateView(CreateView):
    """Vista para crear un nuevo curso."""
    model = Curso
    form_class = CursoForm
    template_name = 'crear_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')

    def form_valid(self, form):
        messages.success(self.request, f'El curso "{form.instance.nombre}" ha sido creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)

class CursoUpdateView(UpdateView):
    """Vista para actualizar un curso."""
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'curso_id'

    def form_valid(self, form):
        messages.success(self.request, f'El curso "{form.instance.nombre}" ha sido actualizado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)

class CursoDeleteView(DeleteView):
    """Vista para eliminar un curso."""
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('cursos:lista_cursos')
    pk_url_kwarg = 'curso_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curso'] = self.get_object()
        return context

    def form_valid(self, form):
        messages.success(self.request, f'El curso "{self.get_object().nombre}" ha sido eliminado exitosamente.')
        return super().form_valid(form)