# Generated by Django 4.1.7 on 2023-03-26 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
