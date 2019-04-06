# Generated by Django 2.1.7 on 2019-03-31 14:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0012_auto_20190331_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_contrib',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='event_contrib',
            unique_together={('user', 'event_id', 'company_name')},
        ),
    ]
