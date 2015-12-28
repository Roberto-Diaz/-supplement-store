# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('password', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('edad', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('precio', models.DecimalField(default=0.0, max_digits=7, decimal_places=2)),
                ('personal', models.ForeignKey(to='proyecto.Personal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ubicacion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.DecimalField(max_digits=7, decimal_places=2)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(to='proyecto.Cliente')),
                ('personal', models.ForeignKey(to='proyecto.Personal')),
                ('sucursal', models.ForeignKey(to='proyecto.Sucursal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productos',
            name='proveedor',
            field=models.ForeignKey(to='proyecto.Proveedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='sucursal',
            field=models.ForeignKey(to='proyecto.Sucursal'),
            preserve_default=True,
        ),
    ]
