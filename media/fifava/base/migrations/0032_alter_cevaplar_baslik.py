# Generated by Django 4.0 on 2022-02-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_cevaplar_baslik_alter_sorular_baslik_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevaplar',
            name='baslik',
            field=models.CharField(default=2, max_length=60, unique=True),
            preserve_default=False,
        ),
    ]