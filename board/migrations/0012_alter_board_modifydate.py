# Generated by Django 5.0.7 on 2024-07-31 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_alter_board_modifydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='modifyDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
