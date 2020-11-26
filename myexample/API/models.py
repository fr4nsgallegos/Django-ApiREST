from django.db import models

# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length = 200)

class Stand(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, blank = True, null=True, related_name="stands")
    nombre = models.CharField(max_length = 200)
    videoCarrera = models.TextField(blank=True, null=True)
    brochure = models.FileField(blank=True, null=True)
    infoCarrera = models.TextField(blank=True, null=True)
    imagen1 = models.ImageField(blank=True, null=True)

class Egresados(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, blank =True, null=True, related_name="egresados")
    video = models.TextField(blank=True, null= True)

class OrientacionVocacional(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, blank =True, null=True, related_name="orientacion")

class Webinars(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, blank =True, null=True, related_name="webinars")
    link_webinar = models.TextField(blank=True, null= True)

class Participante(models.Model):
    dni = models.CharField(max_length = 150, blank= True, null = True)
    nombres = models.CharField(max_length = 200,blank= True, null = True)
    apellidos = models.CharField(max_length = 200,blank= True, null = True)
    correo = models.CharField(max_length = 150)
    colegio = models.CharField(max_length = 150)

class Pregunta(models.Model):
    pregunta = models.TextField(max_length=200,blank= True, null = True)
    imagen = models.ImageField(blank= True, null = True)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="respuestas")
    respuesta = models.TextField(max_length=200, blank= True, null = True)
    imagen = models.ImageField(blank= True, null = True)
    correcta = models.BooleanField(default=False)

class RespuestaParticipante(models.Model):
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE,)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name = "participante_respuesta")
        
    
    
    
    
    
    
    
    

    
        
    
    
    
    

    
    

        