# Generated by Django 3.2.3 on 2021-06-04 06:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrnInterfaceInterface',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Header_Interface_Number', models.CharField(default='NA', max_length=255)),
                ('Receipt_Source_Code', models.CharField(default='NA', max_length=255)),
                ('Business_Unit', models.CharField(default='NA', max_length=255)),
                ('Receipt_Number', models.CharField(default='NA', max_length=255)),
                ('Supplier_Number', models.CharField(default='NA', max_length=255)),
                ('Supplier_Site_Code', models.CharField(default='NA', max_length=255)),
                ('Bill_Of_Lading', models.CharField(default='NA', max_length=255)),
                ('Packing_Slip', models.CharField(default='NA', max_length=255)),
                ('Carrier_Name', models.CharField(default='NA', max_length=255)),
                ('Waybill', models.CharField(default='NA', max_length=255)),
                ('Comments', models.CharField(default='NA', max_length=255)),
                ('Receiver_Name', models.CharField(default='NA', max_length=255)),
                ('Interface_Line_Number', models.CharField(default='NA', max_length=255)),
                ('Transaction_Type', models.CharField(default='NA', max_length=255)),
                ('Auto_Transact_Code', models.CharField(default='NA', max_length=255)),
                ('Transaction_Date', models.CharField(default='NA', max_length=255)),
                ('Source_Document_Code', models.CharField(default='NA', max_length=255)),
                ('Parent_Interface_Number', models.CharField(default='NA', max_length=255)),
                ('Organization_Code', models.CharField(default='NA', max_length=255)),
                ('Item_Number', models.CharField(default='NA', max_length=255)),
                ('Document_Number', models.CharField(default='NA', max_length=255)),
                ('Document_Line_Number', models.CharField(default='NA', max_length=255)),
                ('Document_Schedule_Number', models.CharField(default='NA', max_length=255)),
                ('Document_Distribution_Number', models.CharField(default='NA', max_length=255)),
                ('Subinventory', models.CharField(default='NA', max_length=255)),
                ('Quantity', models.CharField(default='NA', max_length=255)),
                ('UOM', models.CharField(default='NA', max_length=255)),
                ('Locator', models.CharField(default='NA', max_length=255)),
                ('Interface_Source_Code', models.CharField(default='NA', max_length=255)),
                ('Reason', models.CharField(default='NA', max_length=255)),
                ('Remarks', models.CharField(default='NA', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='InventoryTransactionInterface',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Organization_Name', models.CharField(default='NA', max_length=255)),
                ('Source_Code', models.CharField(default='NA', max_length=255)),
                ('Source_Header_Id', models.CharField(default='NA', max_length=255)),
                ('Source_Line_Id', models.CharField(default='NA', max_length=255)),
                ('Transaction_Date', models.CharField(default='NA', max_length=255)),
                ('Item_Number', models.CharField(default='NA', max_length=255)),
                ('Subinventory_Code', models.CharField(default='NA', max_length=255)),
                ('Locator_Rack', models.CharField(default='NA', max_length=255)),
                ('Locator_Row', models.CharField(default='NA', max_length=255)),
                ('Transaction_Quantity', models.CharField(default='NA', max_length=255)),
                ('Transaction_Uom', models.CharField(default='NA', max_length=255)),
                ('Transaction_Type_Name', models.CharField(default='NA', max_length=255)),
                ('Transaction_Reference', models.CharField(default='NA', max_length=255)),
                ('Dst_Segment1', models.CharField(default='NA', max_length=255)),
                ('Dst_Segment2', models.CharField(default='NA', max_length=255)),
                ('Dst_Segment3', models.CharField(default='NA', max_length=255)),
                ('Dst_Segment4', models.CharField(default='NA', max_length=255)),
                ('Dst_Segment5', models.CharField(default='NA', max_length=255)),
                ('Dst_Segment6', models.CharField(default='NA', max_length=255)),
                ('Dst_Segment7', models.CharField(default='NA', max_length=255)),
                ('Use_Current_Cost', models.CharField(default='NA', max_length=255)),
                ('Transaction_Cost_Identifier', models.CharField(default='NA', max_length=255)),
                ('Cost_Component_Code', models.CharField(default='NA', max_length=255)),
                ('Cost', models.CharField(default='NA', max_length=255)),
                ('Serial_Num_Identifier', models.CharField(default='NA', max_length=255)),
                ('From_Serial_Num', models.CharField(default='NA', max_length=255)),
                ('To_Serial_Num', models.CharField(default='NA', max_length=255)),
                ('Destination_Organization', models.CharField(default='NA', max_length=255)),
                ('Destination_Subinventory', models.CharField(default='NA', max_length=255)),
                ('Dest_Locator_Rack', models.CharField(default='NA', max_length=255)),
                ('Dest_Locator_Row', models.CharField(default='NA', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
