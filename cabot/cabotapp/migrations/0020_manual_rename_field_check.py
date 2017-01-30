# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        '0019_auto__add_field_shift_last_modified',
    ]

    operations = [
        migrations.RenameField('StatusCheckResult', 'check', 'status_check'),
    ]
