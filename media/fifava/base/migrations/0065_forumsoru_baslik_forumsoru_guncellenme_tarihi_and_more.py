# Generated by Django 4.0 on 2022-03-23 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0064_alter_profilfoto_biyografi'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumsoru',
            name='baslik',
            field=models.CharField(default=4, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forumsoru',
            name='guncellenme_tarihi',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='forumsoru',
            name='olusturulma_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='forumsorucevap',
            name='soru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.forumsoru'),
        ),
    ]
