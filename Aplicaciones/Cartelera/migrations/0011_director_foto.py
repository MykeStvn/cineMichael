# Generated by Django 4.0.6 on 2024-06-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0010_remove_director_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='directores'),
        ),
    ]
