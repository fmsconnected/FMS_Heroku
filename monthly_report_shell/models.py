from django.db import models
import datetime
from django.utils import timezone
import datetime
from django.db.models import DateTimeField,DateField
from datetime import date,timedelta
from django.urls import reverse




class shell_report(models.Model):
	# AccountNumber = models.CharField(max_length=254, null=True, blank=True)
	# CustomerName1 = models.CharField(max_length=254, null=True, blank=True)
	# FullCardNumber = models.CharField(max_length=254, null=True, blank=True)
	# DelcoListPrice = models.CharField(max_length=254, null=True, blank=True)
	# NetCustomerAmount = models.FloatField(max_length=254, null=True, blank=True)
	# CardSequenceNumber = models.CharField(max_length=254, null=True, blank=True)
	# CheckDigit = models.CharField(max_length=254, null=True, blank=True)
	# DelcoGrossValue = models.FloatField(max_length=254, null=True, blank=True)
	# DelcoVatAmount = models.FloatField(max_length=254, null=True, blank=True)
	# DelcoVatRate = models.FloatField(max_length=254, null=True, blank=True)
	# RebateCustAmount = models.FloatField(max_length=254, null=True, blank=True)
	# VATNetAmount = models.FloatField(max_length=254, null=True, blank=True)
	# DelcoRebateRate = models.FloatField(max_length=254, null=True, blank=True)
	# VoucherNumber = models.CharField(max_length=254, null=True, blank=True)
	# FleetId = models.CharField(max_length=254, null=True, blank=True)
	# Quantity = models.FloatField(max_length=254, null=True, blank=True)
	# DialogueIndicator = models.CharField(max_length=254, null=True, blank=True)
	# IssuerCode1 = models.CharField(max_length=254, null=True, blank=True)
	# NetInvoiceIndicator = models.CharField(max_length=254, null=True, blank=True)
	# NetworkCode = models.CharField(max_length=254, null=True, blank=True)
	# CardGroupName = models.CharField(max_length=254, null=True, blank=True)
	# CardHolderName = models.CharField(max_length=254, null=True, blank=True)
	# CardVehicleRegistrationNumber = models.CharField(max_length=254, null=True, blank=True)
	# DeliveryNetAmount = models.FloatField(max_length=254, null=True, blank=True)
	# PinIndicator = models.CharField(max_length=254, null=True, blank=True)
	# RebateType = models.CharField(max_length=254, null=True, blank=True)
	# RecordType = models.CharField(max_length=254, null=True, blank=True)
	# ReleaseCode = models.CharField(max_length=254, null=True, blank=True)
	# Time = models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
	# TransactionStatus = models.CharField(max_length=254, null=True, blank=True)
	# TransactionType1 = models.CharField(max_length=254, null=True, blank=True)
	# VATIndicator = models.CharField(max_length=254, null=True, blank=True)
	# VatUsage = models.FloatField(max_length=254, null=True, blank=True)
	# IssuerCountry = models.CharField(max_length=254, null=True, blank=True)
	# DelcoCode = models.CharField(max_length=254, null=True, blank=True)
	# DelcoCountryCode1 = models.CharField(max_length=254, null=True, blank=True)
	# TransactionCurrency = models.CharField(max_length=254, null=True, blank=True)
	# InvoiceNumber = models.CharField(max_length=254, null=True, blank=True)
	# InvoiceDate = models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True)
	# ProductCode = models.CharField(max_length=254, null=True, blank=True)
	# SiteCode = models.CharField(max_length=254, null=True, blank=True)
	# Site = models.CharField(max_length=254, null=True, blank=True)
	# DeliveryDate = models.CharField(max_length=254, null=True, blank=True)
	# OdometerReading1 = models.CharField(max_length=254, null=True, blank=True)
	# DelcoCustRate1 = models.CharField(max_length=254, null=True, blank=True)
	# CustomerCurrencyName1 = models.CharField(max_length=254, null=True, blank=True)
	# DelcoPumpPrice = models.FloatField(max_length=254, null=True, blank=True)
	# DelcoRebateAmount1 = models.FloatField(max_length=254, null=True, blank=True)
	# CustRebateRate1 = models.FloatField(max_length=254, null=True, blank=True)
	# PayerDisplayName = models.CharField(max_length=254, null=True, blank=True)
	# PayerCode = models.CharField(max_length=254, null=True, blank=True)
	# CardGroupID = models.CharField(max_length=254, null=True, blank=True)
	# ProductName = models.CharField(max_length=254, null=True, blank=True)
	# CreditDebitCode = models.CharField(max_length=254, null=True, blank=True)
	# CorrectionFlag = models.CharField(max_length=254, null=True, blank=True)
	# DelcoCountryCode = models.CharField(max_length=254, null=True, blank=True)
	# VATApplicable = models.CharField(max_length=254, null=True, blank=True)
	# CustomerEuroRate = models.FloatField(max_length=254, null=True, blank=True)
	# DelcoEuroRate = models.FloatField(max_length=254, null=True, blank=True)
	# EuroRebateAmount = models.FloatField(max_length=254, null=True, blank=True)
	# EuroVATAmount = models.FloatField(max_length=254, null=True, blank=True)
	# InvoiceSequenceNo = models.CharField(max_length=254, null=True, blank=True)
	# ListPriceInTransactionCurrency = models.CharField(max_length=254, null=True, blank=True)
	# NetEuroAmount = models.FloatField(max_length=254, null=True, blank=True)
	# PumpPriceInTransactionCurrency = models.FloatField(max_length=254, null=True, blank=True)
	# RebateonNetAmountInCustomerCurrency = models.FloatField(max_length=254, null=True, blank=True)
	# RebateonNetAmountInTransactionCurrency = models.FloatField(max_length=254, null=True, blank=True)
	# RebateRate = models.FloatField(max_length=254, null=True, blank=True)
	# UnInvoiceSequenceNo = models.CharField(max_length=254, null=True, blank=True)
	# NetworkName = models.CharField(max_length=254, null=True, blank=True)
	# Additional1 = models.CharField(max_length=254, null=True, blank=True)
	# Additional2 = models.CharField(max_length=254, null=True, blank=True)
	# Additional3 = models.CharField(max_length=254, null=True, blank=True)
	# Additional4 = models.CharField(max_length=254, null=True, blank=True)
	# TransactionIdentifier = models.CharField(max_length=254, null=True, blank=True)
	# TransactionAuthorisationCode = models.CharField(max_length=254, null=True, blank=True)
	# DelcoName = models.CharField(max_length=254, null=True, blank=True)
	# SiteGroupid = models.CharField(max_length=254, null=True, blank=True)
	# SiteGroupName = models.CharField(max_length=254, null=True, blank=True)
	# Cardtype = models.CharField(max_length=254, null=True, blank=True)
	# PayerGroup = models.CharField(max_length=254, null=True, blank=True)
	# PayerNumber = models.CharField(max_length=254, null=True, blank=True)
	# RefundFlag = models.CharField(max_length=254, null=True, blank=True)
	# RefundOriginalTransactionId = models.CharField(max_length=254, null=True, blank=True)
	# PostingDate = models.CharField(max_length=254, null=True, blank=True)
	# PostingTime = models.TimeField(auto_now=False,auto_now_add=False, null=True, blank=True)
	# CustomerReferenceValue = models.CharField(max_length=254, null=True, blank=True)
	# CustomerReferenceDescription = models.CharField(max_length=254, null=True, blank=True)
	# CardPayerAssociationCode = models.CharField(max_length=254, null=True, blank=True)
	# CardPayerAssociation = models.CharField(max_length=254, null=True, blank=True)
	# IncomingProductCode = models.CharField(max_length=254, null=True, blank=True)
	# TransactionProviderId = models.CharField(max_length=254, null=True, blank=True)
	# TransactionProviderName = models.CharField(max_length=254, null=True, blank=True)
	# FileName = models.CharField(max_length=254, null=True, blank=True)
	# FileDate = models.CharField(max_length=254, null=True, blank=True)
	# AccountGroup3Code = models.CharField(max_length=254, null=True, blank=True)
	# AccountGroup3Name = models.CharField(max_length=254, null=True, blank=True)
	# ContractedRebateRate = models.FloatField(max_length=254, null=True, blank=True)
	# IsBestOfPricingApplicable = models.CharField(max_length=254, null=True, blank=True)
	# CostCenter = models.CharField(max_length=254, null=True, blank=True)
	# Supplier = models.CharField(max_length=254, null=True, blank=True)

	Account_Customer_Number= models.CharField(max_length=254, null=True, blank=True)
	Account_Name= models.CharField(max_length=254, null=True, blank=True)
	Card_PAN= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Delco_List_Price_Total_Net= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Customer_Invoice_Total_Net= models.CharField(max_length=254, null=True, blank=True)
	Card_Sequence_Number= models.CharField(max_length=254, null=True, blank=True)
	Card_Luhn_Check_Digit= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Delco_Invoice_Total_Gross= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Delco_Invoice_Total_VAT= models.CharField(max_length=254, null=True, blank=True)
	Trx_VAT_Percentage= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Customer_Effective_Discount_Total_Net= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_System_Invoice_Total_VAT= models.CharField(max_length=254, null=True, blank=True)
	Trx_Delco_Effective_Discount_Unit_Net= models.CharField(max_length=254, null=True, blank=True)
	Trx_Other_Prompt= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Quantity= models.CharField(max_length=254, null=True, blank=True)
	Card_Issuer_Code= models.CharField(max_length=254, null=True, blank=True)
	Net_Invoice_Indicator= models.CharField(max_length=254, null=True, blank=True)
	Network_Code= models.CharField(max_length=254, null=True, blank=True)
	Card_Group_Description= models.CharField(max_length=254, null=True, blank=True)
	Account_Card_Embossing_Default_Name= models.CharField(max_length=254, null=True, blank=True)
	Card_VRN= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Delco_Invoice_Total_Net= models.CharField(max_length=254, null=True, blank=True)
	Trx_PIN_Used_Description= models.CharField(max_length=254, null=True, blank=True)
	Trx_Discount_Pricing_Type_Description= models.CharField(max_length=254, null=True, blank=True)
	Transaction_Item_Type_Description= models.CharField(max_length=254, null=True, blank=True)
	Card_Release_Code= models.CharField(max_length=254, null=True, blank=True)
	Trx_Delivery_Time= models.CharField(max_length=254, null=True, blank=True)
	Trx_Transaction_Billed_Indicator= models.CharField(max_length=254, null=True, blank=True)
	Trx_Transaction_Type_Description= models.CharField(max_length=254, null=True, blank=True)
	Card_Issuing_Country_Code= models.CharField(max_length=254, null=True, blank=True)
	Trx_Delco_Code= models.CharField(max_length=254, null=True, blank=True)
	Delco_Country_ISO2_Code= models.CharField(max_length=254, null=True, blank=True)
	Trx_Customer_Currency_ISO3_Code= models.CharField(max_length=254, null=True, blank=True)
	Trx_Invoice_Number= models.CharField(max_length=254, null=True, blank=True)
	Trx_Invoice_Date= models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True)
	Trx_Global_Product_Code= models.CharField(max_length=254, null=True, blank=True)
	Euroshell_Site_Number= models.CharField(max_length=254, null=True, blank=True)
	Site_Name= models.CharField(max_length=254, null=True, blank=True)
	Trx_Delivery_Date= models.CharField(max_length=254, null=True, blank=True)
	Trx_Odometer_Reading= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Delco_Discount_Total_Net= models.CharField(max_length=254, null=True, blank=True)
	Trx_Customer_Effective_Discount_Unit_Net= models.CharField(max_length=254, null=True, blank=True)
	Legal_Entity_Trading_Name= models.CharField(max_length=254, null=True, blank=True)
	Account_Legal_Entity_Customer_Number= models.CharField(max_length=254, null=True, blank=True)
	Card_Group_Code= models.CharField(max_length=254, null=True, blank=True)
	Global_Product_Description= models.CharField(max_length=254, null=True, blank=True)
	Trx_Transaction_Debit_Or_Credit_Indicator= models.CharField(max_length=254, null=True, blank=True)
	Trx_Correction_Flag= models.CharField(max_length=254, null=True, blank=True)
	Delco_Country_Name= models.CharField(max_length=254, null=True, blank=True)
	Legal_Entity_VAT_Exempt_Indicator= models.CharField(max_length=254, null=True, blank=True)
	Trx_Customer_To_Euro_Exchange_Rate= models.CharField(max_length=254, null=True, blank=True)
	Trx_Site_To_Euro_Exchange_Rate= models.CharField(max_length=254, null=True, blank=True)
	Trx_System_Effective_Discount_Total_Net= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_System_Invoice_Total_Net= models.CharField(max_length=254, null=True, blank=True)
	Trx_Delco_Retail_Price_Unit_Net= models.CharField(max_length=254, null=True, blank=True)
	Trx_Rebate_on_Net_Amount_In_Customer_Currency= models.CharField(max_length=254, null=True, blank=True)
	Trx_Rebate_on_Net_Amount_In_Transaction_Currency= models.CharField(max_length=254, null=True, blank=True)
	Trx_Rebate_Rate= models.CharField(max_length=254, null=True, blank=True)
	Network_Name= models.CharField(max_length=254, null=True, blank=True)
	Trx_Additional_1= models.CharField(max_length=254, null=True, blank=True)
	Trx_Additional_2= models.CharField(max_length=254, null=True, blank=True)
	Trx_Additional_3= models.CharField(max_length=254, null=True, blank=True)
	Trx_Additional_4= models.CharField(max_length=254, null=True, blank=True)
	Trx_Transaction_Item_Id= models.CharField(max_length=254, null=True, blank=True)
	Trx_Authorisation_Code= models.CharField(max_length=254, null=True, blank=True)
	Delco_Name= models.CharField(max_length=254, null=True, blank=True)
	Site_Groups= models.CharField(max_length=254, null=True, blank=True)
	Card_Type_Description= models.CharField(max_length=254, null=True, blank=True)
	Legal_Entity_Group_Description= models.CharField(max_length=254, null=True, blank=True)
	Trx_Original_Transaction_Item_Id= models.CharField(max_length=254, null=True, blank=True)
	Trx_GFN_Posting_Date= models.CharField(max_length=254, null=True, blank=True)
	Trx_GFN_Posting_Time= models.CharField(max_length=254, null=True, blank=True)
	Card_Fleet_Id_Prompt= models.CharField(max_length=254, null=True, blank=True)
	Trx_Vehicle_Registration_Number= models.CharField(max_length=254, null=True, blank=True)
	Card_Payer_Association_Code= models.CharField(max_length=254, null=True, blank=True)
	Card_Payer_Association_Name= models.CharField(max_length=254, null=True, blank=True)
	Trx_Forward_Standard_Product_Code= models.CharField(max_length=254, null=True, blank=True)
	Trx_Transaction_Provider_Code= models.CharField(max_length=254, null=True, blank=True)
	Trx_Transaction_Provider_Description= models.CharField(max_length=254, null=True, blank=True)
	Trx_Incoming_Transaction_Batch_File_Name= models.CharField(max_length=254, null=True, blank=True)
	Trx_Insert_Date= models.CharField(max_length=254, null=True, blank=True)
	Account_Group_3_Code= models.CharField(max_length=254, null=True, blank=True)
	Account_Group_3_Name= models.CharField(max_length=254, null=True, blank=True)
	Trx_Colco_Contracted_Discount_Unit_Net= models.CharField(max_length=254, null=True, blank=True)
	Account_Best_Of_Price_Indicator= models.CharField(max_length=254, null=True, blank=True)
	Card_Driver_Name= models.CharField(max_length=254, null=True, blank=True)
	Trx_Incoming_Site_Location_Description= models.CharField(max_length=254, null=True, blank=True)
	Trx_Delco_List_Price_Unit_Net= models.CharField(max_length=254, null=True, blank=True)
	Trx_Receipt_Number= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_System_Invoice_Total_Gross= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Customer_Invoice_Total_VAT= models.CharField(max_length=254, null=True, blank=True)
	Sum_of_Trx_Customer_Invoice_Total_Gross= models.CharField(max_length=254, null=True, blank=True)
	Cost_Center= models.CharField(max_length=254, null=True, blank=True)

	def __str__(self):
		return self.AccountNumber

	def get_absolute_url(self):
		return reverse('report_shell_list')

class shell_pivot(models.Model):
	ChargingDepartment = models.CharField(max_length=254, null=True, blank=True)
	sum_delco_gross = models.CharField(max_length=254, null=True, blank=True)
	Sum_total_net = models.CharField(max_length=254, null=True, blank=True)
