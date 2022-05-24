# Generated by Django 4.0.3 on 2022-05-24 07:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.UUID('75a8839c-42bf-4b89-8be9-d6a69afeab1d'), primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('joined_at', models.DateTimeField(blank=True, null=True)),
                ('mobile_number', models.CharField(max_length=12, unique=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SiteModel',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('3bb3abc8-852c-4a4a-8578-5b319e08b248'), primary_key=True, serialize=False)),
                ('street_name', models.CharField(max_length=1000)),
                ('village', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('district', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=1000)),
                ('location_coordinates', models.CharField(blank=True, max_length=1000, null=True)),
                ('type', models.CharField(blank=True, choices=[('Home', 'home'), ('Site', 'site')], max_length=30)),
                ('price', models.FloatField(blank=True, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('is_private', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
