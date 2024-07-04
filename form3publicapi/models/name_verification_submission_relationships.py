# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.name_verification_1 import NameVerification1


class NameVerificationSubmissionRelationships(object):

    """Implementation of the 'NameVerificationSubmissionRelationships' model.

    TODO: type model description here.

    Attributes:
        name_verification (NameVerification1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name_verification": 'name_verification'
    }

    _optionals = [
        'name_verification',
    ]

    def __init__(self,
                 name_verification=APIHelper.SKIP):
        """Constructor for the NameVerificationSubmissionRelationships class"""

        # Initialize members of the class
        if name_verification is not APIHelper.SKIP:
            self.name_verification = name_verification 

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
        name_verification = NameVerification1.from_dictionary(dictionary.get('name_verification')) if 'name_verification' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name_verification)