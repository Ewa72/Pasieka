from django.db import models

# Create your models here.
class Miody(models.Model):
    rodzaj = models.CharField(max_length=255)
    opis = models.CharField(max_length=1000)
    foto = models.ImageField(upload_to = 'miody/')
    
def __str__(self):
    return f"{self.rodzaj} {self.opis} {self.foto}"    