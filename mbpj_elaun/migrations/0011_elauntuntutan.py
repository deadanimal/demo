# Generated by Django 3.2.3 on 2021-06-06 09:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mbpj_elaun', '0010_auto_20210606_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElaunTuntutan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nric', models.CharField(max_length=255, null=True)),
                ('kod_pekerja', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('elaun', models.ManyToManyField(null=True, to='mbpj_elaun.Elaun')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
