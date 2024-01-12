from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *
from dotenv import load_dotenv
import os

import collections
collections.MutableSequence = collections.abc.MutableSequence

load_dotenv()

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = os.getenv("CREDIT_CARD_ID")
merchantAuth.transactionKey = os.getenv("CREDIT_CARD_KEY")

creditCard = apicontractsv1.creditCardType()
creditCard.cardNumber = "4111111111111111"
creditCard.expirationDate = "2024-12"
 
payment = apicontractsv1.paymentType()
payment.creditCard = creditCard