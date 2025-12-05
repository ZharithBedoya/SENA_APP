from django.contrib import admin
from .models import Curso
from.models import InstructorCurso
from .models import AprendizCurso

admin.site.register(Curso)
admin.site.register(InstructorCurso)
admin.site.register(AprendizCurso)
# Register your models here.
