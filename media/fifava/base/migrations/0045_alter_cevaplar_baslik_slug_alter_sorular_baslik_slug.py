# Generated by Django 4.0 on 2022-03-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_kullanici_oyun_ad_soyad_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevaplar',
            name='baslik_slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sorular',
            name='baslik_slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
