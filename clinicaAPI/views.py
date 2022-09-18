import json
import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Familiar, Persona, Paciente, Medico, JefeEnfermeria, EnfermeroAuxiliar, Registro

def newFamiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            persona = Persona.objects.filter(id = data["personaId"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe persona con ese Id")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Paciente con ese Id")    
            
            familiar = Familiar(
                persona = persona,
                paciente = paciente,
                parentesco = data["parentesco"],
                email = data["email"],               
            )
            familiar.save()
            return HttpResponse("Nueva familiar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")


def newPersona(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona(
                id = data["id"],
                firstName = data["firstName"],
                lastName = data["lastName"],
                phone = data["phone"],
                gender = data["gender"],
            )
            persona.save()
            return HttpResponse("Nuevo cliente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def newRegistro(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Paciente con ese Id")    
            
            registro = Registro(
                paciente = paciente,
                diagnostico = data["diagnostico"],
                sugerencia = data["sugerencia"],
                historiaClinica = data["historiaClinica"]               
            )
            registro.save()
            return HttpResponse("Nueva registro agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def newPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pers = Persona.objects.filter(id = data["userID"]).first()
            if (not pers):
                return HttpResponseBadRequest("No existe cliente con esa cédula.")
            
            paciente = Paciente(
                persona = pers,
                address = data["address"],
                city = data["city"],
                birthday = data["birthday"],
                latitude = data["latitude"],
                longitud = data["longitud"],
            )
            paciente.save()
            return HttpResponse("Nueva cuenta agregada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")


def newJefeEnfermeria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pers = Persona.objects.filter(id = data["userID"]).first()
            if (not pers):
                return HttpResponseBadRequest("No existe cliente con esa cédula.")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Paciente con ese Id")
            registro = Registro.objects.filter(id = data["registroId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Registro con ese Id")

            jefeEnfermeria = JefeEnfermeria (
                persona = pers,
                paciente = paciente,
                registro = registro
            )    
            jefeEnfermeria .save()
            return HttpResponse("Nuevo médico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def newMedico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pers = Persona.objects.filter(id = data["userID"]).first()
            if (not pers):
                return HttpResponseBadRequest("No existe cliente con esa cédula.")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Paciente con ese Id")
            registro = Registro.objects.filter(id = data["registroId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Registro con ese Id")

            medico = Medico (
                persona = pers,
                paciente = paciente,
                registro = registro
            )    
            medico .save()
            return HttpResponse("Nuevo médico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def newEnfermeroAuxiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pers = Persona.objects.filter(id = data["userID"]).first()
            if (not pers):
                return HttpResponseBadRequest("No existe cliente con esa cédula.")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Paciente con ese Id")
            registro = Registro.objects.filter(id = data["registroId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe Registro con ese Id")

            enfermeroAuxiliar = EnfermeroAuxiliar (
                persona = pers,
                paciente = paciente,
                registro = registro
            )    
            enfermeroAuxiliar .save()
            return HttpResponse("Nuevo médico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAllPacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        if (not pacientes):
            return HttpResponseBadRequest("No hay pacientes en la base de datos.")

        personas = Persona.objects.all()
        if (not personas):
            return HttpResponseBadRequest("No hay personas en la base de datos.")

        allPacientesData = []
        for x,y in zip(pacientes,personas):
            data = {    
                    "id": x.id,
                    "firstName": y.firstName,
                    "lastName": y.lastName,
                    "phone": y.phone,
                    "gender": y.gender,
                    "address": x.address, 
                    "city": x.city, 
                    "birthday": x.birthday,
                    "latitude": x.latitude, 
                    "longitud": x.longitud
                        }
            allPacientesData.append(data)
        dataJson = json.dumps(allPacientesData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else: 
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getOnePaciente(request, id):
    if request.method == 'GET':
        paciente = Paciente.objects.filter(id = id).first()
        if (not paciente):
            return HttpResponseBadRequest("No existe paciente con esa cédula.")

        persona = Persona.objects.filter(paciente = id).first()
        if (not persona):
            return HttpResponseBadRequest("No existe paciente con esa cédula.")

        data = {
            "id": paciente.id,
            "firstName": persona.firstName, 
            "lastName": persona.lastName, 
            "phone": persona.phone, 
            "gender": persona.gender,
            "address": paciente.address,
            "city": paciente.city,
            "birthday":paciente.birthday
        }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
        