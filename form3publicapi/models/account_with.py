# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class AccountWith(object):

    """Implementation of the 'AccountWith' model.

    Debtor/Beneficiary agents bank information.

    Attributes:
        bank_id (str): Identification of a member of a clearing system.
        bank_id_code (str): Identification of a clearing system, in a coded
            form as published in an external list.
        bank_name (str): Name by which an agent is known and which is usually
            used to identify that agent.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_id": 'bank_id',
        "bank_id_code": 'bank_id_code',
        "bank_name": 'bank_name'
    }

    _optionals = [
        'bank_id',
        'bank_id_code',
        'bank_name',
    ]

    def __init__(self,
                 bank_id=APIHelper.SKIP,
                 bank_id_code=APIHelper.SKIP,
                 bank_name=APIHelper.SKIP):
        """Constructor for the AccountWith class"""

        # Initialize members of the class
        if bank_id is not APIHelper.SKIP:
            self.bank_id = bank_id 
        if bank_id_code is not APIHelper.SKIP:
            self.bank_id_code = bank_id_code 
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name 

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
        bank_id = dictionary.get("bank_id") if dictionary.get("bank_id") else APIHelper.SKIP
        bank_id_code = dictionary.get("bank_id_code") if dictionary.get("bank_id_code") else APIHelper.SKIP
        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(bank_id,
                   bank_id_code,
                   bank_name)