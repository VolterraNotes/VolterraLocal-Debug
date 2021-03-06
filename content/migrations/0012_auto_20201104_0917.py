# Generated by Django 3.0.8 on 2020-11-04 09:17

import content.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20201104_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='file_audio',
            field=models.FileField(blank=True, null=True, upload_to='audio/', validators=[content.validators.validate_ext_audio]),
        ),
        migrations.AlterField(
            model_name='nota',
            name='file_pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf', validators=[content.validators.validate_ext_pdf]),
        ),
        migrations.AlterField(
            model_name='nota',
            name='immagine',
            field=models.ImageField(blank=True, null=True, upload_to='notes/', validators=[content.validators.validate_ext_image]),
        ),
    ]
