from django.contrib import admin
from .models import Professore, Materia, Nota, Classe, Segnalazione

# Register your models here.
admin.site.register(Professore)
admin.site.register(Materia)
admin.site.register(Nota)
admin.site.register(Classe)
admin.site.register(Segnalazione)
