# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from form3publicapi.api_helper import APIHelper
import form3publicapi.exceptions.api_exception


class ApiErrorException(form3publicapi.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the ApiErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ApiErrorException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.error_code = dictionary.get("error_code") if dictionary.get("error_code") else None
        self.error_message = dictionary.get("error_message") if dictionary.get("error_message") else None
