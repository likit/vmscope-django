# Generated by Django 2.0.8 on 2019-12-09 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photohunt', '0011_auto_20191209_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, null=True)),
                ('title', models.TextField()),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='photohunt.Discipline')),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='discipline',
        ),
        migrations.AddField(
            model_name='session',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='photohunt.Program'),
            preserve_default=False,
        ),
    ]
