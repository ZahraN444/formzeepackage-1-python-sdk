# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.user_defined_data import UserDefinedData


class Attributes6(object):

    """Implementation of the 'Attributes6' model.

    TODO: type model description here.

    Attributes:
        user_defined_data (List[UserDefinedData]): All purpose list of
            key-value pairs specific data stored on the associated beneficiary
            account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_defined_data": 'user_defined_data'
    }

    _optionals = [
        'user_defined_data',
    ]

    def __init__(self,
                 user_defined_data=APIHelper.SKIP):
        """Constructor for the Attributes6 class"""

        # Initialize members of the class
        if user_defined_data is not APIHelper.SKIP:
            self.user_defined_data = user_defined_data 

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
        user_defined_data = None
        if dictionary.get('user_defined_data') is not None:
            user_defined_data = [UserDefinedData.from_dictionary(x) for x in dictionary.get('user_defined_data')]
        else:
            user_defined_data = APIHelper.SKIP
        # Return an object of this model
        return cls(user_defined_data)
