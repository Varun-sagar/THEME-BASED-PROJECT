# Generated by Django 2.1.7 on 2019-02-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='feature',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
