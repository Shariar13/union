# Generated by Django 3.1.2 on 2021-08-23 17:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210823_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
