from django.contrib import admin
from models import *

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nombre','votos']
    list_editable = ['votos']

admin.site.register(Participante, ParticipanteAdmin)

admin.site.register(Pareja)
