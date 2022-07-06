from dataclasses import dataclass, field
from datetime import date, datetime

@dataclass
class Orders:
    orderID: int
    customerID: int
    salesPersonID: int
    pickedByPersonID: int
    contactPersonID: int
    backorderOrderID: int
    orderDate: date
    expectedDeliverDate: date
    customerPurchaseOrderNumber: int
    isUndersupplyBackordered:bool
    comments: str
    deliveryInstructions: str
    internalComments: str
    pickingCompletedWhen: date
    lastEditedBy: int
    lastEditedWhen: datetime

    def __gt__(self, other):
        return self.orderID > other.orderID

    def __ge__(self, other):
        return self.orderID >= other.orderID

@dataclass
class Invoice:
    invoiceID: int
    customerID: int
    billToCustomerID: int
    orderID: int
    deliveryMethodID: int
    contactPersonID: int
    accountsPersonID: int
    salespersonPersonID: int
    packedByPersonID: int
    invoiceDate: date
    isCreditNote: bool
    creditNoteReason: str
    comment: str
    deliveryInstruction: str
    internalComment: str
    totalDrtItem: int
    totalChillerItem: int
    returnedDeliveryData: dict
    confirmedy: str

    def __gt__(self, other):
        return self.invoiceID > other.invoiceID

    def __ge__(self, other):
        return self.invoiceID >= other.invoiceID

@dataclass
class Customer:
    customerID: int
    customerName: str
    billToCustomerID: int
    customerCategoryID: int
    buyingGroupID: int
    primaryContactPersonID: int
    alternateContactPersonID: int
    deliveryCityID: int
    postalCityID: int
    creditLimit: float
    accountOpenedDate: date
    stanardDiscountPercentage: float
    isStatementSeng: bool
    isOnCreditHold: bool
    paymentDays: int
    phoneNumber: str
    faxNumber: str
    websiteURL: str
    deliveryAddressLine1: str
    deliveryAddressLine2: str
    deliveryPostalCode: int
    postalAddressLine1: str
    postalAddressLine2: str
    postalPostalCode: int
    lastEditedBy: int

