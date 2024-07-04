# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class RelationshipsQueryAdmissionProperties(object):

    """Implementation of the 'RelationshipsQueryAdmissionProperties' model.

    TODO: type model description here.

    Attributes:
        id (uuid|str): The query admission associated with this query
        mtype (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "mtype": 'type'
    }

    def __init__(self,
                 id=None):
        """Constructor for the RelationshipsQueryAdmissionProperties class"""

        # Initialize members of the class
        self.id = id 
        self.mtype = 'query_admissions' 

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
        # Return an object of this model
        return cls(id)
