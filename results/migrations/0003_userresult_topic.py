# Generated by Django 3.2.6 on 2021-12-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_userresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='topic',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
