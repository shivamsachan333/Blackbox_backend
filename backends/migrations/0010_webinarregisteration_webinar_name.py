# Generated by Django 5.0.1 on 2024-01-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0009_community_webinarregisteration'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinarregisteration',
            name='Webinar_name',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
