# Generated by Django 3.0.3 on 2020-03-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(default='tiguo')),
                ('start_time', models.TextField(default='0')),
                ('road_type', models.TextField(default='')),
                ('gps_lag', models.FloatField(default=0)),
                ('gps_long', models.FloatField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('car', models.IntegerField(default=0)),
                ('bike', models.IntegerField(default=0)),
                ('man', models.IntegerField(default=0)),
            ],
        ),
    ]