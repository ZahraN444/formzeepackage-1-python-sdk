# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.scheme_files import SchemeFiles


class SchemeFileAdmissionRelationships(object):

    """Implementation of the 'SchemeFileAdmissionRelationships' model.

    TODO: type model description here.

    Attributes:
        scheme_files (SchemeFiles): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_files": 'scheme_files'
    }

    _optionals = [
        'scheme_files',
    ]

    def __init__(self,
                 scheme_files=APIHelper.SKIP):
        """Constructor for the SchemeFileAdmissionRelationships class"""

        # Initialize members of the class
        if scheme_files is not APIHelper.SKIP:
            self.scheme_files = scheme_files 

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
        scheme_files = SchemeFiles.from_dictionary(dictionary.get('scheme_files')) if 'scheme_files' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_files)
