# Generated by Django 3.0.8 on 2020-09-29 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0005_auto_20200929_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='installer_appointment',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date_data',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='user_appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_appointment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]