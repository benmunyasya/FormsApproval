# Generated by Django 4.0.5 on 2022-08-30 12:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0021_rename_ict_remarks_email_request_process_it_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_request_process',
            name='full_name',
            field=models.CharField(default=datetime.datetime(2022, 8, 30, 12, 56, 15, 888265, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
