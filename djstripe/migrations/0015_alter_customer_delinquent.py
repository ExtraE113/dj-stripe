# Generated by Django 3.2.10 on 2021-12-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0014_webhookendpoint"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="delinquent",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Whether or not the latest charge for the customer's latest invoice has failed.",
                null=True,
            ),
        ),
    ]
