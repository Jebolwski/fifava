# Generated by Django 4.0 on 2022-07-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_hareketler'),
    ]

    operations = [
        migrations.AddField(
            model_name='hareketler',
            name='admin_mi',
            field=models.TextField(default=0, max_length=1),
        ),
    ]