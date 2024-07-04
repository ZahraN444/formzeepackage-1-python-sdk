# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from form3publicapi.api_helper import APIHelper


class Attributes32(object):

    """Implementation of the 'Attributes32' model.

    TODO: type model description here.

    Attributes:
        admission_datetime (datetime): TODO: type description here.
        scheme_status_code (str): TODO: type description here.
        scheme_status_code_description (str): TODO: type description here.
        settlement_cycle (int): TODO: type description here.
        settlement_date (date): TODO: type description here.
        status (DirectDebitReturnAdmissionStatusEnum): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "admission_datetime": 'admission_datetime',
        "scheme_status_code": 'scheme_status_code',
        "scheme_status_code_description": 'scheme_status_code_description',
        "settlement_cycle": 'settlement_cycle',
        "settlement_date": 'settlement_date',
        "status": 'status'
    }

    _optionals = [
        'admission_datetime',
        'scheme_status_code',
        'scheme_status_code_description',
        'settlement_cycle',
        'settlement_date',
        'status',
    ]

    def __init__(self,
                 admission_datetime=APIHelper.SKIP,
                 scheme_status_code=APIHelper.SKIP,
                 scheme_status_code_description=APIHelper.SKIP,
                 settlement_cycle=APIHelper.SKIP,
                 settlement_date=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the Attributes32 class"""

        # Initialize members of the class
        if admission_datetime is not APIHelper.SKIP:
            self.admission_datetime = APIHelper.apply_datetime_converter(admission_datetime, APIHelper.RFC3339DateTime) if admission_datetime else None 
        if scheme_status_code is not APIHelper.SKIP:
            self.scheme_status_code = scheme_status_code 
        if scheme_status_code_description is not APIHelper.SKIP:
            self.scheme_status_code_description = scheme_status_code_description 
        if settlement_cycle is not APIHelper.SKIP:
            self.settlement_cycle = settlement_cycle 
        if settlement_date is not APIHelper.SKIP:
            self.settlement_date = settlement_date 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        admission_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("admission_datetime")).datetime if dictionary.get("admission_datetime") else APIHelper.SKIP
        scheme_status_code = dictionary.get("scheme_status_code") if dictionary.get("scheme_status_code") else APIHelper.SKIP
        scheme_status_code_description = dictionary.get("scheme_status_code_description") if dictionary.get("scheme_status_code_description") else APIHelper.SKIP
        settlement_cycle = dictionary.get("settlement_cycle") if dictionary.get("settlement_cycle") else APIHelper.SKIP
        settlement_date = dateutil.parser.parse(dictionary.get('settlement_date')).date() if dictionary.get('settlement_date') else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(admission_datetime,
                   scheme_status_code,
                   scheme_status_code_description,
                   settlement_cycle,
                   settlement_date,
                   status)
