# Generated by Django 3.1.7 on 2021-04-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]