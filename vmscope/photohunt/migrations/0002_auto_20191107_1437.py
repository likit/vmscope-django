# Generated by Django 2.0.8 on 2019-11-07 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photohunt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageTagSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagsets', to='photohunt.Image')),
            ],
        ),
        migrations.AddField(
            model_name='imagetag',
            name='tagset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='photohunt.ImageTagSet'),
        ),
    ]
