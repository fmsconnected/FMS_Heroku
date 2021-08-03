from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import (
	shell_report
	)


class shell_form(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(shell_form, self).__init__(*args, **kwargs)
		self.fields['AccountNumber'].required = False
		self.fields['CustomerName1'].required = False
		self.fields['FullCardNumber'].required = False
		self.fields['DelcoListPrice'].required = False
		self.fields['NetCustomerAmount'].required = False
		self.fields['CardSequenceNumber'].required = False
		self.fields['CheckDigit'].required = False
		self.fields['DelcoGrossValue'].required = True
		self.fields['DelcoVatAmount'].required = True
		self.fields['DelcoVatRate'].required = True
		self.fields['RebateCustAmount'].required = True
		self.fields['VATNetAmount'].required = True
		self.fields['DelcoRebateRate'].required = False
		self.fields['VoucherNumber'].required = False
		self.fields['FleetId'].required = False
		self.fields['Quantity'].required = False
		self.fields['DialogueIndicator'].required = False
		self.fields['IssuerCode1'].required = False
		self.fields['NetInvoiceIndicator'].required = False
		self.fields['NetworkCode'].required = False
		self.fields['CardGroupName'].required = False
		self.fields['CardHolderName'].required = False
		self.fields['CardVehicleRegistrationNumber'].required = False
		self.fields['DeliveryNetAmount'].required = False
		self.fields['PinIndicator'].required = False
		self.fields['RebateType'].required = False
		self.fields['RecordType'].required = False
		self.fields['ReleaseCode'].required = False
		self.fields['Time'].required = False
		self.fields['TransactionStatus'].required = False
		self.fields['TransactionType1'].required = False
		self.fields['VATIndicator'].required = False
		self.fields['VatUsage'].required = False
		self.fields['IssuerCountry'].required = False
		self.fields['DelcoCode'].required = False
		self.fields['DelcoCountryCode1'].required = False
		self.fields['TransactionCurrency'].required = False
		self.fields['InvoiceNumber'].required = False
		self.fields['InvoiceDate'].required = True
		self.fields['ProductCode'].required = False
		self.fields['SiteCode'].required = False
		self.fields['Site'].required = False
		self.fields['DeliveryDate'].required = False
		self.fields['OdometerReading1'].required = False
		self.fields['DelcoCustRate1'].required = False
		self.fields['CustomerCurrencyName1'].required = False
		self.fields['DelcoPumpPrice'].required = False
		self.fields['DelcoRebateAmount1'].required = False
		self.fields['CustRebateRate1'].required = False
		self.fields['PayerDisplayName'].required = False
		self.fields['PayerCode'].required = False
		self.fields['CardGroupID'].required = False
		self.fields['ProductName'].required = False
		self.fields['CreditDebitCode'].required = False
		self.fields['CorrectionFlag'].required = False
		self.fields['DelcoCountryCode'].required = False
		self.fields['VATApplicable'].required = False
		self.fields['DelcoEuroRate'].required = False
		self.fields['EuroRebateAmount'].required = False
		self.fields['EuroVATAmount'].required = False
		self.fields['InvoiceSequenceNo'].required = False
		self.fields['ListPriceInTransactionCurrency'].required = False
		self.fields['NetEuroAmount'].required = False
		self.fields['PumpPriceInTransactionCurrency'].required = False
		self.fields['RebateonNetAmountInCustomerCurrency'].required = False
		self.fields['RebateonNetAmountInTransactionCurrency'].required = False
		self.fields['RebateRate'].required = False
		self.fields['UnInvoiceSequenceNo'].required = False
		self.fields['NetworkName'].required = False
		self.fields['Additional1'].required = False
		self.fields['Additional2'].required = False
		self.fields['Additional3'].required = False
		self.fields['Additional4'].required = False
		self.fields['TransactionIdentifier'].required = False
		self.fields['TransactionAuthorisationCode'].required = False
		self.fields['DelcoName'].required = False
		self.fields['SiteGroupid'].required = False
		self.fields['SiteGroupName'].required = False
		self.fields['Cardtype'].required = False
		self.fields['PayerGroup'].required = False
		self.fields['PayerNumber'].required = False
		self.fields['RefundFlag'].required = False
		self.fields['RefundOriginalTransactionId'].required = False
		self.fields['PostingDate'].required = False
		self.fields['PostingTime'].required = False
		self.fields['CustomerReferenceValue'].required = False
		self.fields['CustomerReferenceDescription'].required = False
		self.fields['CardPayerAssociationCode'].required = False
		self.fields['CardPayerAssociation'].required = False
		self.fields['IncomingProductCode'].required = False
		self.fields['TransactionProviderId'].required = False
		self.fields['TransactionProviderName'].required = False
		self.fields['FileName'].required = False
		self.fields['FileDate'].required = False
		self.fields['AccountGroup3Code'].required = False
		self.fields['AccountGroup3Name'].required = False
		self.fields['ContractedRebateRate'].required = False
		self.fields['IsBestOfPricingApplicable'].required = False
		self.fields['CostCenter'].required = True

		
	class Meta:
		model = shell_report
		fields = [
		'AccountNumber','CustomerName1','FullCardNumber','DelcoListPrice','NetCustomerAmount','CardSequenceNumber',
		'CheckDigit','DelcoGrossValue','DelcoVatAmount','DelcoVatRate','RebateCustAmount','VATNetAmount','DelcoRebateRate',
		'VoucherNumber','FleetId','Quantity','DialogueIndicator','IssuerCode1','NetInvoiceIndicator','NetworkCode','CardGroupName',
		'CardHolderName','CardVehicleRegistrationNumber','DeliveryNetAmount','PinIndicator','RebateType','RecordType','ReleaseCode',
		'Time','TransactionStatus','TransactionType1','VATIndicator','VatUsage','IssuerCountry','DelcoCode','DelcoCountryCode1',
		'TransactionCurrency','InvoiceNumber','InvoiceDate','ProductCode','SiteCode','Site','DeliveryDate','OdometerReading1',
		'DelcoCustRate1','CustomerCurrencyName1','DelcoPumpPrice','DelcoRebateAmount1','CustRebateRate1','PayerDisplayName',
		'PayerCode','CardGroupID','ProductName','CreditDebitCode','CorrectionFlag','DelcoCountryCode','VATApplicable','CustomerEuroRate',
		'DelcoEuroRate','EuroRebateAmount','EuroVATAmount','InvoiceSequenceNo','ListPriceInTransactionCurrency','NetEuroAmount',
		'PumpPriceInTransactionCurrency','RebateonNetAmountInCustomerCurrency','RebateonNetAmountInTransactionCurrency','RebateRate',
		'UnInvoiceSequenceNo','NetworkName','Additional1','Additional2','Additional3','Additional4','TransactionIdentifier',
		'TransactionAuthorisationCode','DelcoName','SiteGroupid','SiteGroupName','Cardtype','PayerGroup','PayerNumber','RefundFlag',
		'RefundOriginalTransactionId','PostingDate','PostingTime','CustomerReferenceValue','CustomerReferenceDescription',
		'CardPayerAssociationCode','CardPayerAssociation','IncomingProductCode','TransactionProviderId','TransactionProviderName',
		'FileName','FileDate','AccountGroup3Code','AccountGroup3Name','ContractedRebateRate','IsBestOfPricingApplicable','CostCenter',
		'Supplier'
		]
		widgets = {
		'AccountNumber': forms.TextInput(attrs={'class':'form-control'}),
		'CustomerName1': forms.TextInput(attrs={'class':'form-control'}),
		'FullCardNumber': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoListPrice': forms.TextInput(attrs={'class':'form-control'}),
		'NetCustomerAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'CardSequenceNumber': forms.TextInput(attrs={'class':'form-control'}),
		'CheckDigit': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoGrossValue': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'DelcoVatAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'DelcoVatRate': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'RebateCustAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'VATNetAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'DelcoRebateRate': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'VoucherNumber': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'FleetId': forms.TextInput(attrs={'class':'form-control'}),
		'Quantity': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'DialogueIndicator': forms.TextInput(attrs={'class':'form-control'}),
		'IssuerCode1': forms.TextInput(attrs={'class':'form-control'}),
		'NetInvoiceIndicator': forms.TextInput(attrs={'class':'form-control'}),
		'NetworkCode': forms.TextInput(attrs={'class':'form-control'}),
		'CardGroupName': forms.TextInput(attrs={'class':'form-control'}),
		'CardHolderName': forms.TextInput(attrs={'class':'form-control'}),
		'CardVehicleRegistrationNumber': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'DeliveryNetAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'PinIndicator': forms.TextInput(attrs={'class':'form-control'}),
		'RebateType': forms.TextInput(attrs={'class':'form-control'}),
		'RecordType': forms.TextInput(attrs={'class':'form-control'}),
		'ReleaseCode': forms.TextInput(attrs={'class':'form-control'}),
		'Time': forms.TextInput(attrs={'class':'form-control','type':'time'}),
		'TransactionStatus': forms.TextInput(attrs={'class':'form-control'}),
		'TransactionType1': forms.TextInput(attrs={'class':'form-control'}),
		'VATIndicator': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'VatUsage': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'IssuerCountry': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoCode': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoCountryCode1': forms.TextInput(attrs={'class':'form-control'}),
		'TransactionCurrency': forms.TextInput(attrs={'class':'form-control'}),
		'InvoiceNumber': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'InvoiceDate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'ProductCode': forms.TextInput(attrs={'class':'form-control'}),
		'SiteCode': forms.TextInput(attrs={'class':'form-control'}),
		'Site': forms.TextInput(attrs={'class':'form-control'}),
		'DeliveryDate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'OdometerReading1': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoCustRate1': forms.TextInput(attrs={'class':'form-control'}),
		'CustomerCurrencyName1': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoPumpPrice': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'DelcoRebateAmount1': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'CustRebateRate1': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'PayerDisplayName': forms.TextInput(attrs={'class':'form-control'}),
		'PayerCode': forms.TextInput(attrs={'class':'form-control'}),
		'CardGroupID': forms.TextInput(attrs={'class':'form-control'}),
		'ProductName': forms.TextInput(attrs={'class':'form-control'}),
		'CreditDebitCode': forms.TextInput(attrs={'class':'form-control'}),
		'CorrectionFlag': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoCountryCode': forms.TextInput(attrs={'class':'form-control'}),
		'VATApplicable': forms.TextInput(attrs={'class':'form-control'}),
		'CustomerEuroRate': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoEuroRate': forms.TextInput(attrs={'class':'form-control'}),
		'EuroRebateAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'EuroVATAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'InvoiceSequenceNo': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'ListPriceInTransactionCurrency': forms.TextInput(attrs={'class':'form-control'}),
		'NetEuroAmount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'PumpPriceInTransactionCurrency': forms.TextInput(attrs={'class':'form-control'}),
		'RebateonNetAmountInCustomerCurrency': forms.TextInput(attrs={'class':'form-control'}),
		'RebateonNetAmountInTransactionCurrency': forms.TextInput(attrs={'class':'form-control'}),
		'RebateRate': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'UnInvoiceSequenceNo': forms.TextInput(attrs={'class':'form-control'}),
		'NetworkName': forms.TextInput(attrs={'class':'form-control'}),
		'Additional1': forms.TextInput(attrs={'class':'form-control'}),
		'Additional2': forms.TextInput(attrs={'class':'form-control'}),
		'Additional3': forms.TextInput(attrs={'class':'form-control'}),
		'Additional4': forms.TextInput(attrs={'class':'form-control'}),
		'TransactionIdentifier': forms.TextInput(attrs={'class':'form-control'}),
		'TransactionAuthorisationCode': forms.TextInput(attrs={'class':'form-control'}),
		'DelcoName': forms.TextInput(attrs={'class':'form-control'}),
		'SiteGroupid': forms.TextInput(attrs={'class':'form-control'}),
		'SiteGroupName': forms.TextInput(attrs={'class':'form-control'}),
		'Cardtype': forms.TextInput(attrs={'class':'form-control'}),
		'PayerGroup': forms.TextInput(attrs={'class':'form-control'}),
		'PayerNumber': forms.TextInput(attrs={'class':'form-control'}),
		'RefundFlag': forms.TextInput(attrs={'class':'form-control'}),
		'RefundOriginalTransactionId': forms.TextInput(attrs={'class':'form-control'}),
		'PostingDate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'PostingTime': forms.TextInput(attrs={'class':'form-control','type':'time'}),
		'CustomerReferenceValue': forms.TextInput(attrs={'class':'form-control'}),
		'CustomerReferenceDescription': forms.TextInput(attrs={'class':'form-control'}),
		'CardPayerAssociationCode': forms.TextInput(attrs={'class':'form-control'}),
		'CardPayerAssociation': forms.TextInput(attrs={'class':'form-control'}),
		'IncomingProductCode': forms.TextInput(attrs={'class':'form-control'}),
		'TransactionProviderId': forms.TextInput(attrs={'class':'form-control'}),
		'TransactionProviderName': forms.TextInput(attrs={'class':'form-control'}),
		'FileName': forms.TextInput(attrs={'class':'form-control'}),
		'FileDate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'AccountGroup3Code': forms.TextInput(attrs={'class':'form-control'}),
		'AccountGroup3Name': forms.TextInput(attrs={'class':'form-control'}),
		'ContractedRebateRate': forms.TextInput(attrs={'class':'form-control'}),
		'IsBestOfPricingApplicable': forms.TextInput(attrs={'class':'form-control'}),
		'CostCenter': forms.TextInput(attrs={'class':'form-control'}),
		'Supplier': forms.TextInput(attrs={'class':'form-control', 'value':'Shell','hidden':'true'})
		}