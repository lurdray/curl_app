# Generated by Django 4.1.1 on 2022-10-05 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_photo', models.FileField(blank=True, default='default_files/default_face.jpg', upload_to='account_files/profile_photos/')),
                ('account_type', models.CharField(default='candidate', max_length=10)),
                ('cprofile_status', models.BooleanField(default=False)),
                ('cv', models.FileField(blank=True, default='default_files/default_face.jpg', upload_to='account_files/profile_photos/')),
                ('profile_photo', models.FileField(blank=True, default='default_files/default_face.jpg', upload_to='account_files/profile_photos/')),
                ('address', models.TextField(default=' ')),
                ('country', models.CharField(default=' ', max_length=100)),
                ('phone_no', models.CharField(default=' ', max_length=15)),
                ('age', models.IntegerField(default=18)),
                ('gender', models.CharField(default=' ', max_length=10)),
                ('facebook_link', models.CharField(default='#', max_length=100)),
                ('twitter_link', models.CharField(default='#', max_length=100)),
                ('instagram_link', models.CharField(default='#', max_length=100)),
                ('whatsapp_link', models.CharField(default='#', max_length=100)),
                ('github_link', models.CharField(default='#', max_length=100)),
                ('agency_name', models.CharField(default='', max_length=30, null=True)),
                ('rank', models.CharField(default='1', max_length=30, null=True)),
                ('ranks', models.CharField(default='1', max_length=30, null=True)),
                ('rankers', models.CharField(default='1', max_length=30, null=True)),
                ('charge', models.CharField(default='0', max_length=30, null=True)),
                ('bio', models.TextField(default='This agency have not updated their bio..')),
                ('agency_logo', models.FileField(blank=True, default='default_files/default_face.jpg', upload_to='account_files/profile_photos/')),
                ('otp_code', models.CharField(default='none', max_length=10)),
                ('ec_status', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('wallet_address', models.CharField(default='null', max_length=100)),
                ('wallet_key', models.CharField(default='null', max_length=100)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
