# Generated by Django 4.0 on 2022-04-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_forumsoru_soru'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='hikayesi',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='meslek',
            field=models.CharField(max_length=40),
        ),
    ]