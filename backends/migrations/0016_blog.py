# Generated by Django 5.0.1 on 2024-02-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0015_webinarregisteration_parmas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=200)),
                ('Title', models.CharField(max_length=800)),
                ('short_note', models.CharField(max_length=2000)),
                ('Description', models.TextField()),
                ('Tages', models.CharField(max_length=1000)),
            ],
        ),
    ]
