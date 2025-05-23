# Generated by Django 3.2.3 on 2021-06-14 23:50

from django.db import migrations, models
import helpers.general


class Migration(migrations.Migration):

    dependencies = [
        ('kpdnhep_eaduan', '0007_aduan_tugas'),
    ]

    operations = [
        migrations.AddField(
            model_name='bantuan',
            name='daripada_syarikat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bantuan',
            name='dokumen',
            field=models.FileField(null=True, upload_to=helpers.general.PathAndRename('enquiry-attached-document')),
        ),
        migrations.AddField(
            model_name='bantuan',
            name='jenis_bantuan',
            field=models.CharField(choices=[('A', 'Laporan Helpdesk'), ('B', 'Dokumen Pembangunan')], default='A', max_length=1),
        ),
    ]
