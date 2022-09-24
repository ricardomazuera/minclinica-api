import json
import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Familiar, Persona, Paciente, Medico, JefeEnfermeria, EnfermeroAuxiliar


def newPersona(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona.objects.filter(id = data["personaId"]).first()
            if (persona):
                return HttpResponseBadRequest("Ya existe una persona con ese documento de identidad")
            else:
                persona = Persona(
                    id = data["personaId"],
                    firstName = data["firstName"],
                    lastName = data["lastName"],
                    phone = data["phone"],
                    gender = data["gender"],
                )
                persona.save()
            return HttpResponse("Nueva persona agregada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def newPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pers = Persona.objects.filter(id = data["personaId"]).first()
            if (not pers):
                return HttpResponseBadRequest("No existe persona con esa cédula.")

            paci = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (paci):
                return HttpResponseBadRequest("Ya existe un paciente con ese documento de identidad")
            else:            
                paciente = Paciente(
                    id = data["pacienteId"],
                    persona = pers,
                    address = data["address"],
                    city = data["city"],
                    birthday = data["birthday"],
                    latitude = data["latitude"],
                    longitud = data["longitud"],
                )
                paciente.save()
            return HttpResponse("Nuevo paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def newFamiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            persona = Persona.objects.filter(id = data["personaId"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe persona con esa cédula.")
            paciente = Paciente.objects.filter(id = data["pacienteId"]).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe paciente con esa identificación")    
        
            familiar = Familiar(
                    persona = persona,
                    paciente = paciente,
                    parentesco = data["parentesco"],
                    email = data["email"],               
                )
            familiar.save()
            return HttpResponse("Nuevo familiar agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def newMedico(request):
    if request.method == 'POST':
        # try:
            data = json.loads(request.body)
            pers = Persona.objects.filter(id = data["personaId"]).first()
            if (not pers):
                return HttpResponseBadRequest("No existe persona con esa cédula.")
               
            medi = Medico.objects.filter(id = data["medicoId"]).first()
            if (medi):
                return HttpResponseBadRequest("Ya existe un médico con ese documento de identidad")
            else:     
                medico = Medico (
                        id = data["personaId"],
                        persona = pers,
                        especialidad = data["especialidad"],
                        registro = data["registro"],
                    )    
                medico .save()
            return HttpResponse("Nuevo médico agregado")
        # except:
        #     return HttpResponseBadRequest("Error en los datos enviados")
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
           

            jefeEnfermeria = JefeEnfermeria (
                persona = pers,
                paciente = paciente
                
            )    
            jefeEnfermeria .save()
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
           
            enfermeroAuxiliar = EnfermeroAuxiliar (
                persona = pers,
                paciente = paciente,
              
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

        for x in pacientes:
            for y in personas:
                if x.id == y.id:
                    data = {    
                        "id": x.id,
                        "dni": y.id,
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
            "dni": persona.id,
            "firstName": persona.firstName, 
            "lastName": persona.lastName, 
            "phone": persona.phone, 
            "gender": persona.gender,
            "address": paciente.address,
            "city": paciente.city,
            "birthday":paciente.birthday,
            "latitude": paciente.latitude, 
            "longitud": paciente.longitud
        }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
        