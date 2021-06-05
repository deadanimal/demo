# Generated by Django 3.2.3 on 2021-06-05 12:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mbpj_elaun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elaun',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jenis_permohonan', models.CharField(max_length=255)),
                ('tarikh', models.CharField(max_length=255)),
                ('masa_mula', models.CharField(max_length=255)),
                ('masa_akhir', models.CharField(max_length=255)),
                ('sebab_lebih_masa', models.CharField(max_length=255)),
                ('lokasi', models.CharField(max_length=255)),
                ('pegawai_lulus', models.CharField(max_length=255)),
                ('pegawai_sah', models.CharField(max_length=255)),
                ('hari', models.CharField(max_length=255)),
                ('waktu', models.CharField(max_length=255)),
                ('kadar_jam', models.CharField(max_length=255)),
                ('tujuan', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ElaunPerson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nric', models.CharField(max_length=255)),
                ('kod_pekerja', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('elaun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbpj_elaun.elaun')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
