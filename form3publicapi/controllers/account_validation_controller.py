# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from form3publicapi.api_helper import APIHelper
from form3publicapi.configuration import Server
from form3publicapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from form3publicapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from form3publicapi.models.sort_code_details_response import SortCodeDetailsResponse
from form3publicapi.models.account_number_details_response import AccountNumberDetailsResponse
from form3publicapi.exceptions.api_error_exception import ApiErrorException


class AccountValidationController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(AccountValidationController, self).__init__(config)

    def fetch_sort_code_details(self,
                                sortcode):
        """Does a GET request to /validations/gbdsc/sortcodes/{sortcode}.

        Fetch sort code details

        Args:
            sortcode (str): Sort code

        Returns:
            SortCodeDetailsResponse: Response from the API. Sort code details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/validations/gbdsc/sortcodes/{sortcode}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('sortcode')
                            .value(sortcode)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SortCodeDetailsResponse.from_dictionary)
            .local_error('400', 'Validation failed', ApiErrorException)
        ).execute()

    def validate_sortcode_and_account_number_details(self,
                                                     sortcode,
                                                     accountnumber):
        """Does a GET request to /validations/gbdsc/sortcodes/{sortcode}/accountnumbers/{accountnumber}.

        Validate sortcode and account number details

        Args:
            sortcode (str): Sort code
            accountnumber (str): Account number

        Returns:
            AccountNumberDetailsResponse: Response from the API. Sort code and
                account number details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/validations/gbdsc/sortcodes/{sortcode}/accountnumbers/{accountnumber}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('sortcode')
                            .value(sortcode)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('accountnumber')
                            .value(accountnumber)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountNumberDetailsResponse.from_dictionary)
            .local_error('400', 'Validation error', ApiErrorException)
            .local_error('404', 'Validation failed', ApiErrorException)
        ).execute()