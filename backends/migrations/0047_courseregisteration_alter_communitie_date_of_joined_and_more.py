# Generated by Django 5.0.1 on 2024-02-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0046_alter_webinar_date_alter_webinar_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseRegisteration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=500)),
                ('course_time', models.CharField(default='08022024', max_length=20)),
                ('course_author', models.CharField(default='not able to get', max_length=20)),
                ('full_name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('years_of_trading_experience', models.CharField(max_length=3)),
                ('date_of_registeration', models.CharField(default='08022024', max_length=20)),
                ('parmas', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='communitie',
            name='date_of_joined',
            field=models.CharField(default='08022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='lead',
            name='date_of_joined',
            field=models.CharField(default='08022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='webinarregisteration',
            name='Webinar_time',
            field=models.CharField(default='08022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='webinarregisteration',
            name='date_of_registeration',
            field=models.CharField(default='08022024', max_length=20),
        ),
    ]
