# Generated by Django 4.0 on 2022-05-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_profilfoto_resim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilfoto',
            name='resim',
            field=models.ImageField(blank=True, default='profil_foto/default-profile.jpg', null=True, upload_to='profil_foto'),
        ),
    ]