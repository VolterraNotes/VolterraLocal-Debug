# Generated by Django 3.0.8 on 2020-11-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20201103_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='file_audio',
            field=models.FileField(blank=True, upload_to='audio/'),
        ),
    ]
