from django.db import models
from django.utils import timezone

class Film(models.Model):
    nom = models.CharField(max_length=128, default='Nom par défaut')
    description = models.TextField(max_length=2048)
    date_de_parution = models.DateField(default=timezone.now)
    note = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(6)])


    def __str__(self):
        return self.titre
