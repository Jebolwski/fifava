# Generated by Django 4.0 on 2022-03-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_alter_sorular_onay1_alter_sorular_onay2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='onaydurum',
            name='guncellenme_tarihi',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='onaydurum',
            name='olusturulma_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='onaydurum',
            name='onaydurum',
            field=models.CharField(blank=True, choices=[('Kabul Et', 'Kabul Et'), ('Bekle', 'Bekle'), ('Reddet', 'Reddet')], max_length=8, null=True),
        ),
    ]
