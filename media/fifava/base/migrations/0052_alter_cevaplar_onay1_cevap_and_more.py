# Generated by Django 4.0 on 2022-03-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0051_alter_onaydurum_onaydurum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevaplar',
            name='onay1_cevap',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cevaplar',
            name='onay2_cevap',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cevaplar',
            name='onay3_cevap',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cevaplar',
            name='onay4_cevap',
            field=models.BooleanField(default=False),
        ),
    ]
