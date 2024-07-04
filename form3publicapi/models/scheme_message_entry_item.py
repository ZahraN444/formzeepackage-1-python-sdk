# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class SchemeMessageEntryItem(object):

    """Implementation of the 'SchemeMessageEntryItem' model.

    TODO: type model description here.

    Attributes:
        key (str): TODO: type description here.
        value (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    _optionals = [
        'value',
    ]

    def __init__(self,
                 key=None,
                 value=APIHelper.SKIP):
        """Constructor for the SchemeMessageEntryItem class"""

        # Initialize members of the class
        self.key = key 
        if value is not APIHelper.SKIP:
            self.value = value 

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
        key = dictionary.get("key") if dictionary.get("key") else None
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        # Return an object of this model
        return cls(key,
                   value)