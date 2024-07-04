# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class ReversalAmount(object):

    """Implementation of the 'ReversalAmount' model.

    SEPA only

    Attributes:
        amount (str): Full amount of the Direct Debit Reversal including
            charges
        currency (str): ISO currency code for `amount`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "currency": 'currency'
    }

    _optionals = [
        'amount',
        'currency',
    ]

    def __init__(self,
                 amount=APIHelper.SKIP,
                 currency=APIHelper.SKIP):
        """Constructor for the ReversalAmount class"""

        # Initialize members of the class
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
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   currency)
