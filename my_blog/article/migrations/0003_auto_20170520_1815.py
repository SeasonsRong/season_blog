# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170519_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
    ]
