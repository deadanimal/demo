from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from phonenumber_field.modelfields import PhoneNumberField


class Grn(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Header_Interface_Number = models.CharField(max_length=255, default='')
    Receipt_Source_Code = models.CharField(max_length=255, default='')
    Business_Unit = models.CharField(max_length=255, default='')
    Transaction_Type = models.CharField(max_length=255, default='')
    Receipt_Number = models.CharField(max_length=255, default='')
    Supplier_Number = models.CharField(max_length=255, default='')
    Supplier_Site_Code = models.CharField(max_length=255, default='')
    Bill_Of_Lading = models.CharField(max_length=255, default='')
    Packing_Slip = models.CharField(max_length=255, default='')
    Carrier_Name = models.CharField(max_length=255, default='')
    Waybill = models.CharField(max_length=255, default='')
    Comments = models.CharField(max_length=255, default='')
    Receiver_Name = models.CharField(max_length=255, default='')
    Interface_Line_Number = models.CharField(max_length=255, default='')

    TRANSACTION_TYPE = [
        ('00', 'RECEIVE'),
        ('01', 'CORRECT'),
        ('02', 'RETURN TO VENDOR'),

        ('NA', ''),
    ]

    Transaction_Type = models.CharField(max_length=2, choices=TRANSACTION_TYPE, default='NA')

    AUTO_TRANSACT_CODE = [
        ('00', 'DELIVER'),

        ('NA', ''),
    ]

    Auto_Transact_Code = models.CharField(max_length=2, choices=AUTO_TRANSACT_CODE, default='NA')
    Transaction_Date = models.DateField(null=True)
    Source_Document_Code = models.CharField(max_length=255, default='')
    Parent_Interface_Number = models.CharField(max_length=255, default='')
    Organization_Code = models.CharField(max_length=255, default='')
    Item_Number = models.CharField(max_length=255, default='')
    Document_Number = models.CharField(max_length=255, default='')
    Document_Line_Number = models.CharField(max_length=255, default='')
    Document_Schedule_Number = models.CharField(max_length=255, default='')
    Document_Distribution_Number = models.CharField(max_length=255, default='')
    Subinventory = models.CharField(max_length=255, default='')
    Quantity = models.CharField(max_length=255, default='')
    UOM = models.CharField(max_length=255, default='')
    Locator = models.CharField(max_length=255, default='')
    Interface_Source_Code = models.CharField(max_length=255, default='')
    Reason = models.CharField(max_length=255, default='')
    Remarks = models.CharField(max_length=255, default='')    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id   

class InventoryTransaction(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Organization_Name = models.CharField(max_length=255, default='')
    Source_Code = models.CharField(max_length=255, default='')
    Source_Header_Id  = models.CharField(max_length=255, default='')
    Source_Line_Id  = models.CharField(max_length=255, default='')
    Transaction_Date = models.CharField(max_length=255, default='')
    Item_Number = models.CharField(max_length=255, default='')
    Subinventory_Code = models.CharField(max_length=255, default='')
    Locator_Rack = models.CharField(max_length=255, default='')
    Locator_Row = models.CharField(max_length=255, default='')
    Transaction_Quantity = models.CharField(max_length=255, default='')
    Transaction_Uom = models.CharField(max_length=255, default='')
    Transaction_Type_Name = models.CharField(max_length=255, default='')
    Transaction_Reference = models.CharField(max_length=255, default='')
    Dst_Segment1  = models.CharField(max_length=255, default='')
    Dst_Segment2  = models.CharField(max_length=255, default='')
    Dst_Segment3  = models.CharField(max_length=255, default='')
    Dst_Segment4  = models.CharField(max_length=255, default='')
    Dst_Segment5 = models.CharField(max_length=255, default='')
    Dst_Segment6  = models.CharField(max_length=255, default='')
    Dst_Segment7 = models.CharField(max_length=255, default='')
    Use_Current_Cost  = models.CharField(max_length=255, default='')
    Transaction_Cost_Identifier = models.CharField(max_length=255, default='')
    Cost_Component_Code = models.CharField(max_length=255, default='')
    Cost = models.CharField(max_length=255, default='')
    Serial_Num_Identifier = models.CharField(max_length=255, default='')
    From_Serial_Num = models.CharField(max_length=255, default='')
    To_Serial_Num = models.CharField(max_length=255, default='')
    Destination_Organization = models.CharField(max_length=255, default='')
    Destination_Subinventory = models.CharField(max_length=255, default='')
    Dest_Locator_Rack = models.CharField(max_length=255, default='')
    Dest_Locator_Row = models.CharField(max_length=255, default='')

    Dest_Locator_Rack = models.CharField(max_length=255, default='')
    Dest_Locator_Row = models.CharField(max_length=255, default='')    

    Project_Number = models.CharField(max_length=255, default='')
    Task_Number = models.CharField(max_length=255, default='')
    Expenditure_Type_Name = models.CharField(max_length=255, default='')
    Expenditure_Item_Date = models.CharField(max_length=255, default='')
    Expenditure_Org_Name = models.CharField(max_length=255, default='')
    Mat_Req_Ref = models.CharField(max_length=255, default='')
    Mat_Req_Ref_Value = models.CharField(max_length=255, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id        


class MrTransaction(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Organization_Name = models.CharField(max_length=255, default='')
    Source_Code = models.CharField(max_length=255, default='')
    Source_Header_Id  = models.CharField(max_length=255, default='')
    Source_Line_Id  = models.CharField(max_length=255, default='')
    Transaction_Date = models.CharField(max_length=255, default='')
    Item_Number = models.CharField(max_length=255, default='')
    Subinventory_Code = models.CharField(max_length=255, default='')
    Locator_Rack = models.CharField(max_length=255, default='')
    Locator_Row = models.CharField(max_length=255, default='')
    Transaction_Quantity = models.CharField(max_length=255, default='')
    Transaction_Uom = models.CharField(max_length=255, default='')
    Transaction_Type_Name = models.CharField(max_length=255, default='')
    Transaction_Reference = models.CharField(max_length=255, default='')
    Dst_Segment1  = models.CharField(max_length=255, default='')
    Dst_Segment2  = models.CharField(max_length=255, default='')
    Dst_Segment3  = models.CharField(max_length=255, default='')
    Dst_Segment4  = models.CharField(max_length=255, default='')
    Dst_Segment5 = models.CharField(max_length=255, default='')
    Dst_Segment6  = models.CharField(max_length=255, default='')
    Dst_Segment7 = models.CharField(max_length=255, default='')
    Use_Current_Cost  = models.CharField(max_length=255, default='')
    Transaction_Cost_Identifier = models.CharField(max_length=255, default='')
    Cost_Component_Code = models.CharField(max_length=255, default='')
    Cost = models.CharField(max_length=255, default='')
    Serial_Num_Identifier = models.CharField(max_length=255, default='')
    From_Serial_Num = models.CharField(max_length=255, default='')
    To_Serial_Num = models.CharField(max_length=255, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']
      


class MrTransactionChild(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    MrTransaction = models.ForeignKey(MrTransaction, on_delete=models.CASCADE, null=False)

    Item_Number = models.CharField(max_length=255, default='')    
    Description = models.CharField(max_length=255, default='')
    Long_Description = models.CharField(max_length=1023, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']
      