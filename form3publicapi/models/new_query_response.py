# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.models.query_response_attributes import QueryResponseAttributes


class NewQueryResponse(object):

    """Implementation of the 'NewQueryResponse' model.

    TODO: type model description here.

    Attributes:
        attributes (QueryResponseAttributes): TODO: type description here.
        id (uuid|str): TODO: type description here.
        organisation_id (uuid|str): TODO: type description here.
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes": 'attributes',
        "id": 'id',
        "organisation_id": 'organisation_id',
        "mtype": 'type'
    }

    def __init__(self,
                 attributes=None,
                 id=None,
                 organisation_id=None):
        """Constructor for the NewQueryResponse class"""

        # Initialize members of the class
        self.attributes = attributes 
        self.id = id 
        self.organisation_id = organisation_id 
        self.mtype = 'query_responses' 

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
        attributes = QueryResponseAttributes.from_dictionary(dictionary.get('attributes')) if dictionary.get('attributes') else None
        id = dictionary.get("id") if dictionary.get("id") else None
        organisation_id = dictionary.get("organisation_id") if dictionary.get("organisation_id") else None
        # Return an object of this model
        return cls(attributes,
                   id,
                   organisation_id)
