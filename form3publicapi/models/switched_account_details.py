# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from form3publicapi.api_helper import APIHelper
from form3publicapi.models.account_holding_entity import AccountHoldingEntity


class SwitchedAccountDetails(object):

    """Implementation of the 'SwitchedAccountDetails' model.

    Alternate Account details to use in case the account has been switched
    away from this organisation.

    Attributes:
        account_number (str): Switched account number. Must be a UK account
            number, maximum length 8 characters.
        account_number_code (str): ISO 20022 code used to identify the type of
            account number being used
        account_type (int): The type of the account provided in
            account_number. Only required if requested by the beneficiary
            party.
        account_with (AccountHoldingEntity): Information about the financial
            institution servicing the account.
        switched_effective_date (date): Starting date for the account to be
            effectively switched

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_number": 'account_number',
        "account_number_code": 'account_number_code',
        "account_with": 'account_with',
        "switched_effective_date": 'switched_effective_date',
        "account_type": 'account_type'
    }

    _optionals = [
        'account_type',
    ]

    def __init__(self,
                 account_number=None,
                 account_with=None,
                 switched_effective_date=None,
                 account_type=0):
        """Constructor for the SwitchedAccountDetails class"""

        # Initialize members of the class
        self.account_number = account_number 
        self.account_number_code = 'BBAN' 
        self.account_type = account_type 
        self.account_with = account_with 
        self.switched_effective_date = switched_effective_date 

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
        account_number = dictionary.get("account_number") if dictionary.get("account_number") else None
        account_with = AccountHoldingEntity.from_dictionary(dictionary.get('account_with')) if dictionary.get('account_with') else None
        switched_effective_date = dateutil.parser.parse(dictionary.get('switched_effective_date')).date() if dictionary.get('switched_effective_date') else None
        account_type = dictionary.get("account_type") if dictionary.get("account_type") else 0
        # Return an object of this model
        return cls(account_number,
                   account_with,
                   switched_effective_date,
                   account_type)
