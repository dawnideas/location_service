# Generated by Django 2.1.3 on 2018-12-19 11:15

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('organization_uuid', models.UUIDField(verbose_name='Organization UUID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('address_line1', models.CharField(blank=True, max_length=255, verbose_name='Address line 1')),
                ('address_line2', models.CharField(blank=True, max_length=255, verbose_name='Address line 2')),
                ('address_line3', models.CharField(blank=True, max_length=255, verbose_name='Address line 3')),
                ('address_line4', models.CharField(blank=True, max_length=255, verbose_name='Address line 4')),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=85)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('administrative_level1', models.CharField(blank=True, max_length=255, verbose_name='Administrative division (First level)')),
                ('administrative_level2', models.CharField(blank=True, max_length=255, verbose_name='Administrative division (Second level)')),
                ('administrative_level3', models.CharField(blank=True, max_length=255, verbose_name='Administrative division (Third level)')),
                ('administrative_level4', models.CharField(blank=True, max_length=255, verbose_name='Administrative division (Fourth level)')),
                ('latitude', models.DecimalField(decimal_places=16, default=Decimal('0.00'), help_text='Latitude (Decimal Coordinates)', max_digits=25)),
                ('longitude', models.DecimalField(decimal_places=16, default=Decimal('0.00'), help_text='Longitude (Decimal Coordinates)', max_digits=25)),
                ('notes', models.TextField(blank=True)),
                ('organization_uuid', models.UUIDField(verbose_name='Organization UUID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('profiletype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.ProfileType')),
            ],
        ),
    ]
