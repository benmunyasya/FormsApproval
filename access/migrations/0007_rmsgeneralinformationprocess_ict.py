# Generated by Django 4.0 on 2022-07-28 04:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0006_alter_rmsgeneralinformationprocess_temporary_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmsgeneralinformationprocess',
            name='ICT',
            field=models.CharField(choices=[('Systems Administrator', 'Systems Administrator'), ('Senior Management', 'Senior Management')], default=datetime.datetime(2022, 7, 28, 4, 37, 43, 110126, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
