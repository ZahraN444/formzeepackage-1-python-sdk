# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from form3publicapi.api_helper import APIHelper


class Attributes9(object):

    """Implementation of the 'Attributes9' model.

    TODO: type model description here.

    Attributes:
        admission_datetime (datetime): Date and time the payment admission was
            created
        route (Route1Enum): Route taken for a return
        scheme_status_code (str): Refer to individual scheme where applicable
        scheme_status_code_description (str):
            [Description](http://api-docs.form3.tech/api.html#enumerations-sche
            me-status-codes-for-bacs) of `scheme_status_code`
        settlement_cycle (int): Cycle in which the payment will be settled
        settlement_date (date): Date on which the payment will be settled
        status (ReturnAdmissionStatusEnum):
            [Status](http://draft-api-docs.form3.tech/api.html#enumerations-pay
            ment-admission-status) of the return admission
        status_reason (str): Further explanation of the status. [See
            here](http://api-docs.form3.tech/api.html#enumerations-payment-admi
            ssion-status-reasons) for possible values.
        unique_scheme_id (str): Scheme-specific unique ID (42 character
            string)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "admission_datetime": 'admission_datetime',
        "route": 'route',
        "scheme_status_code": 'scheme_status_code',
        "scheme_status_code_description": 'scheme_status_code_description',
        "settlement_cycle": 'settlement_cycle',
        "settlement_date": 'settlement_date',
        "status": 'status',
        "status_reason": 'status_reason',
        "unique_scheme_id": 'unique_scheme_id'
    }

    _optionals = [
        'admission_datetime',
        'route',
        'scheme_status_code',
        'scheme_status_code_description',
        'settlement_cycle',
        'settlement_date',
        'status',
        'status_reason',
        'unique_scheme_id',
    ]

    def __init__(self,
                 admission_datetime=APIHelper.SKIP,
                 route=APIHelper.SKIP,
                 scheme_status_code=APIHelper.SKIP,
                 scheme_status_code_description=APIHelper.SKIP,
                 settlement_cycle=APIHelper.SKIP,
                 settlement_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 status_reason=APIHelper.SKIP,
                 unique_scheme_id=APIHelper.SKIP):
        """Constructor for the Attributes9 class"""

        # Initialize members of the class
        if admission_datetime is not APIHelper.SKIP:
            self.admission_datetime = APIHelper.apply_datetime_converter(admission_datetime, APIHelper.RFC3339DateTime) if admission_datetime else None 
        if route is not APIHelper.SKIP:
            self.route = route 
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
        if status_reason is not APIHelper.SKIP:
            self.status_reason = status_reason 
        if unique_scheme_id is not APIHelper.SKIP:
            self.unique_scheme_id = unique_scheme_id 

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
        route = dictionary.get("route") if dictionary.get("route") else APIHelper.SKIP
        scheme_status_code = dictionary.get("scheme_status_code") if dictionary.get("scheme_status_code") else APIHelper.SKIP
        scheme_status_code_description = dictionary.get("scheme_status_code_description") if dictionary.get("scheme_status_code_description") else APIHelper.SKIP
        settlement_cycle = dictionary.get("settlement_cycle") if dictionary.get("settlement_cycle") else APIHelper.SKIP
        settlement_date = dateutil.parser.parse(dictionary.get('settlement_date')).date() if dictionary.get('settlement_date') else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        status_reason = dictionary.get("status_reason") if dictionary.get("status_reason") else APIHelper.SKIP
        unique_scheme_id = dictionary.get("unique_scheme_id") if dictionary.get("unique_scheme_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(admission_datetime,
                   route,
                   scheme_status_code,
                   scheme_status_code_description,
                   settlement_cycle,
                   settlement_date,
                   status,
                   status_reason,
                   unique_scheme_id)
