from django.contrib import admin
from .models import Miody
from django.utils.html import format_html # do wyswietlenia foto

# Register your models here.

#class ImageAdmin(admin.ModelAdmin):


class MiodyAdmin(admin.ModelAdmin):
 
   def image_tag(self, obj):
       return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.foto.url)) # wyswietlane zdj miodu
   
   image_tag.short_description = 'foto'
   
   list_display = ("rodzaj", "opis", "foto", 'image_tag',)
    
    
  
admin.site.register(Miody, MiodyAdmin)#, ImageAdmin)