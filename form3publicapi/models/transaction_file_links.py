# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.models.transaction_file_link import TransactionFileLink


class TransactionFileLinks(object):

    """Implementation of the 'TransactionFileLinks' model.

    TODO: type model description here.

    Attributes:
        mself (TransactionFileLink): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mself": 'self'
    }

    def __init__(self,
                 mself=None):
        """Constructor for the TransactionFileLinks class"""

        # Initialize members of the class
        self.mself = mself 

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
        mself = TransactionFileLink.from_dictionary(dictionary.get('self')) if dictionary.get('self') else None
        # Return an object of this model
        return cls(mself)
