# Generated by Django 4.0.3 on 2022-03-04 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('street_name', models.CharField(max_length=1000)),
                ('village', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('district', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=1000)),
                ('location_coordinates', models.CharField(max_length=1000)),
                ('type', models.CharField(blank=True, choices=[('Home', 'home'), ('Site', 'site')], max_length=30)),
                ('price', models.FloatField(blank=True, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('is_private', models.BooleanField(default=False)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.user')),
            ],
        ),
    ]
