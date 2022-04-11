# Generated by Django 4.0 on 2022-03-21 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0059_alter_iletisim_aciklama_forumsorucevap_forumsoru'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(blank=True, null=True, upload_to='profil_foto')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]