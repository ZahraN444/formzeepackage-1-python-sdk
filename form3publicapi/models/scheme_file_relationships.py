# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.scheme_file_admissions import SchemeFileAdmissions
from form3publicapi.models.scheme_file_submission_2 import SchemeFileSubmission2


class SchemeFileRelationships(object):

    """Implementation of the 'SchemeFileRelationships' model.

    TODO: type model description here.

    Attributes:
        scheme_file_admissions (SchemeFileAdmissions): TODO: type description
            here.
        scheme_file_submission (SchemeFileSubmission2): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_file_admissions": 'scheme_file_admissions',
        "scheme_file_submission": 'scheme_file_submission'
    }

    _optionals = [
        'scheme_file_admissions',
        'scheme_file_submission',
    ]

    def __init__(self,
                 scheme_file_admissions=APIHelper.SKIP,
                 scheme_file_submission=APIHelper.SKIP):
        """Constructor for the SchemeFileRelationships class"""

        # Initialize members of the class
        if scheme_file_admissions is not APIHelper.SKIP:
            self.scheme_file_admissions = scheme_file_admissions 
        if scheme_file_submission is not APIHelper.SKIP:
            self.scheme_file_submission = scheme_file_submission 

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
        scheme_file_admissions = SchemeFileAdmissions.from_dictionary(dictionary.get('scheme_file_admissions')) if 'scheme_file_admissions' in dictionary.keys() else APIHelper.SKIP
        scheme_file_submission = SchemeFileSubmission2.from_dictionary(dictionary.get('scheme_file_submission')) if 'scheme_file_submission' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_file_admissions,
                   scheme_file_submission)
