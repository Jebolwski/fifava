# Generated by Django 4.0 on 2022-03-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0079_alter_forumsorucevap_cevaba_cevap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumsorucevap',
            name='cevaba_cevap',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
