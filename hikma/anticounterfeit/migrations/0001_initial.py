# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 11:25
from __future__ import unicode_literals

import anticounterfeit.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityPK', models.AutoField(primary_key=True, serialize=False, verbose_name=b'City PK')),
                ('city', models.CharField(default=b'city', max_length=30, unique=True, verbose_name=b'City')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorPK', models.AutoField(primary_key=True, serialize=False, verbose_name=b'Doctor PK')),
                ('doctor', models.CharField(max_length=30, unique=True, verbose_name=b'Doctor')),
                ('cityFK', models.ForeignKey(on_delete=anticounterfeit.models.City, to='anticounterfeit.City')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('pharmacyPK', models.AutoField(primary_key=True, serialize=False, verbose_name=b'Pharmacy PK')),
                ('pharmacy', models.CharField(max_length=30, unique=True, verbose_name=b'Pharmacy')),
                ('cityFK', models.ForeignKey(on_delete=anticounterfeit.models.City, to='anticounterfeit.City')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productPK', models.AutoField(primary_key=True, serialize=False, verbose_name=b'Product PK')),
                ('product', models.CharField(max_length=20, unique=True, verbose_name=b'Product')),
            ],
        ),
        migrations.CreateModel(
            name='publicCode',
            fields=[
                ('publicCodePK', models.AutoField(primary_key=True, serialize=False, verbose_name=b'Public Code PK')),
                ('publicCode', models.BigIntegerField(unique=True, verbose_name=b'Public Code')),
                ('active', models.BooleanField(default=False, verbose_name=b'Active')),
                ('productFK', models.ForeignKey(on_delete=anticounterfeit.models.Product, to='anticounterfeit.Product')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('statePK', models.AutoField(primary_key=True, serialize=False, verbose_name=b'State PK')),
                ('state', models.CharField(max_length=20, unique=True, verbose_name=b'State')),
            ],
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('userCodePK', models.AutoField(primary_key=True, serialize=False, verbose_name=b'User Code PK')),
                ('userCode', models.BigIntegerField(unique=True, verbose_name=b'User Code')),
                ('active', models.BooleanField(default=False, verbose_name=b'Active')),
                ('productFK', models.ForeignKey(on_delete=anticounterfeit.models.Product, to='anticounterfeit.Product')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='stateFK',
            field=models.ForeignKey(on_delete=anticounterfeit.models.State, to='anticounterfeit.State'),
        ),
        migrations.AlterUniqueTogether(
            name='pharmacy',
            unique_together=set([('pharmacy', 'cityFK')]),
        ),
        migrations.AlterUniqueTogether(
            name='doctor',
            unique_together=set([('doctor', 'cityFK')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('city', 'stateFK')]),
        ),
    ]
