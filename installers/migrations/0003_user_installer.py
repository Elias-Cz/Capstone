# Generated by Django 3.0.8 on 2020-09-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0002_date_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='installer',
            field=models.BooleanField(default=False),
        ),
    ]