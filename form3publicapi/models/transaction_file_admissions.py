# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.transaction_file_admission import TransactionFileAdmission


class TransactionFileAdmissions(object):

    """Implementation of the 'TransactionFileAdmissions' model.

    TODO: type model description here.

    Attributes:
        data (List[TransactionFileAdmission]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data'
    }

    _optionals = [
        'data',
    ]

    def __init__(self,
                 data=APIHelper.SKIP):
        """Constructor for the TransactionFileAdmissions class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 

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
        data = None
        if dictionary.get('data') is not None:
            data = [TransactionFileAdmission.from_dictionary(x) for x in dictionary.get('data')]
        else:
            data = APIHelper.SKIP
        # Return an object of this model
        return cls(data)