from django.contrib import admin


from .models import Curso
from .models import Semestre


admin.site.register(Curso)
admin.site.register(Semestre)

