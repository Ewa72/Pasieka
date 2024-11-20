from django import forms

from .models import Miody

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Miody
        fields = ('miody_foto',)