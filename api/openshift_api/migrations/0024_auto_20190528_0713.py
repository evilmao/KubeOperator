# Generated by Django 2.1.2 on 2019-05-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0023_auto_20190527_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployexecution',
            name='current_play',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
    ]
