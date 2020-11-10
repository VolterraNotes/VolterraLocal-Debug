from django.db import models
import core.models
from django.utils import timezone
from .validators import validate_ext_image, validate_ext_pdf, validate_ext_audio

# Create your models here.

class Classe(models.Model):
    grado = models.IntegerField()

    def __str__(self):
        return str(self.grado)+"a"

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classi"

class Materia(models.Model):
    nome = models.CharField(max_length=60)
    classi = models.ManyToManyField(Classe)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materie"


class Professore(models.Model):
    nome = models.CharField(max_length=60)
    cognome = models.CharField(max_length=60)
    materie = models.ManyToManyField(Materia)
    classi = models.ManyToManyField(Classe, blank=True, related_name="profs")

    def __str__(self):
        self.materia_list = [i.nome for i in self.materie.all()]
        return self.nome + " " + self.cognome + ", " + str(self.materia_list)

    class Meta:
        verbose_name = "Professore"
        verbose_name_plural = "Professori"

class Nota(models.Model):
    titolo = models.CharField(max_length=60)
    professore = models.ForeignKey(Professore, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    studente = models.ForeignKey("core.CustomUser", on_delete=models.CASCADE, related_name="appunti", blank=True, null=True)
    immagine = models.ImageField(upload_to="notes/", validators=[validate_ext_image], blank=True)
    file_pdf = models.FileField(upload_to='pdf/', validators=[validate_ext_pdf], blank=True)
    file_audio = models.FileField(upload_to="audio/", validators=[validate_ext_audio], blank=True)
    data_pubblicazione = models.DateTimeField(auto_now_add=True)
    utile = models.IntegerField(default=0)
    non_utile = models.IntegerField(default=0)
    votanti = models.ManyToManyField("core.CustomUser", blank=True, related_name="note_votate")
    segnalanti = models.ManyToManyField("core.CustomUser", blank=True, related_name="note_segnalate")

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Note"

    def __str__(self):
        return self.titolo + ", " + self.materia.nome


class Segnalazione(models.Model):
    motivazioni = (
        ("Linguaggio Scurrile","Linguaggio Scurrile"),
        ("Contenuti Violenti","Contenuti Violenti"),
        ("Contenuti non inerenti allo studio","Contenuti non inerenti allo studio"),
        ("Contenuti illeggibili","Contenuti illeggibili"),
        ("Materiale illecito/inadatto al contesto","Materiale illecito/inadatto al contesto"),
        ("Contenuto irriverente e di cattivo gusto","Contenuto irriverente e di cattivo gusto")
        )

    motivo = models.CharField(max_length=60, choices=motivazioni, default="linguaggio scurrile")
    nota = models.ForeignKey(Nota, on_delete=models.DO_NOTHING, related_name="segnalazioni")
    user = models.ForeignKey("core.CustomUser", on_delete=models.DO_NOTHING, related_name="segnalazioni")
    messaggio = models.TextField(default="")

    class Meta:
        verbose_name = "segnalazione"
        verbose_name_plural = "segnalazioni"

    def __str__(self):
        return self.user.username + " a '" + self.nota.titolo + "' per " + self.motivo
