from django.contrib import admin

from API.models import *
'''
class StandInline(admin.StackedInline):
    model = Stand
    # Mostramos dos inlines vacíos por defecto
    extra = 2

class SedeAdmin(admin.ModelAdmin):
    # Registramos el inline en la persona
    inlines = [StandInline]'''

# Register your models here.
admin.site.register(Sede)
admin.site.register(Stand)
admin.site.register(Egresados)
admin.site.register(OrientacionVocacional)
admin.site.register(Webinars)
admin.site.register(Participante)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(RespuestaParticipante)