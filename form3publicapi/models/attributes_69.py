# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes69(object):

    """Implementation of the 'Attributes69' model.

    TODO: type model description here.

    Attributes:
        error_category (str): TODO: type description here.
        error_message (str): TODO: type description here.
        occurred_on (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_category": 'error_category',
        "error_message": 'error_message',
        "occurred_on": 'occurred_on'
    }

    _optionals = [
        'error_category',
        'error_message',
        'occurred_on',
    ]

    def __init__(self,
                 error_category=APIHelper.SKIP,
                 error_message=APIHelper.SKIP,
                 occurred_on=APIHelper.SKIP):
        """Constructor for the Attributes69 class"""

        # Initialize members of the class
        if error_category is not APIHelper.SKIP:
            self.error_category = error_category 
        if error_message is not APIHelper.SKIP:
            self.error_message = error_message 
        if occurred_on is not APIHelper.SKIP:
            self.occurred_on = APIHelper.apply_datetime_converter(occurred_on, APIHelper.RFC3339DateTime) if occurred_on else None 

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
        error_category = dictionary.get("error_category") if dictionary.get("error_category") else APIHelper.SKIP
        error_message = dictionary.get("error_message") if dictionary.get("error_message") else APIHelper.SKIP
        occurred_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("occurred_on")).datetime if dictionary.get("occurred_on") else APIHelper.SKIP
        # Return an object of this model
        return cls(error_category,
                   error_message,
                   occurred_on)
