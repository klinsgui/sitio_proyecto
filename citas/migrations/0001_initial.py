# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Citar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=3)),
                ('tipo_cita', models.CharField(max_length=100)),
                ('descripcion_malestar', models.TextField()),
                ('fecha_reservacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_cita', models.DateTimeField(null=True, blank=True)),
                ('medico', models.CharField(max_length=200)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
