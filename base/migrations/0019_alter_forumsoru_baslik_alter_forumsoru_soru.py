# Generated by Django 4.0 on 2022-05-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_remove_forumsoru_yanit_sayi_alter_haberler_aciklama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumsoru',
            name='baslik',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forumsoru',
            name='soru',
            field=models.TextField(max_length=1000),
        ),
    ]