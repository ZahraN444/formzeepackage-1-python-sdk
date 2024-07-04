# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.account_holding_entity import AccountHoldingEntity


class MandateAttributesDebtorParty(object):

    """Implementation of the 'MandateAttributesDebtorParty' model.

    TODO: type model description here.

    Attributes:
        account_name (str): TODO: type description here.
        account_number (str): TODO: type description here.
        account_number_code (AccountNumberCodeEnum): The type of
            identification given at `account_number` attribute
        account_with (AccountHoldingEntity): Information about the financial
            institution servicing the account.
        address (List[str]): TODO: type description here.
        country (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'account_name',
        "account_number": 'account_number',
        "account_number_code": 'account_number_code',
        "account_with": 'account_with',
        "address": 'address',
        "country": 'country'
    }

    _optionals = [
        'account_name',
        'account_number',
        'account_number_code',
        'account_with',
        'address',
        'country',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_number_code=APIHelper.SKIP,
                 account_with=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 country=APIHelper.SKIP):
        """Constructor for the MandateAttributesDebtorParty class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_number_code is not APIHelper.SKIP:
            self.account_number_code = account_number_code 
        if account_with is not APIHelper.SKIP:
            self.account_with = account_with 
        if address is not APIHelper.SKIP:
            self.address = address 
        if country is not APIHelper.SKIP:
            self.country = country 

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
        account_name = dictionary.get("account_name") if dictionary.get("account_name") else APIHelper.SKIP
        account_number = dictionary.get("account_number") if dictionary.get("account_number") else APIHelper.SKIP
        account_number_code = dictionary.get("account_number_code") if dictionary.get("account_number_code") else APIHelper.SKIP
        account_with = AccountHoldingEntity.from_dictionary(dictionary.get('account_with')) if 'account_with' in dictionary.keys() else APIHelper.SKIP
        address = dictionary.get("address") if dictionary.get("address") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   account_number,
                   account_number_code,
                   account_with,
                   address,
                   country)
