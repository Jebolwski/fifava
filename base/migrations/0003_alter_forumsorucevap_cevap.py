# Generated by Django 4.0 on 2022-04-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_forumsoru_dislikes_forumsoru_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumsorucevap',
            name='cevap',
            field=models.CharField(max_length=200),
        ),
    ]