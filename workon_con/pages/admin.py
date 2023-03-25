from django.contrib import admin
from . models import Contact 
from . models import Proje

admin.site.register(Contact)

@admin.register(Proje)
class ProjeAdmin(admin.ModelAdmin):
    list_display = ('name' , 'available')
    list_filter = ('available',)
    search_fields = ('name',)