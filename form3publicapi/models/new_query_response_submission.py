# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.attributes_50 import Attributes50


class NewQueryResponseSubmission(object):

    """Implementation of the 'NewQueryResponseSubmission' model.

    TODO: type model description here.

    Attributes:
        attributes (Attributes50): TODO: type description here.
        id (uuid|str): TODO: type description here.
        organisation_id (uuid|str): TODO: type description here.
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "organisation_id": 'organisation_id',
        "mtype": 'type',
        "attributes": 'attributes'
    }

    _optionals = [
        'attributes',
    ]

    def __init__(self,
                 id=None,
                 organisation_id=None,
                 attributes=APIHelper.SKIP):
        """Constructor for the NewQueryResponseSubmission class"""

        # Initialize members of the class
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 
        self.id = id 
        self.organisation_id = organisation_id 
        self.mtype = 'query_response_submissions' 

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
        id = dictionary.get("id") if dictionary.get("id") else None
        organisation_id = dictionary.get("organisation_id") if dictionary.get("organisation_id") else None
        attributes = Attributes50.from_dictionary(dictionary.get('attributes')) if 'attributes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   organisation_id,
                   attributes)