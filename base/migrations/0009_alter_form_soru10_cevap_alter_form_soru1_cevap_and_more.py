# Generated by Django 4.0 on 2022-02-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_form_soru10_cevap_alter_form_soru1_cevap_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='soru10_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru1_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru2_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=128),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru3_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru4_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru5_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru6_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru7_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru8_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
        migrations.AlterField(
            model_name='form',
            name='soru9_cevap',
            field=models.CharField(choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=64),
        ),
    ]
