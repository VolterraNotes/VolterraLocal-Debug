# Generated by Django 3.0.8 on 2020-11-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20201102_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='immagine',
            field=models.ImageField(blank=True, upload_to='notes/'),
        ),
    ]