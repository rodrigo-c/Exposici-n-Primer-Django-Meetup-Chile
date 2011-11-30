from django.db import models

# Create your models here.
from django.db.models import permalink

class Participante(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='uploads/participante')
    votos = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nombre

    @permalink
    def get_absolute_url(self):
        return ('votar', str(self.id))

    class Meta:
        ordering = ['-votos']
    
class Pareja(models.Model):
    participante1 = models.ForeignKey(Participante, related_name='pareja1')
    participante2 = models.ForeignKey(Participante, related_name='pareja2')
    comenatario = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s - %s" % (self.participante1, self.participante2)

