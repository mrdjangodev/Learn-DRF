# Generated by Django 4.2 on 2023-06-13 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('students', '0002_studentpayment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentpayment',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Students Payments'},
        ),
        migrations.AddField(
            model_name='studentpayment',
            name='adminstrator',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.adminstrator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentpayment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentpayment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='studentpayment',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='students.student'),
            preserve_default=False,
        ),
    ]
