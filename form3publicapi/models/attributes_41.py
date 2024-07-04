# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes41(object):

    """Implementation of the 'Attributes41' model.

    TODO: type model description here.

    Attributes:
        start_datetime (datetime): Time the submission request was received by
            Form3. Used to compute the total processing time
        status (SchemeFileSubmissionStatusEnum): Status of the scheme file
            submission
        status_reason (str): Plain-text description of the status attribute
        submission_datetime (datetime): Time when the Form3 system begins
            processing of the submission

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_datetime": 'start_datetime',
        "status": 'status',
        "status_reason": 'status_reason',
        "submission_datetime": 'submission_datetime'
    }

    _optionals = [
        'start_datetime',
        'status',
        'status_reason',
        'submission_datetime',
    ]

    def __init__(self,
                 start_datetime=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 status_reason=APIHelper.SKIP,
                 submission_datetime=APIHelper.SKIP):
        """Constructor for the Attributes41 class"""

        # Initialize members of the class
        if start_datetime is not APIHelper.SKIP:
            self.start_datetime = APIHelper.apply_datetime_converter(start_datetime, APIHelper.RFC3339DateTime) if start_datetime else None 
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
        start_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_datetime")).datetime if dictionary.get("start_datetime") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        status_reason = dictionary.get("status_reason") if dictionary.get("status_reason") else APIHelper.SKIP
        submission_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("submission_datetime")).datetime if dictionary.get("submission_datetime") else APIHelper.SKIP
        # Return an object of this model
        return cls(start_datetime,
                   status,
                   status_reason,
                   submission_datetime)
