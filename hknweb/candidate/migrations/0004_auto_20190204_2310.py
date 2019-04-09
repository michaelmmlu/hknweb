# Generated by Django 2.1.5 on 2019-02-04 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_auto_20190204_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offchallenge',
            name='officer',
            field=models.ForeignKey(default=None, limit_choices_to={'groups__name': 'officer'}, on_delete=django.db.models.deletion.CASCADE, related_name='officer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offchallenge',
            name='requester',
            field=models.ForeignKey(default=None, limit_choices_to={'groups__name': 'candidate'}, on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL),
        ),
    ]