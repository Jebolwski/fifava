# Generated by Django 4.0 on 2022-03-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0045_alter_cevaplar_baslik_slug_alter_sorular_baslik_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorular',
            name='onaydurum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.onaydurum'),
        ),
    ]
