# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.direct_debit_reversal import DirectDebitReversal
from form3publicapi.models.links import Links


class DirectDebitReversalCreationResponse(object):

    """Implementation of the 'DirectDebitReversalCreationResponse' model.

    TODO: type model description here.

    Attributes:
        data (DirectDebitReversal): TODO: type description here.
        links (Links): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "links": 'links'
    }

    _optionals = [
        'data',
        'links',
    ]

    def __init__(self,
                 data=APIHelper.SKIP,
                 links=APIHelper.SKIP):
        """Constructor for the DirectDebitReversalCreationResponse class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 
        if links is not APIHelper.SKIP:
            self.links = links 

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
        data = DirectDebitReversal.from_dictionary(dictionary.get('data')) if 'data' in dictionary.keys() else APIHelper.SKIP
        links = Links.from_dictionary(dictionary.get('links')) if 'links' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(data,
                   links)
