# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes36(object):

    """Implementation of the 'Attributes36' model.

    TODO: type model description here.

    Attributes:
        scheme_status_code (str): TODO: type description here.
        scheme_status_code_description (str): TODO: type description here.
        source_gateway (str): TODO: type description here.
        status (DirectDebitReversalAdmissionStatusEnum): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_status_code": 'scheme_status_code',
        "scheme_status_code_description": 'scheme_status_code_description',
        "source_gateway": 'source_gateway',
        "status": 'status'
    }

    _optionals = [
        'scheme_status_code',
        'scheme_status_code_description',
        'source_gateway',
        'status',
    ]

    def __init__(self,
                 scheme_status_code=APIHelper.SKIP,
                 scheme_status_code_description=APIHelper.SKIP,
                 source_gateway=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the Attributes36 class"""

        # Initialize members of the class
        if scheme_status_code is not APIHelper.SKIP:
            self.scheme_status_code = scheme_status_code 
        if scheme_status_code_description is not APIHelper.SKIP:
            self.scheme_status_code_description = scheme_status_code_description 
        if source_gateway is not APIHelper.SKIP:
            self.source_gateway = source_gateway 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        source_gateway = dictionary.get("source_gateway") if dictionary.get("source_gateway") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_status_code,
                   scheme_status_code_description,
                   source_gateway,
                   status)
