# Generated by Django 4.2 on 2023-06-18 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0001_initial'),
        ('marketing', '0002_alter_interestor_found_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.teacher'),
        ),
        migrations.AlterField(
            model_name='serviceusage',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.service'),
        ),
        migrations.AlterField(
            model_name='serviceusage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
