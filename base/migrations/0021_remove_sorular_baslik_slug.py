# Generated by Django 4.0 on 2022-06-04 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_remove_forumsoru_baslik_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sorular',
            name='baslik_slug',
        ),
    ]
