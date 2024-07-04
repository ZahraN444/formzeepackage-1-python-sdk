# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.scheme_file_1 import SchemeFile1


class SchemeFileSubmissionRelationships(object):

    """Implementation of the 'SchemeFileSubmissionRelationships' model.

    TODO: type model description here.

    Attributes:
        scheme_file (SchemeFile1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_file": 'scheme_file'
    }

    _optionals = [
        'scheme_file',
    ]

    def __init__(self,
                 scheme_file=APIHelper.SKIP):
        """Constructor for the SchemeFileSubmissionRelationships class"""

        # Initialize members of the class
        if scheme_file is not APIHelper.SKIP:
            self.scheme_file = scheme_file 

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
        scheme_file = SchemeFile1.from_dictionary(dictionary.get('scheme_file')) if 'scheme_file' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_file)
