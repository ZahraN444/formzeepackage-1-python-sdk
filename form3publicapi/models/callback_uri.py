# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CallbackURI(object):

    """Implementation of the 'CallbackURI' model.

    TODO: type model description here.

    Attributes:
        callback_transport (CallbackTransportEnum): TODO: type description
            here.
        callback_uri (str): URI that will be called with the notification

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "callback_transport": 'callback_transport',
        "callback_uri": 'callback_uri'
    }

    def __init__(self,
                 callback_transport=None,
                 callback_uri=None):
        """Constructor for the CallbackURI class"""

        # Initialize members of the class
        self.callback_transport = callback_transport 
        self.callback_uri = callback_uri 

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
        callback_transport = dictionary.get("callback_transport") if dictionary.get("callback_transport") else None
        callback_uri = dictionary.get("callback_uri") if dictionary.get("callback_uri") else None
        # Return an object of this model
        return cls(callback_transport,
                   callback_uri)
