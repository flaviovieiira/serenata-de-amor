# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamber_of_deputies', '0002_remove_django_simple_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reimbursement',
            name='available_in_latest_dataset',
        ),
    ]
