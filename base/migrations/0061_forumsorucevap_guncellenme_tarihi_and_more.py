# Generated by Django 4.0 on 2022-03-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0060_profilfoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumsorucevap',
            name='guncellenme_tarihi',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='forumsorucevap',
            name='olusturulma_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profilfoto',
            name='guncellenme_tarihi',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='profilfoto',
            name='olusturulma_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]