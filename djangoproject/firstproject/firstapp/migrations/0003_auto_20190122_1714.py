# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_empcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card', models.CharField(max_length=264)),
                ('name', models.ForeignKey(to='firstapp.WebPage')),
            ],
        ),
        migrations.RemoveField(
            model_name='empcontact',
            name='name',
        ),
        migrations.DeleteModel(
            name='EmpContact',
        ),
    ]
