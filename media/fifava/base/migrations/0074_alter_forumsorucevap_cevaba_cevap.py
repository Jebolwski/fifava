# Generated by Django 4.0 on 2022-03-26 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0073_alter_forumsorucevap_cevaba_cevap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumsorucevap',
            name='cevaba_cevap',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.forumsorucevap'),
            preserve_default=False,
        ),
    ]