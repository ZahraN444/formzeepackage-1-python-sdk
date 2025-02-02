# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.prometheus_metric_data import PrometheusMetricData


class MetricsQueryResponse(object):

    """Implementation of the 'MetricsQueryResponse' model.

    TODO: type model description here.

    Attributes:
        data (PrometheusMetricData): TODO: type description here.
        error (str): TODO: type description here.
        error_type (str): TODO: type description here.
        status (str): TODO: type description here.
        warnings (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "error": 'error',
        "error_type": 'errorType',
        "status": 'status',
        "warnings": 'warnings'
    }

    _optionals = [
        'data',
        'error',
        'error_type',
        'status',
        'warnings',
    ]

    def __init__(self,
                 data=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 error_type=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 warnings=APIHelper.SKIP):
        """Constructor for the MetricsQueryResponse class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 
        if error is not APIHelper.SKIP:
            self.error = error 
        if error_type is not APIHelper.SKIP:
            self.error_type = error_type 
        if status is not APIHelper.SKIP:
            self.status = status 
        if warnings is not APIHelper.SKIP:
            self.warnings = warnings 

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
        data = PrometheusMetricData.from_dictionary(dictionary.get('data')) if 'data' in dictionary.keys() else APIHelper.SKIP
        error = dictionary.get("error") if dictionary.get("error") else APIHelper.SKIP
        error_type = dictionary.get("errorType") if dictionary.get("errorType") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        warnings = dictionary.get("warnings") if dictionary.get("warnings") else APIHelper.SKIP
        # Return an object of this model
        return cls(data,
                   error,
                   error_type,
                   status,
                   warnings)
