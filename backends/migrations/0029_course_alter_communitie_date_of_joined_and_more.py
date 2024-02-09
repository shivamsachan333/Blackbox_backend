# Generated by Django 5.0.1 on 2024-02-06 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0028_whatweoffer_long_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course_poster', models.ImageField(upload_to='course_posters/')),
            ],
        ),
        migrations.AlterField(
            model_name='communitie',
            name='date_of_joined',
            field=models.CharField(default='06022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='lead',
            name='date_of_joined',
            field=models.CharField(default='06022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='webinarregisteration',
            name='Webinar_time',
            field=models.CharField(default='06022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='webinarregisteration',
            name='date_of_registeration',
            field=models.CharField(default='06022024', max_length=20),
        ),
        migrations.CreateModel(
            name='CourseStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_structures', to='backends.course')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_details', to='backends.course')),
            ],
        ),
    ]
