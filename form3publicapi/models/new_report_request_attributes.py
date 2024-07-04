# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.models.new_report_request_filter import NewReportRequestFilter


class NewReportRequestAttributes(object):

    """Implementation of the 'NewReportRequestAttributes' model.

    TODO: type model description here.

    Attributes:
        filter (NewReportRequestFilter): TODO: type description here.
        payment_scheme (str): TODO: type description here.
        report_type (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filter": 'filter',
        "payment_scheme": 'payment_scheme',
        "report_type": 'report_type'
    }

    def __init__(self,
                 filter=None,
                 payment_scheme=None,
                 report_type=None):
        """Constructor for the NewReportRequestAttributes class"""

        # Initialize members of the class
        self.filter = filter 
        self.payment_scheme = payment_scheme 
        self.report_type = report_type 

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
        filter = NewReportRequestFilter.from_dictionary(dictionary.get('filter')) if dictionary.get('filter') else None
        payment_scheme = dictionary.get("payment_scheme") if dictionary.get("payment_scheme") else None
        report_type = dictionary.get("report_type") if dictionary.get("report_type") else None
        # Return an object of this model
        return cls(filter,
                   payment_scheme,
                   report_type)
