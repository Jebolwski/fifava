# Generated by Django 4.0 on 2022-02-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_basik_haberler_baslik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soru1', models.TextField(blank=True, max_length=50, null=True)),
                ('soru2', models.TextField(blank=True, max_length=50, null=True)),
                ('soru3', models.TextField(blank=True, max_length=50, null=True)),
                ('soru4', models.TextField(blank=True, max_length=50, null=True)),
                ('soru5', models.TextField(blank=True, max_length=50, null=True)),
                ('soru6', models.TextField(blank=True, max_length=50, null=True)),
                ('soru7', models.TextField(blank=True, max_length=50, null=True)),
                ('soru8', models.TextField(blank=True, max_length=50, null=True)),
                ('soru9', models.TextField(blank=True, max_length=50, null=True)),
                ('soru10', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]