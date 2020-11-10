from django.core.exceptions import ValidationError
import os

def validate_ext_image(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg", ".png", ".heic"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Estensioni accettate: .jpg, .png")

def validate_ext_pdf(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".pdf, .doc", ".docx", ".pages"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Estensioni accettate: .pdf, .doc, .docx, .pages")

def validate_ext_audio(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".mp3"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Estensioni accettate: .mp3")
