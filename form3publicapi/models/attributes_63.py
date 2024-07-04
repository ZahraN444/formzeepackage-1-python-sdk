# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes63(object):

    """Implementation of the 'Attributes63' model.

    TODO: type model description here.

    Attributes:
        scheme_status_code (str): Scheme-specific status code. Refer to
            individual scheme where applicable
        scheme_status_code_description (str):
            [Description](http://draft-api-docs.form3.tech/api.html#enumeration
            s-scheme-status-codes-for-bacs) of scheme_status_code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_status_code": 'scheme_status_code',
        "scheme_status_code_description": 'scheme_status_code_description'
    }

    _optionals = [
        'scheme_status_code',
        'scheme_status_code_description',
    ]

    def __init__(self,
                 scheme_status_code=APIHelper.SKIP,
                 scheme_status_code_description=APIHelper.SKIP):
        """Constructor for the Attributes63 class"""

        # Initialize members of the class
        if scheme_status_code is not APIHelper.SKIP:
            self.scheme_status_code = scheme_status_code 
        if scheme_status_code_description is not APIHelper.SKIP:
            self.scheme_status_code_description = scheme_status_code_description 

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
        scheme_status_code = dictionary.get("scheme_status_code") if dictionary.get("scheme_status_code") else APIHelper.SKIP
        scheme_status_code_description = dictionary.get("scheme_status_code_description") if dictionary.get("scheme_status_code_description") else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_status_code,
                   scheme_status_code_description)
