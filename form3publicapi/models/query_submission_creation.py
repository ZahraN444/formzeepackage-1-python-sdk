# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.models.new_query_submission import NewQuerySubmission


class QuerySubmissionCreation(object):

    """Implementation of the 'QuerySubmissionCreation' model.

    TODO: type model description here.

    Attributes:
        data (NewQuerySubmission): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data'
    }

    def __init__(self,
                 data=None):
        """Constructor for the QuerySubmissionCreation class"""

        # Initialize members of the class
        self.data = data 

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
        data = NewQuerySubmission.from_dictionary(dictionary.get('data')) if dictionary.get('data') else None
        # Return an object of this model
        return cls(data)
