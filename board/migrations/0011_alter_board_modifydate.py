# Generated by Django 5.0.7 on 2024-07-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_alter_board_modifydate_alter_board_registdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='modifyDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
