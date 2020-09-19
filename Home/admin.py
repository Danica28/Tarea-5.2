from django.contrib import admin
from .models import Estudiante,TipoEstudiante,Curso,Catedraticos

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(TipoEstudiante)
admin.site.register(Curso)
admin.site.register(Catedraticos)