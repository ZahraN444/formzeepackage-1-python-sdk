# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Self(object):

    """Implementation of the 'Self' model.

    TODO: type model description here.

    Attributes:
        mself (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mself": 'self'
    }

    _optionals = [
        'mself',
    ]

    def __init__(self,
                 mself=APIHelper.SKIP):
        """Constructor for the Self class"""

        # Initialize members of the class
        if mself is not APIHelper.SKIP:
            self.mself = mself 

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
        mself = dictionary.get("self") if dictionary.get("self") else APIHelper.SKIP
        # Return an object of this model
        return cls(mself)
