# Generated by Django 4.0 on 2022-02-16 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_sorular_baslik'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='sorular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.sorular'),
        ),
    ]
