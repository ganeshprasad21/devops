# Generated by Django 5.1.6 on 2025-02-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_type', models.CharField(choices=[('CPU', 'CPU Usage'), ('Memory', 'Memory Usage'), ('Disk', 'Disk Usage'), ('Network', 'Network Traffic')], max_length=20)),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
