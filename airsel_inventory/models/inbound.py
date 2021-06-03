from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from phonenumber_field.modelfields import PhoneNumberField


class PurchaseOrderInterface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    PO_Number = models.CharField(max_length=255, default='NA')
    Change_Order_Number = models.CharField(max_length=255, default='NA')
    Change_Order_Status = models.CharField(max_length=255, default='NA')
    Description = models.CharField(max_length=255, default='NA')
    Procurement_BU = models.CharField(max_length=255, default='NA')
    SoldTo_Legal_Entity = models.CharField(max_length=255, default='NA')
    Buyer = models.CharField(max_length=255, default='NA')
    Supplier_Number = models.CharField(max_length=255, default='NA')
    Supplier_Name = models.CharField(max_length=255, default='NA')
    Supplier_Site_Code = models.CharField(max_length=255, default='NA')
    Address_Name = models.CharField(max_length=255, default='NA')
    Address_Line1 = models.CharField(max_length=255, default='NA')
    Address_Line2 = models.CharField(max_length=255, default='NA')
    Address_Line3 = models.CharField(max_length=255, default='NA')
    City = models.CharField(max_length=255, default='NA')
    State = models.CharField(max_length=255, default='NA')
    Postal_Code = models.CharField(max_length=255, default='NA')
    Country = models.CharField(max_length=255, default='NA')
    Contact_First_Name = models.CharField(max_length=255, default='NA')
    Contact_Last_Name = models.CharField(max_length=255, default='NA')
    Contact_Email_Address = models.CharField(max_length=255, default='NA')
    Contact_Mobile_Number = models.CharField(max_length=255, default='NA')
    Contact_Phone_Number = models.CharField(max_length=255, default='NA')
    Supplier_Contact = models.CharField(max_length=255, default='NA')
    Line_Num = models.CharField(max_length=255, default='NA')
    Schedule_Num = models.CharField(max_length=255, default='NA')
    Distribution_Num = models.CharField(max_length=255, default='NA')
    Item_Number = models.CharField(max_length=255, default='NA')
    Line_Description = models.CharField(max_length=255, default='NA')
    Quantity = models.CharField(max_length=255, default='NA')
    UOM_Code = models.CharField(max_length=255, default='NA')
    Base_Quantity = models.CharField(max_length=255, default='NA')
    Base_UOM_Code = models.CharField(max_length=255, default='NA')
    Requested_Date = models.CharField(max_length=255, default='NA')
    Ship_to_Organization = models.CharField(max_length=255, default='NA')
    Ship_to_Organization_Name = models.CharField(max_length=255, default='NA')
    SubInventory_Code = models.CharField(max_length=255, default='NA')
    Ship_to_Location = models.CharField(max_length=255, default='NA')
    Line_Type = models.CharField(max_length=255, default='NA')
    Line_Status = models.CharField(max_length=255, default='NA')
    Requester = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id


class MaterialRequestInterface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Organization_Code = models.CharField(max_length=255, default='NA')
    Organization_Name = models.CharField(max_length=255, default='NA')
    Movement_Request_Number = models.CharField(max_length=255, default='NA')
    Movement_Request_Type = models.CharField(max_length=255, default='NA')
    Description =models.CharField(max_length=255, default='NA')
    Required_Date = models.CharField(max_length=255, default='NA')
    Transaction_Type = models.CharField(max_length=255, default='NA')
    Status =models.CharField(max_length=255, default='NA')
    Source_Subinventory = models.CharField(max_length=255, default='NA')
    Source_Locator = models.CharField(max_length=255, default='NA')
    Destination_Subinventory = models.CharField(max_length=255, default='NA')
    Destination_Locator = models.CharField(max_length=255, default='NA')
    Destination_Account = models.CharField(max_length=255, default='NA')
    DST_SEGMENT1 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT2 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT3 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT4 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT5 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT6 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT7 =models.CharField(max_length=255, default='NA')
    Line_Number = models.CharField(max_length=255, default='NA')
    Item =models.CharField(max_length=255, default='NA')
    Transaction_Type = models.CharField(max_length=255, default='NA')
    Required_Date = models.CharField(max_length=255, default='NA')
    Requested_Quantity = models.CharField(max_length=255, default='NA')
    UOM_Name = models.CharField(max_length=255, default='NA')
    Status = models.CharField(max_length=255, default='NA')
    Source_Subinventory = models.CharField(max_length=255, default='NA')
    Source_Locator = models.CharField(max_length=255, default='NA')
    Destination_Subinventory = models.CharField(max_length=255, default='NA')
    Destination_Locator = models.CharField(max_length=255, default='NA')
    Destination_Account = models.CharField(max_length=255, default='NA')
    DST_SEGMENT21 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT22 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT23 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT24 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT25 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT26 =models.CharField(max_length=255, default='NA')
    DST_SEGMENT27 =models.CharField(max_length=255, default='NA')
    Created_by = models.CharField(max_length=255, default='NA')
    Last_Update_Date = models.CharField(max_length=255, default='NA')
    Destination_Account_Id = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id   


class ItemInterface(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    Organization_Code = models.CharField(max_length=255, default='NA')
    Organization_Name = models.CharField(max_length=255, default='NA')
    Item_Number = models.CharField(max_length=255, default='NA')
    Item_Class = models.CharField(max_length=255, default='NA')
    Item_Class_Description = models.CharField(max_length=255, default='NA')
    Legal_Entity_Code = models.CharField(max_length=255, default='NA')
    Legal_Entity_Name = models.CharField(max_length=255, default='NA')
    Short_Description = models.CharField(max_length=255, default='NA')
    Long_Description = models.CharField(max_length=255, default='NA')
    Primary_UOM_Code = models.CharField(max_length=255, default='NA')
    Primary_UOM = models.CharField(max_length=255, default='NA')
    Secondary_UOM_Code = models.CharField(max_length=255, default='NA')
    Secondary_UOM = models.CharField(max_length=255, default='NA')
    Item_Status = models.CharField(max_length=255, default='NA')
    Catalog = models.CharField(max_length=255, default='NA')
    Category = models.CharField(max_length=255, default='NA')
    Minimum_Quantity = models.CharField(max_length=255, default='NA')
    Maximum_Quantity = models.CharField(max_length=255, default='NA')
    Inventory_Item = models.CharField(max_length=255, default='NA')
    Transfer_Orders_Enabled = models.CharField(max_length=255, default='NA')
    Purchasable_Item = models.CharField(max_length=255, default='NA')
    Shippable_Item = models.CharField(max_length=255, default='NA')
    Attribute1 = models.CharField(max_length=255, default='NA')
    Attribute2 = models.CharField(max_length=255, default='NA')
    Attribute3 = models.CharField(max_length=255, default='NA')
    Attribute4 = models.CharField(max_length=255, default='NA')
    Attribute5 = models.CharField(max_length=255, default='NA')
    Attribute6 = models.CharField(max_length=255, default='NA')
    Attribute7 = models.CharField(max_length=255, default='NA')
    Attribute8 = models.CharField(max_length=255, default='NA')
    Attribute9 = models.CharField(max_length=255, default='NA')
    Attribute10 = models.CharField(max_length=255, default='NA')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id            
