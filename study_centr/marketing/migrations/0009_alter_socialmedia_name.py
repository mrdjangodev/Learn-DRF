# Generated by Django 4.2 on 2023-06-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_alter_socialmedia_effect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
