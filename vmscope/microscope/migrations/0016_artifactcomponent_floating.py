# Generated by Django 2.0.8 on 2018-11-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microscope', '0015_artifactcomponent_resizable'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifactcomponent',
            name='floating',
            field=models.BooleanField(default=False),
        ),
    ]
