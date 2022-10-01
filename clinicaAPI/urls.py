from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # path('login', views.login, name='login'),
    path('login', TokenObtainPairView.as_view(), name = 'login'),
    path('refresh', TokenRefreshView.as_view(), name = 'refresh'),
    path('getOnePaciente/<int:id>', views.getOnePaciente , name='getOnePaciente'),
    path('getAllPacientes', views.getAllPacientes, name='getAllPacientes'),
    path('newFamiliar', views.newFamiliar, name='newFamiliar'),
    path('newEnfermeroAuxiliar', views.newEnfermeroAuxiliar , name='newEnfermeroAuxiliar'),
    path('newPaciente', views.newPaciente, name='newPaciente'),
    path('newJefeEnfermeria', views.newJefeEnfermeria, name='newJefeEnfermeria'),
    path('newFamiliar', views.newFamiliar, name='newFamiliar'),
    path('newPersona', views.newPersona, name='newPersona'),
    path('newMedico', views.newMedico, name='medico'),
    path('updatePaciente/<int:id>', views.updatePaciente, name='updatePaciente'),
    path('updateMedico/<int:id>', views.updateMedico, name='updateMedico'),
    path('getAllMedico', views.getAllMedico, name='getAllMedico'),
]

