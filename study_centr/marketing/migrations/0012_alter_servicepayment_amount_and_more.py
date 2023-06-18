# Generated by Django 4.2 on 2023-06-18 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0011_alter_servicepayment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepayment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='servicepayment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.service'),
        ),
        migrations.AlterField(
            model_name='servicepayment',
            name='service_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.serviceuser'),
        ),
    ]
