from django.db import models

# Create your models here.
class Miody(models.Model):
    rodzaj = models.CharField(max_length=255)
    opis = models.TextField(max_length=1000, help_text="Krótka charakterystyka typu miodu") # dla dłuższych opisów
    miody_foto = models.ImageField(upload_to = 'miody_foto', blank=True, null=True, default='miody_foto/spadz.jpg')
 

def __str__(self):
    return f"{self.rodzaj} {self.opis} {self.miody_foto}"    

