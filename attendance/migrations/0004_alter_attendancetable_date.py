# Generated by Django 4.0.2 on 2022-06-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_remove_attendancetable_present_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancetable',
            name='date',
            field=models.DateField(help_text='Format: yyyy-mm-dd', null=True),
        ),
    ]
