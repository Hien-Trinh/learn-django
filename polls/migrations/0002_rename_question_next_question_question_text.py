# Generated by Django 5.0.7 on 2024-07-23 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_next',
            new_name='question_text',
        ),
    ]
