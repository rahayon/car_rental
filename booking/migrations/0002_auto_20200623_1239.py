# Generated by Django 3.0.7 on 2020-06-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingcar',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('paypal', 'PayPal'), ('payoneer', 'Payoneer'), ('visacard', 'Visa Card')], default='paypal', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='extrabenifit',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='extrabenifit',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
