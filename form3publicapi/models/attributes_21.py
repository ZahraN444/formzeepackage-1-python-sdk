# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes21(object):

    """Implementation of the 'Attributes21' model.

    TODO: type model description here.

    Attributes:
        status (ClaimSubmissionStatusEnum): TODO: type description here.
        status_reason (str): TODO: type description here.
        submission_datetime (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "status_reason": 'status_reason',
        "submission_datetime": 'submission_datetime'
    }

    _optionals = [
        'status',
        'status_reason',
        'submission_datetime',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 status_reason=APIHelper.SKIP,
                 submission_datetime=APIHelper.SKIP):
        """Constructor for the Attributes21 class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        if status_reason is not APIHelper.SKIP:
            self.status_reason = status_reason 
        if submission_datetime is not APIHelper.SKIP:
            self.submission_datetime = APIHelper.apply_datetime_converter(submission_datetime, APIHelper.RFC3339DateTime) if submission_datetime else None 

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
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        status_reason = dictionary.get("status_reason") if dictionary.get("status_reason") else APIHelper.SKIP
        submission_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("submission_datetime")).datetime if dictionary.get("submission_datetime") else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   status_reason,
                   submission_datetime)
