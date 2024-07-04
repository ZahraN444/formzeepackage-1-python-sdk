# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes37(object):

    """Implementation of the 'Attributes37' model.

    TODO: type model description here.

    Attributes:
        destination_gateway (str): TODO: type description here.
        scheme_status_code (str): TODO: type description here.
        scheme_status_code_description (str): TODO: type description here.
        status (DirectDebitReversalSubmissionStatusEnum): TODO: type
            description here.
        status_reason (str): TODO: type description here.
        submission_datetime (datetime): TODO: type description here.
        transaction_start_datetime (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "destination_gateway": 'destination_gateway',
        "scheme_status_code": 'scheme_status_code',
        "scheme_status_code_description": 'scheme_status_code_description',
        "status": 'status',
        "status_reason": 'status_reason',
        "submission_datetime": 'submission_datetime',
        "transaction_start_datetime": 'transaction_start_datetime'
    }

    _optionals = [
        'destination_gateway',
        'scheme_status_code',
        'scheme_status_code_description',
        'status',
        'status_reason',
        'submission_datetime',
        'transaction_start_datetime',
    ]

    def __init__(self,
                 destination_gateway=APIHelper.SKIP,
                 scheme_status_code=APIHelper.SKIP,
                 scheme_status_code_description=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 status_reason=APIHelper.SKIP,
                 submission_datetime=APIHelper.SKIP,
                 transaction_start_datetime=APIHelper.SKIP):
        """Constructor for the Attributes37 class"""

        # Initialize members of the class
        if destination_gateway is not APIHelper.SKIP:
            self.destination_gateway = destination_gateway 
        if scheme_status_code is not APIHelper.SKIP:
            self.scheme_status_code = scheme_status_code 
        if scheme_status_code_description is not APIHelper.SKIP:
            self.scheme_status_code_description = scheme_status_code_description 
        if status is not APIHelper.SKIP:
            self.status = status 
        if status_reason is not APIHelper.SKIP:
            self.status_reason = status_reason 
        if submission_datetime is not APIHelper.SKIP:
            self.submission_datetime = APIHelper.apply_datetime_converter(submission_datetime, APIHelper.RFC3339DateTime) if submission_datetime else None 
        if transaction_start_datetime is not APIHelper.SKIP:
            self.transaction_start_datetime = APIHelper.apply_datetime_converter(transaction_start_datetime, APIHelper.RFC3339DateTime) if transaction_start_datetime else None 

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
        destination_gateway = dictionary.get("destination_gateway") if dictionary.get("destination_gateway") else APIHelper.SKIP
        scheme_status_code = dictionary.get("scheme_status_code") if dictionary.get("scheme_status_code") else APIHelper.SKIP
        scheme_status_code_description = dictionary.get("scheme_status_code_description") if dictionary.get("scheme_status_code_description") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        status_reason = dictionary.get("status_reason") if dictionary.get("status_reason") else APIHelper.SKIP
        submission_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("submission_datetime")).datetime if dictionary.get("submission_datetime") else APIHelper.SKIP
        transaction_start_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_start_datetime")).datetime if dictionary.get("transaction_start_datetime") else APIHelper.SKIP
        # Return an object of this model
        return cls(destination_gateway,
                   scheme_status_code,
                   scheme_status_code_description,
                   status,
                   status_reason,
                   submission_datetime,
                   transaction_start_datetime)