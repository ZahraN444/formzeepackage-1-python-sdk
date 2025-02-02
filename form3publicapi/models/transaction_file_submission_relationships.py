# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.transaction_files import TransactionFiles


class TransactionFileSubmissionRelationships(object):

    """Implementation of the 'TransactionFileSubmissionRelationships' model.

    TODO: type model description here.

    Attributes:
        transaction_files (TransactionFiles): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_files": 'transaction_files'
    }

    _optionals = [
        'transaction_files',
    ]

    def __init__(self,
                 transaction_files=APIHelper.SKIP):
        """Constructor for the TransactionFileSubmissionRelationships class"""

        # Initialize members of the class
        if transaction_files is not APIHelper.SKIP:
            self.transaction_files = transaction_files 

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
        transaction_files = TransactionFiles.from_dictionary(dictionary.get('transaction_files')) if 'transaction_files' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(transaction_files)
