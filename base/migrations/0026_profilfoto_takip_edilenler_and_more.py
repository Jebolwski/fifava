# Generated by Django 4.0 on 2022-07-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_profilfoto_takipciler'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilfoto',
            name='takip_edilenler',
            field=models.ManyToManyField(blank=True, default=None, related_name='takip_edilenler', to='base.ProfilFoto'),
        ),
        migrations.AlterField(
            model_name='profilfoto',
            name='takipciler',
            field=models.ManyToManyField(blank=True, default=None, related_name='takipciler', to='base.ProfilFoto'),
        ),
    ]
