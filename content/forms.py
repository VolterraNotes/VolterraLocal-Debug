from django import forms
from .models import Nota, Segnalazione
from django.core.exceptions import ValidationError

class CreaNota(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ("titolo", "professore", "materia", "classe", "immagine")

class CreaNotaPDF(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ("titolo", "professore", "materia", "classe", "file_pdf")

class CreaNotaAudio(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ("titolo", "professore", "materia", "classe", "file_audio")

class FormSegnalazione(forms.ModelForm):

    class Meta:
        model = Segnalazione
        fields = ("motivo", "messaggio")
