# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class QueryResponseCharges(object):

    """Implementation of the 'QueryResponseCharges' model.

    TODO: type model description here.

    Attributes:
        account_number (str): TODO: type description here.
        account_number_code (str): TODO: type description here.
        amount (str): TODO: type description here.
        currency (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_number": 'account_number',
        "account_number_code": 'account_number_code',
        "amount": 'amount',
        "currency": 'currency'
    }

    _optionals = [
        'account_number',
        'account_number_code',
        'amount',
        'currency',
    ]

    def __init__(self,
                 account_number=APIHelper.SKIP,
                 account_number_code=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 currency=APIHelper.SKIP):
        """Constructor for the QueryResponseCharges class"""

        # Initialize members of the class
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_number_code is not APIHelper.SKIP:
            self.account_number_code = account_number_code 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if currency is not APIHelper.SKIP:
            self.currency = currency 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        account_number = dictionary.get("account_number") if dictionary.get("account_number") else APIHelper.SKIP
        account_number_code = dictionary.get("account_number_code") if dictionary.get("account_number_code") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_number,
                   account_number_code,
                   amount,
                   currency)
