# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citar',
            name='realizada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='citar',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
