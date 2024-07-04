# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.account_holding_entity import AccountHoldingEntity


class NewBankDetails(object):

    """Implementation of the 'NewBankDetails' model.

    TODO: type model description here.

    Attributes:
        account_number (str): TODO: type description here.
        account_number_code (AccountNumberCodeEnum): The type of
            identification given at `account_number` attribute
        account_with (AccountHoldingEntity): Information about the financial
            institution servicing the account.
        roll_number (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_number": 'account_number',
        "account_number_code": 'account_number_code',
        "account_with": 'account_with',
        "roll_number": 'roll_number'
    }

    _optionals = [
        'account_number',
        'account_number_code',
        'account_with',
        'roll_number',
    ]

    def __init__(self,
                 account_number=APIHelper.SKIP,
                 account_number_code=APIHelper.SKIP,
                 account_with=APIHelper.SKIP,
                 roll_number=APIHelper.SKIP):
        """Constructor for the NewBankDetails class"""

        # Initialize members of the class
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_number_code is not APIHelper.SKIP:
            self.account_number_code = account_number_code 
        if account_with is not APIHelper.SKIP:
            self.account_with = account_with 
        if roll_number is not APIHelper.SKIP:
            self.roll_number = roll_number 

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
        account_with = AccountHoldingEntity.from_dictionary(dictionary.get('account_with')) if 'account_with' in dictionary.keys() else APIHelper.SKIP
        roll_number = dictionary.get("roll_number") if dictionary.get("roll_number") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_number,
                   account_number_code,
                   account_with,
                   roll_number)
