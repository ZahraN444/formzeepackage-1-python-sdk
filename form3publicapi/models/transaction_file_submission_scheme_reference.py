# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class TransactionFileSubmissionSchemeReference(object):

    """Implementation of the 'TransactionFileSubmissionSchemeReference' model.

    TODO: type model description here.

    Attributes:
        clearing_id (str): Service User Number (SUN) of the payment
            originator
        file_identifier (str): Submission serial number
        file_number (str): Number of the file sent to the scheme
        transaction_count (int): The count of transactions submitted in a
            given scheme file
        transaction_sum (str): The sum of transactions submitted in a given
            scheme file

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "clearing_id": 'clearing_id',
        "file_identifier": 'file_identifier',
        "file_number": 'file_number',
        "transaction_count": 'transaction_count',
        "transaction_sum": 'transaction_sum'
    }

    _optionals = [
        'clearing_id',
        'file_identifier',
        'file_number',
        'transaction_count',
        'transaction_sum',
    ]

    def __init__(self,
                 clearing_id=APIHelper.SKIP,
                 file_identifier=APIHelper.SKIP,
                 file_number=APIHelper.SKIP,
                 transaction_count=APIHelper.SKIP,
                 transaction_sum=APIHelper.SKIP):
        """Constructor for the TransactionFileSubmissionSchemeReference class"""

        # Initialize members of the class
        if clearing_id is not APIHelper.SKIP:
            self.clearing_id = clearing_id 
        if file_identifier is not APIHelper.SKIP:
            self.file_identifier = file_identifier 
        if file_number is not APIHelper.SKIP:
            self.file_number = file_number 
        if transaction_count is not APIHelper.SKIP:
            self.transaction_count = transaction_count 
        if transaction_sum is not APIHelper.SKIP:
            self.transaction_sum = transaction_sum 

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
        clearing_id = dictionary.get("clearing_id") if dictionary.get("clearing_id") else APIHelper.SKIP
        file_identifier = dictionary.get("file_identifier") if dictionary.get("file_identifier") else APIHelper.SKIP
        file_number = dictionary.get("file_number") if dictionary.get("file_number") else APIHelper.SKIP
        transaction_count = dictionary.get("transaction_count") if dictionary.get("transaction_count") else APIHelper.SKIP
        transaction_sum = dictionary.get("transaction_sum") if dictionary.get("transaction_sum") else APIHelper.SKIP
        # Return an object of this model
        return cls(clearing_id,
                   file_identifier,
                   file_number,
                   transaction_count,
                   transaction_sum)
