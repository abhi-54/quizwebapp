# Generated by Django 3.2.6 on 2021-12-13 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_typeofquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='typeOfquestion',
            new_name='type_of_question',
        ),
    ]
