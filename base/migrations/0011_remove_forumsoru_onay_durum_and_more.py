# Generated by Django 4.0 on 2022-04-30 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_iletisim_dosya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumsoru',
            name='onay_durum',
        ),
        migrations.RemoveField(
            model_name='kullanici',
            name='hikayesi',
        ),
    ]
