# Generated by Django 2.1 on 2018-08-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180803_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='body',
            field=models.TextField(blank=True, max_length=1028),
        ),
    ]