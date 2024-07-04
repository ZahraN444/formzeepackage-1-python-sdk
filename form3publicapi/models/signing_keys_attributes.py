# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class SigningKeysAttributes(object):

    """Implementation of the 'SigningKeysAttributes' model.

    TODO: type model description here.

    Attributes:
        certificate (str): TODO: type description here.
        expiration_datetime (datetime): TODO: type description here.
        public_key (str): TODO: type description here.
        revocation_datetime (datetime): TODO: type description here.
        status (Status5Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "public_key": 'public_key',
        "certificate": 'certificate',
        "expiration_datetime": 'expiration_datetime',
        "revocation_datetime": 'revocation_datetime',
        "status": 'status'
    }

    _optionals = [
        'certificate',
        'expiration_datetime',
        'revocation_datetime',
        'status',
    ]

    def __init__(self,
                 public_key=None,
                 certificate=APIHelper.SKIP,
                 expiration_datetime=APIHelper.SKIP,
                 revocation_datetime=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the SigningKeysAttributes class"""

        # Initialize members of the class
        if certificate is not APIHelper.SKIP:
            self.certificate = certificate 
        if expiration_datetime is not APIHelper.SKIP:
            self.expiration_datetime = APIHelper.apply_datetime_converter(expiration_datetime, APIHelper.RFC3339DateTime) if expiration_datetime else None 
        self.public_key = public_key 
        if revocation_datetime is not APIHelper.SKIP:
            self.revocation_datetime = APIHelper.apply_datetime_converter(revocation_datetime, APIHelper.RFC3339DateTime) if revocation_datetime else None 
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
        public_key = dictionary.get("public_key") if dictionary.get("public_key") else None
        certificate = dictionary.get("certificate") if dictionary.get("certificate") else APIHelper.SKIP
        expiration_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("expiration_datetime")).datetime if dictionary.get("expiration_datetime") else APIHelper.SKIP
        revocation_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("revocation_datetime")).datetime if dictionary.get("revocation_datetime") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(public_key,
                   certificate,
                   expiration_datetime,
                   revocation_datetime,
                   status)