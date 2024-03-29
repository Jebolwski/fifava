# Generated by Django 4.0 on 2022-03-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_haberler_baslik_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cevaplar',
            name='baslik_slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sorular',
            name='baslik_slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
