# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes50(object):

    """Implementation of the 'Attributes50' model.

    TODO: type model description here.

    Attributes:
        auto (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto": 'auto'
    }

    _optionals = [
        'auto',
    ]

    def __init__(self,
                 auto=APIHelper.SKIP):
        """Constructor for the Attributes50 class"""

        # Initialize members of the class
        if auto is not APIHelper.SKIP:
            self.auto = auto 

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
        auto = dictionary.get("auto") if "auto" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(auto)
