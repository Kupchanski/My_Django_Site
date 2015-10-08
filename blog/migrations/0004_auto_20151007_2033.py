# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_sighup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighup',
            name='full_name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
