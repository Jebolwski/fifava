# Generated by Django 4.0 on 2022-03-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_onaydurum_kisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorular',
            name='onay1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sorular',
            name='onay2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sorular',
            name='onay3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sorular',
            name='onay4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
