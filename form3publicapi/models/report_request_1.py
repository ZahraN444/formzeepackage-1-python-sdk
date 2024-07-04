# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.report_request import ReportRequest


class ReportRequest1(object):

    """Implementation of the 'ReportRequest1' model.

    TODO: type model description here.

    Attributes:
        data (List[ReportRequest]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data'
    }

    _optionals = [
        'data',
    ]

    def __init__(self,
                 data=APIHelper.SKIP):
        """Constructor for the ReportRequest1 class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 

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
        data = None
        if dictionary.get('data') is not None:
            data = [ReportRequest.from_dictionary(x) for x in dictionary.get('data')]
        else:
            data = APIHelper.SKIP
        # Return an object of this model
        return cls(data)