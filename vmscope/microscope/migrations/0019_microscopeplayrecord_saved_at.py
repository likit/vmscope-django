# Generated by Django 2.0.8 on 2020-03-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microscope', '0018_microscopeplayrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='microscopeplayrecord',
            name='saved_at',
            field=models.DateTimeField(null=True),
        ),
    ]