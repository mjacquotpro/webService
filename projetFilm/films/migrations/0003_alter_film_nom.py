# Generated by Django 5.0.4 on 2024-04-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_remove_film_annee_remove_film_realisateur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='nom',
            field=models.CharField(default='Nom par défaut', max_length=128),
        ),
    ]