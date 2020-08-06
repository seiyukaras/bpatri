from django.db import models

# Create your models here.
class buscar(models.Model):
    nombre = models.TextField(default='')
    fichero = models.TextField()
    formato = models.CharField(max_length=20, default="Video")
    tamanno = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
    	return self.fichero