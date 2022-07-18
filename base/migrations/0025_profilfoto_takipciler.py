# Generated by Django 4.0 on 2022-07-05 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0024_cevaplar_soru19_cevap_sorular_soru19'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilfoto',
            name='takipciler',
            field=models.ManyToManyField(blank=True, default=None, related_name='takipciler', to=settings.AUTH_USER_MODEL),
        ),
    ]