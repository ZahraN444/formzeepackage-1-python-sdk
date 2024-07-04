# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Attributes20(object):

    """Implementation of the 'Attributes20' model.

    TODO: type model description here.

    Attributes:
        original_instruction_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "original_instruction_id": 'original_instruction_id'
    }

    def __init__(self,
                 original_instruction_id=None):
        """Constructor for the Attributes20 class"""

        # Initialize members of the class
        self.original_instruction_id = original_instruction_id 

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
        original_instruction_id = dictionary.get("original_instruction_id") if dictionary.get("original_instruction_id") else None
        # Return an object of this model
        return cls(original_instruction_id)
