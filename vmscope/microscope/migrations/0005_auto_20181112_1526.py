# Generated by Django 2.0.8 on 2018-11-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microscope', '0004_program_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
