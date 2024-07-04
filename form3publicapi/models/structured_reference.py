# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class StructuredReference(object):

    """Implementation of the 'StructuredReference' model.

    TODO: type model description here.

    Attributes:
        issuer (str): Issuer of remittance reference
        reference (str): Unique reference to unambiguously refer to the
            payment originated by the creditor, this reference enables
            reconciliation by the creditor upon receipt of the amount of
            money.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "issuer": 'issuer',
        "reference": 'reference'
    }

    _optionals = [
        'issuer',
        'reference',
    ]

    def __init__(self,
                 issuer=APIHelper.SKIP,
                 reference=APIHelper.SKIP):
        """Constructor for the StructuredReference class"""

        # Initialize members of the class
        if issuer is not APIHelper.SKIP:
            self.issuer = issuer 
        if reference is not APIHelper.SKIP:
            self.reference = reference 

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
        issuer = dictionary.get("issuer") if dictionary.get("issuer") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        # Return an object of this model
        return cls(issuer,
                   reference)
