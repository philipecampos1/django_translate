from django.db import models


class Tipos(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo
