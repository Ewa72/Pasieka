from django.contrib import admin
from .models import Miody

# Register your models here.

class MiodyAdmin(admin.ModelAdmin):
    list_display = ("rodzaj", "opis", "foto")
  
admin.site.register(Miody, MiodyAdmin)