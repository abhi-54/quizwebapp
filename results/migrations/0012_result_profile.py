# Generated by Django 4.0.2 on 2022-09-06 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regester', '0010_alter_profile1_user'),
        ('results', '0011_result_result_summary_alter_result_date1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='profile',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='regester.profile1'),
        ),
    ]
