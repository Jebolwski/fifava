# Generated by Django 4.0 on 2022-04-10 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumSoru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=250)),
                ('baslik_slug', models.SlugField(unique=True)),
                ('soru', models.CharField(max_length=1000)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Haberler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=30)),
                ('baslik_slug', models.SlugField(unique=True)),
                ('aciklama', models.TextField(blank=True, max_length=250, null=True)),
                ('resim', models.ImageField(blank=True, null=True, upload_to='haberler')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Iletisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_soyad', models.CharField(max_length=100)),
                ('baslik', models.CharField(max_length=100)),
                ('aciklama', models.TextField(blank=True, max_length=1000, null=True)),
                ('dosya', models.ImageField(blank=True, null=True, upload_to='iletisim')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Kullanici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oyun_ad_soyad', models.CharField(max_length=25)),
                ('oyun_ad_soyad_slug', models.SlugField(unique=True)),
                ('meslek', models.CharField(max_length=25)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OnayDurum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onaydurum', models.CharField(blank=True, choices=[('Kabul Et', 'Kabul Et'), ('Bekle', 'Bekle'), ('Reddet', 'Reddet'), ('Yasakla', 'Yasakla'), ('Cevapsız', 'Cevapsız')], max_length=8, null=True)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('kisi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Sorular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=60)),
                ('baslik_slug', models.SlugField(blank=True, null=True, unique=True)),
                ('soru1', models.TextField(blank=True, max_length=200, null=True)),
                ('soru2', models.TextField(blank=True, max_length=200, null=True)),
                ('soru3', models.TextField(blank=True, max_length=200, null=True)),
                ('soru4', models.TextField(blank=True, max_length=200, null=True)),
                ('soru5', models.TextField(blank=True, max_length=200, null=True)),
                ('soru6', models.TextField(blank=True, max_length=200, null=True)),
                ('soru7', models.TextField(blank=True, max_length=200, null=True)),
                ('soru8', models.TextField(blank=True, max_length=200, null=True)),
                ('soru9', models.TextField(blank=True, max_length=200, null=True)),
                ('soru10', models.TextField(blank=True, max_length=200, null=True)),
                ('soru11', models.TextField(blank=True, max_length=200, null=True)),
                ('soru12', models.TextField(blank=True, max_length=200, null=True)),
                ('soru13', models.TextField(blank=True, max_length=200, null=True)),
                ('soru14', models.TextField(blank=True, max_length=200, null=True)),
                ('soru15', models.TextField(blank=True, max_length=200, null=True)),
                ('soru16', models.TextField(blank=True, max_length=200, null=True)),
                ('soru17', models.TextField(blank=True, max_length=200, null=True)),
                ('soru18', models.TextField(blank=True, max_length=200, null=True)),
                ('onay1', models.CharField(blank=True, max_length=120, null=True)),
                ('onay2', models.CharField(blank=True, max_length=120, null=True)),
                ('onay3', models.CharField(blank=True, max_length=120, null=True)),
                ('onay4', models.CharField(blank=True, max_length=120, null=True)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('onaydurum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.onaydurum')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=160, null=True)),
                ('username_slug', models.CharField(blank=True, max_length=160, null=True)),
                ('biyografi', models.CharField(blank=True, max_length=160, null=True)),
                ('resim', models.ImageField(blank=True, null=True, upload_to='profil_foto')),
                ('arka_plan', models.ImageField(blank=True, null=True, upload_to='arka_plan')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Iletisim_cevap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('cevap', models.TextField(max_length=600)),
                ('iletisim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.iletisim')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='ForumSoruCevap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cevap', models.CharField(max_length=1000)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('cevaba_cevap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.forumsorucevap')),
                ('dislikes', models.ManyToManyField(blank=True, default=None, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('profil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.profilfoto')),
                ('soru', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.forumsoru')),
            ],
        ),
        migrations.AddField(
            model_name='forumsoru',
            name='profil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.profilfoto'),
        ),
        migrations.CreateModel(
            name='Cevaplar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=60)),
                ('baslik_slug', models.SlugField(blank=True, null=True, unique=True)),
                ('soru1_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru2_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru3_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru4_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru5_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru6_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru7_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru8_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru9_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru10_cevap', models.CharField(blank=True, choices=[('1', 'Kesinlikle Katılmıyorum'), ('2', 'Katılmıyorum'), ('3', 'Kararsızım'), ('4', 'Katılıyorum'), ('5', 'Kesinlikle Katılıyorum')], max_length=5, null=True)),
                ('soru11_cevap', models.TextField(blank=True, max_length=200, null=True)),
                ('soru12_cevap', models.TextField(blank=True, max_length=1000, null=True)),
                ('soru13_cevap', models.TextField(blank=True, max_length=200, null=True)),
                ('soru14_cevap', models.TextField(blank=True, max_length=200, null=True)),
                ('soru15_cevap', models.TextField(blank=True, max_length=200, null=True)),
                ('soru16_cevap', models.TextField(blank=True, max_length=200, null=True)),
                ('soru17_cevap', models.TextField(blank=True, max_length=500, null=True)),
                ('soru18_cevap', models.TextField(blank=True, max_length=200, null=True)),
                ('onay1_cevap', models.BooleanField(default=False)),
                ('onay2_cevap', models.BooleanField(default=False)),
                ('onay3_cevap', models.BooleanField(default=False)),
                ('onay4_cevap', models.BooleanField(default=False)),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True, null=True)),
                ('kayitli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('sorular', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.sorular')),
            ],
        ),
    ]
