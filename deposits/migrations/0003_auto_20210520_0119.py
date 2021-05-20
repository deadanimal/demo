# Generated by Django 3.2.3 on 2021-05-20 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0002_auto_20210515_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='bank_account',
        ),
        migrations.AddField(
            model_name='deposit',
            name='circle_account_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='circle_iban_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='circle_routing_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='circle_wire_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='deposit',
            name='user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
    ]
