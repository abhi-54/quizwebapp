# Generated by Django 4.0.2 on 2022-08-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0006_alter_quiz_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects1',
            name='std',
            field=models.CharField(choices=[('0', '0'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('CET', 'CET'), ('JEE', 'JEE'), ('NEET', 'NEET'), ('Navodaya Vidyalaya', 'Navodaya Vidyalaya'), ('12 COMBO', '12COMBO')], default='', max_length=20),
        ),
    ]
