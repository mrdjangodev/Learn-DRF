# Generated by Django 4.2 on 2023-06-18 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_alter_service_teacher_alter_serviceusage_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='serviceusage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.serviceuser'),
        ),
    ]
