from django.shortcuts import render, get_object_or_404
from .models import Semestre, Curso


def index(request):
    semestres = Semestre.objects.all()  # Obtiene todos los semestres
    cursos = Curso.objects.all()  # Obtiene todos los cursos
    return render(request, 'index.html', {'semestres': semestres, 'cursos': cursos})

def cursos_por_semestre(request, semestre_id):
    semestre = get_object_or_404(Semestre, id=semestre_id)  
    cursos = semestre.cursos.all()  
    semestres = Semestre.objects.all()  # Asegúrate de obtener todos los semestres
    return render(request, 'cursos_por_semestre.html', {
        'semestre': semestre,
        'cursos': cursos,
        'semestres': semestres,  # Pasa la lista de semestres aquí
    })

def curso_detalle(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    semestre_id = curso.semestre.id  # Suponiendo que Curso tiene una relación con Semestre
    semestres = Semestre.objects.all()  # Asegúrate de obtener todos los semestres
    return render(request, 'curso_detalle.html', {
        'curso': curso,
        'semestre_id': semestre_id,  # Pasa el semestre_id a la plantilla
        'semestres': semestres,  # Pasa la lista de semestres aquí
    })
