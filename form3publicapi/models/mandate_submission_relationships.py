# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.mandate_2 import Mandate2


class MandateSubmissionRelationships(object):

    """Implementation of the 'MandateSubmissionRelationships' model.

    TODO: type model description here.

    Attributes:
        mandate (Mandate2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mandate": 'mandate'
    }

    _optionals = [
        'mandate',
    ]

    def __init__(self,
                 mandate=APIHelper.SKIP):
        """Constructor for the MandateSubmissionRelationships class"""

        # Initialize members of the class
        if mandate is not APIHelper.SKIP:
            self.mandate = mandate 

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
        mandate = Mandate2.from_dictionary(dictionary.get('mandate')) if 'mandate' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mandate)
