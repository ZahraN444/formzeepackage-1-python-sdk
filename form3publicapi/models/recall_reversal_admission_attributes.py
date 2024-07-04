# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class RecallReversalAdmissionAttributes(object):

    """Implementation of the 'RecallReversalAdmissionAttributes' model.

    TODO: type model description here.

    Attributes:
        scheme_status_code (str): Scheme-specific status code
        source_gateway (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_status_code": 'scheme_status_code',
        "source_gateway": 'source_gateway'
    }

    _optionals = [
        'scheme_status_code',
        'source_gateway',
    ]

    def __init__(self,
                 scheme_status_code=APIHelper.SKIP,
                 source_gateway=APIHelper.SKIP):
        """Constructor for the RecallReversalAdmissionAttributes class"""

        # Initialize members of the class
        if scheme_status_code is not APIHelper.SKIP:
            self.scheme_status_code = scheme_status_code 
        if source_gateway is not APIHelper.SKIP:
            self.source_gateway = source_gateway 

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
        source_gateway = dictionary.get("source_gateway") if dictionary.get("source_gateway") else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_status_code,
                   source_gateway)
