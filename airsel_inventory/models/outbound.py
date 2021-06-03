from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from phonenumber_field.modelfields import PhoneNumberField


class GrnInterfaceInterface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Header_Interface_Number = models.CharField(max_length=255, default='NA')
    Receipt_Source_Code = models.CharField(max_length=255, default='NA')
    Business_Unit = models.CharField(max_length=255, default='NA')
    Transaction_Type = models.CharField(max_length=255, default='NA')
    Receipt_Number = models.CharField(max_length=255, default='NA')
    Supplier_Number = models.CharField(max_length=255, default='NA')
    Supplier_Site_Code = models.CharField(max_length=255, default='NA')
    Bill_Of_Lading = models.CharField(max_length=255, default='NA')
    Packing_Slip = models.CharField(max_length=255, default='NA')
    Carrier_Name = models.CharField(max_length=255, default='NA')
    Waybill = models.CharField(max_length=255, default='NA')
    Comments = models.CharField(max_length=255, default='NA')
    Receiver_Name = models.CharField(max_length=255, default='NA')
    Interface_Line_Number = models.CharField(max_length=255, default='NA')
    Transaction_Type = models.CharField(max_length=255, default='NA')
    Auto_Transact_Code = models.CharField(max_length=255, default='NA')
    Transaction_Date = models.CharField(max_length=255, default='NA')
    Source_Document_Code = models.CharField(max_length=255, default='NA')
    Parent_Interface_Number = models.CharField(max_length=255, default='NA')
    Organization_Code = models.CharField(max_length=255, default='NA')
    Item_Number = models.CharField(max_length=255, default='NA')
    Document_Number = models.CharField(max_length=255, default='NA')
    Document_Line_Number = models.CharField(max_length=255, default='NA')
    Document_Schedule_Number = models.CharField(max_length=255, default='NA')
    Document_Distribution_Number = models.CharField(max_length=255, default='NA')
    Subinventory = models.CharField(max_length=255, default='NA')
    Quantity = models.CharField(max_length=255, default='NA')
    UOM = models.CharField(max_length=255, default='NA')
    Locator = models.CharField(max_length=255, default='NA')
    Interface_Source_Code = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id   

class GrnInterface2Interface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Header_Interface_Number = models.CharField(max_length=255, default='NA')
    Receipt_Source_Code = models.CharField(max_length=255, default='NA')
    Business_Unit = models.CharField(max_length=255, default='NA')
    Transaction_Type = models.CharField(max_length=255, default='NA')
    Receipt_Number = models.CharField(max_length=255, default='NA')
    Supplier_Number = models.CharField(max_length=255, default='NA')
    Supplier_Site_Code = models.CharField(max_length=255, default='NA')
    Bill_Of_Lading = models.CharField(max_length=255, default='NA')
    Packing_Slip = models.CharField(max_length=255, default='NA')
    Carrier_Name = models.CharField(max_length=255, default='NA')
    Waybill = models.CharField(max_length=255, default='NA')
    Comments = models.CharField(max_length=255, default='NA')
    Receiver_Name = models.CharField(max_length=255, default='NA')
    Interface_Line_Number = models.CharField(max_length=255, default='NA')
    Transaction_Type = models.CharField(max_length=255, default='NA')
    Auto_Transact_Code = models.CharField(max_length=255, default='NA')
    Transaction_Date = models.CharField(max_length=255, default='NA')
    Source_Document_Code = models.CharField(max_length=255, default='NA')
    Parent_Interface_Number = models.CharField(max_length=255, default='NA')
    Organization_Code = models.CharField(max_length=255, default='NA')
    Item_Number = models.CharField(max_length=255, default='NA')
    Document_Number = models.CharField(max_length=255, default='NA')
    Document_Line_Number = models.CharField(max_length=255, default='NA')
    Document_Schedule_Number = models.CharField(max_length=255, default='NA')
    Document_Distribution_Number = models.CharField(max_length=255, default='NA')
    Subinventory = models.CharField(max_length=255, default='NA')
    Quantity = models.CharField(max_length=255, default='NA')
    UOM = models.CharField(max_length=255, default='NA')
    Locator = models.CharField(max_length=255, default='NA')
    Interface_Source_Code = models.CharField(max_length=255, default='NA')
    Reason = models.CharField(max_length=255, default='NA')
    Remarks = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id    



class InventoryTransactionInterface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Organization_Name = models.CharField(max_length=255, default='NA')
    Source_Code = models.CharField(max_length=255, default='NA')
    Source_Header_Id  = models.CharField(max_length=255, default='NA')
    Source_Line_Id  = models.CharField(max_length=255, default='NA')
    Transaction_Date = models.CharField(max_length=255, default='NA')
    Item_Number = models.CharField(max_length=255, default='NA')
    Subinventory_Code = models.CharField(max_length=255, default='NA')
    Locator_Rack = models.CharField(max_length=255, default='NA')
    Locator_Row = models.CharField(max_length=255, default='NA')
    Transaction_Quantity = models.CharField(max_length=255, default='NA')
    Transaction_Uom = models.CharField(max_length=255, default='NA')
    Transaction_Type_Name = models.CharField(max_length=255, default='NA')
    Transaction_Reference = models.CharField(max_length=255, default='NA')
    Dst_Segment1  = models.CharField(max_length=255, default='NA')
    Dst_Segment2  = models.CharField(max_length=255, default='NA')
    Dst_Segment3  = models.CharField(max_length=255, default='NA')
    Dst_Segment4  = models.CharField(max_length=255, default='NA')
    Dst_Segment5 = models.CharField(max_length=255, default='NA')
    Dst_Segment6  = models.CharField(max_length=255, default='NA')
    Dst_Segment7 = models.CharField(max_length=255, default='NA')
    Use_Current_Cost  = models.CharField(max_length=255, default='NA')
    Transaction_Cost_Identifier = models.CharField(max_length=255, default='NA')
    Cost_Component_Code = models.CharField(max_length=255, default='NA')
    Cost = models.CharField(max_length=255, default='NA')
    Serial_Num_Identifier = models.CharField(max_length=255, default='NA')
    From_Serial_Num = models.CharField(max_length=255, default='NA')
    To_Serial_Num = models.CharField(max_length=255, default='NA')
    Destination_Organization = models.CharField(max_length=255, default='NA')
    Destination_Subinventory = models.CharField(max_length=255, default='NA')
    Dest_Locator_Rack = models.CharField(max_length=255, default='NA')
    Dest_Locator_Row = models.CharField(max_length=255, default='NA')



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id        


class InventoryTransactionFromProjectInterface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Organization_Name = models.CharField(max_length=255, default='NA')
    Source_Code = models.CharField(max_length=255, default='NA')
    Source_Header_Id  = models.CharField(max_length=255, default='NA')
    Source_Line_Id  = models.CharField(max_length=255, default='NA')
    Transaction_Date = models.CharField(max_length=255, default='NA')
    Item_Number = models.CharField(max_length=255, default='NA')
    Subinventory_Code = models.CharField(max_length=255, default='NA')
    Locator_Rack = models.CharField(max_length=255, default='NA')
    Locator_Row = models.CharField(max_length=255, default='NA')
    Transaction_Quantity = models.CharField(max_length=255, default='NA')
    Transaction_Uom = models.CharField(max_length=255, default='NA')
    Transaction_Type_Name = models.CharField(max_length=255, default='NA')
    Transaction_Reference = models.CharField(max_length=255, default='NA')
    Dst_Segment1  = models.CharField(max_length=255, default='NA')
    Dst_Segment2  = models.CharField(max_length=255, default='NA')
    Dst_Segment3  = models.CharField(max_length=255, default='NA')
    Dst_Segment4  = models.CharField(max_length=255, default='NA')
    Dst_Segment5 = models.CharField(max_length=255, default='NA')
    Dst_Segment6  = models.CharField(max_length=255, default='NA')
    Dst_Segment7 = models.CharField(max_length=255, default='NA')
    Use_Current_Cost  = models.CharField(max_length=255, default='NA')
    Transaction_Cost_Identifier = models.CharField(max_length=255, default='NA')
    Cost_Component_Code = models.CharField(max_length=255, default='NA')
    Cost = models.CharField(max_length=255, default='NA')
    Project_Number = models.CharField(max_length=255, default='NA')
    Task_Number = models.CharField(max_length=255, default='NA')
    Expenditure_Type_Name = models.CharField(max_length=255, default='NA')
    Expenditure_Item_Date = models.CharField(max_length=255, default='NA')
    Expenditure_Org_Name = models.CharField(max_length=255, default='NA')
    Serial_Num_Identifier = models.CharField(max_length=255, default='NA')
    From_Serial_Num = models.CharField(max_length=255, default='NA')
    To_Serial_Num = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id  


class InventoryTransactionFromMaintenanceInterface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Organization_Name = models.CharField(max_length=255, default='NA')
    Source_Code = models.CharField(max_length=255, default='NA')
    Source_Header_Id  = models.CharField(max_length=255, default='NA')
    Source_Line_Id  = models.CharField(max_length=255, default='NA')
    Transaction_Date = models.CharField(max_length=255, default='NA')
    Item_Number = models.CharField(max_length=255, default='NA')
    Subinventory_Code = models.CharField(max_length=255, default='NA')
    Locator_Rack = models.CharField(max_length=255, default='NA')
    Locator_Row = models.CharField(max_length=255, default='NA')
    Transaction_Quantity = models.CharField(max_length=255, default='NA')
    Transaction_Uom = models.CharField(max_length=255, default='NA')
    Transaction_Type_Name = models.CharField(max_length=255, default='NA')
    Transaction_Reference = models.CharField(max_length=255, default='NA')
    Dst_Segment1  = models.CharField(max_length=255, default='NA')
    Dst_Segment2  = models.CharField(max_length=255, default='NA')
    Dst_Segment3  = models.CharField(max_length=255, default='NA')
    Dst_Segment4  = models.CharField(max_length=255, default='NA')
    Dst_Segment5 = models.CharField(max_length=255, default='NA')
    Dst_Segment6  = models.CharField(max_length=255, default='NA')
    Dst_Segment7 = models.CharField(max_length=255, default='NA')
    Use_Current_Cost  = models.CharField(max_length=255, default='NA')
    Transaction_Cost_Identifier = models.CharField(max_length=255, default='NA')
    Cost_Component_Code = models.CharField(max_length=255, default='NA')
    Cost = models.CharField(max_length=255, default='NA')
    Mat_Req_Ref = models.CharField(max_length=255, default='NA')
    Mat_Req_Ref_Value = models.CharField(max_length=255, default='NA')
    Serial_Num_Identifier = models.CharField(max_length=255, default='NA')
    From_Serial_Num = models.CharField(max_length=255, default='NA')
    To_Serial_Num = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id          