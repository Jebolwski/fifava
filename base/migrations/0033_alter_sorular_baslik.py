# Generated by Django 4.0 on 2022-02-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_alter_cevaplar_baslik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorular',
            name='baslik',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
