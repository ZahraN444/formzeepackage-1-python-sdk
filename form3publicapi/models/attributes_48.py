# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from form3publicapi.api_helper import APIHelper
from form3publicapi.models.mandate_attributes import MandateAttributes


class Attributes48(object):

    """Implementation of the 'Attributes48' model.

    TODO: type model description here.

    Attributes:
        file_identifier (str): TODO: type description here.
        file_number (str): TODO: type description here.
        last_payment_date (date): TODO: type description here.
        original_mandate (MandateAttributes): TODO: type description here.
        status (MandateSubmissionStatusEnum): TODO: type description here.
        status_reason (str): TODO: type description here.
        submission_datetime (datetime): TODO: type description here.
        submission_reason (str): TODO: type description here.
        submitted_mandate (MandateAttributes): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_identifier": 'file_identifier',
        "file_number": 'file_number',
        "last_payment_date": 'last_payment_date',
        "original_mandate": 'original_mandate',
        "status": 'status',
        "status_reason": 'status_reason',
        "submission_datetime": 'submission_datetime',
        "submission_reason": 'submission_reason',
        "submitted_mandate": 'submitted_mandate'
    }

    _optionals = [
        'file_identifier',
        'file_number',
        'last_payment_date',
        'original_mandate',
        'status',
        'status_reason',
        'submission_datetime',
        'submission_reason',
        'submitted_mandate',
    ]

    def __init__(self,
                 file_identifier=APIHelper.SKIP,
                 file_number=APIHelper.SKIP,
                 last_payment_date=APIHelper.SKIP,
                 original_mandate=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 status_reason=APIHelper.SKIP,
                 submission_datetime=APIHelper.SKIP,
                 submission_reason=APIHelper.SKIP,
                 submitted_mandate=APIHelper.SKIP):
        """Constructor for the Attributes48 class"""

        # Initialize members of the class
        if file_identifier is not APIHelper.SKIP:
            self.file_identifier = file_identifier 
        if file_number is not APIHelper.SKIP:
            self.file_number = file_number 
        if last_payment_date is not APIHelper.SKIP:
            self.last_payment_date = last_payment_date 
        if original_mandate is not APIHelper.SKIP:
            self.original_mandate = original_mandate 
        if status is not APIHelper.SKIP:
            self.status = status 
        if status_reason is not APIHelper.SKIP:
            self.status_reason = status_reason 
        if submission_datetime is not APIHelper.SKIP:
            self.submission_datetime = APIHelper.apply_datetime_converter(submission_datetime, APIHelper.RFC3339DateTime) if submission_datetime else None 
        if submission_reason is not APIHelper.SKIP:
            self.submission_reason = submission_reason 
        if submitted_mandate is not APIHelper.SKIP:
            self.submitted_mandate = submitted_mandate 

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
        file_identifier = dictionary.get("file_identifier") if dictionary.get("file_identifier") else APIHelper.SKIP
        file_number = dictionary.get("file_number") if dictionary.get("file_number") else APIHelper.SKIP
        last_payment_date = dateutil.parser.parse(dictionary.get('last_payment_date')).date() if dictionary.get('last_payment_date') else APIHelper.SKIP
        original_mandate = MandateAttributes.from_dictionary(dictionary.get('original_mandate')) if 'original_mandate' in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        status_reason = dictionary.get("status_reason") if dictionary.get("status_reason") else APIHelper.SKIP
        submission_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("submission_datetime")).datetime if dictionary.get("submission_datetime") else APIHelper.SKIP
        submission_reason = dictionary.get("submission_reason") if dictionary.get("submission_reason") else APIHelper.SKIP
        submitted_mandate = MandateAttributes.from_dictionary(dictionary.get('submitted_mandate')) if 'submitted_mandate' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(file_identifier,
                   file_number,
                   last_payment_date,
                   original_mandate,
                   status,
                   status_reason,
                   submission_datetime,
                   submission_reason,
                   submitted_mandate)
