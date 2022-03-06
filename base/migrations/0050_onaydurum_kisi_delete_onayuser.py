# Generated by Django 4.0 on 2022-03-06 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0049_remove_onaydurum_kisi'),
    ]

    operations = [
        migrations.AddField(
            model_name='onaydurum',
            name='kisi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.DeleteModel(
            name='OnayUser',
        ),
    ]
