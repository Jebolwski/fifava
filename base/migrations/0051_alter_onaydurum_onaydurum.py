# Generated by Django 4.0 on 2022-03-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0050_onaydurum_kisi_delete_onayuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onaydurum',
            name='onaydurum',
            field=models.CharField(blank=True, choices=[('Kabul Et', 'Kabul Et'), ('Bekle', 'Bekle'), ('Reddet', 'Reddet'), ('Yasakla', 'Yasakla'), ('Cevapsız', 'Cevapsız')], max_length=8, null=True),
        ),
    ]