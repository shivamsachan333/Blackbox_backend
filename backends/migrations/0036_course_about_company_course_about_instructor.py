# Generated by Django 5.0.1 on 2024-02-07 06:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0035_alter_programdetail_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about_company',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='about_instructor',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
