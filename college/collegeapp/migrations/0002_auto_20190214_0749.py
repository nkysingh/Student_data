# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact_no',
            field=models.IntegerField(),
        ),
    ]
