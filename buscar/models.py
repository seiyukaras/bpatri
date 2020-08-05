from django.db import models

# Create your models here.
class buscar(models.Model):
    fichero = models.TextField()
    tamanno = models.CharField(max_length=10, null=True, blank=False)

    def __str__(self):
    	return self.fichero