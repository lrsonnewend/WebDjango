from django.contrib import admin

#Importar classes
from .models import Campo, Atividade


# Register your models here.
admin.site.register(Campo)
admin.site.register(Atividade)