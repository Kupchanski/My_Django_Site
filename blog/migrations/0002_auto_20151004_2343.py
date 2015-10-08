# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикации')),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
