from django.urls import path
from .views import index, cursos_por_semestre, curso_detalle
from django.conf import settings
from django.conf.urls.static import static

app_name = "software"
urlpatterns = [
    path('', index, name='index'), 
    path('cursos/<int:semestre_id>/', cursos_por_semestre, name='cursos_por_semestre'),  
    path('curso/<int:curso_id>/', curso_detalle, name='curso_detalle'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
