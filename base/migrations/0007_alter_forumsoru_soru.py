# Generated by Django 4.0 on 2022-04-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_kullanici_dosya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumsoru',
            name='soru',
            field=models.CharField(max_length=500),
        ),
    ]
