# Generated by Django 2.0.8 on 2020-03-26 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microscope', '0017_parasitepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MicroscopePlayRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microscope.MicroscopeSection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
