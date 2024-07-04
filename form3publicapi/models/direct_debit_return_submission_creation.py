# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.direct_debit_return_submission import DirectDebitReturnSubmission


class DirectDebitReturnSubmissionCreation(object):

    """Implementation of the 'DirectDebitReturnSubmissionCreation' model.

    TODO: type model description here.

    Attributes:
        data (DirectDebitReturnSubmission): TODO: type description here.

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
        """Constructor for the DirectDebitReturnSubmissionCreation class"""

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
        data = DirectDebitReturnSubmission.from_dictionary(dictionary.get('data')) if 'data' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(data)
