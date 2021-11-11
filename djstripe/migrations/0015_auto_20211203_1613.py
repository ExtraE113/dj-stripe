# Generated by Django 3.2.9 on 2021-12-03 16:13

from django.db import migrations
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0014_webhookeventtrigger_stripe_trigger_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='acss_debit',
            field=djstripe.fields.JSONField(blank=True, help_text='Additional information for payment methods of type `acss_debit`', null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='afterpay_clearpay',
            field=djstripe.fields.JSONField(blank=True, help_text='Additional information for payment methods of type `afterpay_clearpay`', null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='boleto',
            field=djstripe.fields.JSONField(blank=True, help_text='Additional information for payment methods of type `boleto`', null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='grabpay',
            field=djstripe.fields.JSONField(blank=True, help_text='Additional information for payment methods of type `grabpay`', null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='wechat_pay',
            field=djstripe.fields.JSONField(blank=True, help_text='Additional information for payment methods of type `wechat_pay`', null=True),
        ),
    ]