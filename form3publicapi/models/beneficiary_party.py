# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.new_bank_details import NewBankDetails


class BeneficiaryParty(object):

    """Implementation of the 'BeneficiaryParty' model.

    TODO: type model description here.

    Attributes:
        new_bank_details (NewBankDetails): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "new_bank_details": 'new_bank_details'
    }

    _optionals = [
        'new_bank_details',
    ]

    def __init__(self,
                 new_bank_details=APIHelper.SKIP):
        """Constructor for the BeneficiaryParty class"""

        # Initialize members of the class
        if new_bank_details is not APIHelper.SKIP:
            self.new_bank_details = new_bank_details 

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
        new_bank_details = NewBankDetails.from_dictionary(dictionary.get('new_bank_details')) if 'new_bank_details' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(new_bank_details)
