# Generated by Django 2.0.8 on 2018-11-16 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181116_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='microscopeitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='microscopeitem',
            name='section',
        ),
        migrations.RemoveField(
            model_name='microscopesection',
            name='session',
        ),
        migrations.DeleteModel(
            name='MicroscopeItem',
        ),
        migrations.DeleteModel(
            name='MicroscopeSection',
        ),
    ]
