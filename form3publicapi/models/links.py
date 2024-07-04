# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Links(object):

    """Implementation of the 'Links' model.

    TODO: type model description here.

    Attributes:
        first (str): Link to the first resource in the list
        last (str): Link to the last resource in the list
        next (str): Link to the next resource in the list
        prev (str): Link to the previous resource in the list
        mself (str): Link to this resource type

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mself": 'self',
        "first": 'first',
        "last": 'last',
        "next": 'next',
        "prev": 'prev'
    }

    _optionals = [
        'first',
        'last',
        'next',
        'prev',
    ]

    def __init__(self,
                 mself=None,
                 first=APIHelper.SKIP,
                 last=APIHelper.SKIP,
                 next=APIHelper.SKIP,
                 prev=APIHelper.SKIP):
        """Constructor for the Links class"""

        # Initialize members of the class
        if first is not APIHelper.SKIP:
            self.first = first 
        if last is not APIHelper.SKIP:
            self.last = last 
        if next is not APIHelper.SKIP:
            self.next = next 
        if prev is not APIHelper.SKIP:
            self.prev = prev 
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
        mself = dictionary.get("self") if dictionary.get("self") else None
        first = dictionary.get("first") if dictionary.get("first") else APIHelper.SKIP
        last = dictionary.get("last") if dictionary.get("last") else APIHelper.SKIP
        next = dictionary.get("next") if dictionary.get("next") else APIHelper.SKIP
        prev = dictionary.get("prev") if dictionary.get("prev") else APIHelper.SKIP
        # Return an object of this model
        return cls(mself,
                   first,
                   last,
                   next,
                   prev)