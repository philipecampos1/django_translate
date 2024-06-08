from django.db import models
from tipos.models import Tipos


# Create your models here.
class Traducoes(models.Model):
    tipo = models.ForeignKey(Tipos, on_delete=models.PROTECT)
    pt_br = models.TextField()
    en_gb = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pt_br
