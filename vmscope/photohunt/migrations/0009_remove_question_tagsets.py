# Generated by Django 2.0.8 on 2019-11-22 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photohunt', '0008_question_tagset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tagsets',
        ),
    ]