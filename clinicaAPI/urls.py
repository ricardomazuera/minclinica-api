
from django.urls import path
from . import views

urlpatterns = [
    path('getOnePaciente/<int:id>', views.getOnePaciente , name='getOnePaciente'),
    path('getAllPacientes', views.getAllPacientes, name='getAllPacientes'),
    path('newFamiliar', views.newFamiliar, name='newFamiliar'),
    path('newEnfermeroAuxiliar', views.newEnfermeroAuxiliar , name='newEnfermeroAuxiliar'),
    path('newRegistro', views.newRegistro , name='newRegistro'),
    path('newPaciente', views.newPaciente, name='newPaciente'),
    path('newJefeEnfermeria', views.newJefeEnfermeria, name='newJefeEnfermeria'),
    path('newFamiliar', views.newFamiliar, name='newFamiliar'),
    path('newPersona', views.newPersona, name='newPersona'),
    path('newMedico', views.newMedico, name='medico'),
]

