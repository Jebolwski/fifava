# Generated by Django 4.0 on 2022-04-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_haberler_goruldu_iletisim_goruldu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='dosya',
            field=models.ImageField(blank=True, null=True, upload_to='oyuncu'),
        ),
    ]