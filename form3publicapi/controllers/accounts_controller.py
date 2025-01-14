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
from form3publicapi.models.account_details_list_response import AccountDetailsListResponse
from form3publicapi.models.account_creation_response import AccountCreationResponse
from form3publicapi.models.account_details_response import AccountDetailsResponse
from form3publicapi.models.account_event_list_response import AccountEventListResponse


class AccountsController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(AccountsController, self).__init__(config)

    def list_accounts(self,
                      page_number=None,
                      page_before=None,
                      page_after=None,
                      page_size=None,
                      filter_organisation_id=None,
                      filter_bank_id_code=None,
                      filter_bank_id=None,
                      filter_account_number=None,
                      filter_country=None,
                      filter_customer_id=None,
                      filter_iban=None):
        """Does a GET request to /organisation/accounts.

        List accounts

        Args:
            page_number (str, optional): Which page to select
            page_before (str, optional): Cursor value for getting previous
                page
            page_after (str, optional): Cursor value for getting next page
            page_size (int, optional): Number of items to select
            filter_organisation_id (List[uuid|str], optional): Filter by
                organisation id
            filter_bank_id_code (List[str], optional): Filter by type of bank
                id e.g. "GBDSC"
            filter_bank_id (List[str], optional): Filter by bank id e.g. sort
                code or bic
            filter_account_number (List[str], optional): Filter by account
                number
            filter_country (List[str], optional): Filter by country e.g.
                FR,GB
            filter_customer_id (List[str], optional): Filter by customer_id
            filter_iban (List[str], optional): Filter by IBAN

        Returns:
            AccountDetailsListResponse: Response from the API. List of account
                details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/accounts')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page[number]')
                         .value(page_number))
            .query_param(Parameter()
                         .key('page[before]')
                         .value(page_before))
            .query_param(Parameter()
                         .key('page[after]')
                         .value(page_after))
            .query_param(Parameter()
                         .key('page[size]')
                         .value(page_size))
            .query_param(Parameter()
                         .key('filter[organisation_id]')
                         .value(filter_organisation_id))
            .query_param(Parameter()
                         .key('filter[bank_id_code]')
                         .value(filter_bank_id_code))
            .query_param(Parameter()
                         .key('filter[bank_id]')
                         .value(filter_bank_id))
            .query_param(Parameter()
                         .key('filter[account_number]')
                         .value(filter_account_number))
            .query_param(Parameter()
                         .key('filter[country]')
                         .value(filter_country))
            .query_param(Parameter()
                         .key('filter[customer_id]')
                         .value(filter_customer_id))
            .query_param(Parameter()
                         .key('filter[iban]')
                         .value(filter_iban))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountDetailsListResponse.from_dictionary)
        ).execute()

    def create_account(self,
                       account_creation_request=None):
        """Does a POST request to /organisation/accounts.

        Create account

        Args:
            account_creation_request (AccountCreation, optional): TODO: type
                description here.

        Returns:
            AccountCreationResponse: Response from the API. Account creation
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/accounts')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(account_creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountCreationResponse.from_dictionary)
        ).execute()

    def delete_account(self,
                       id,
                       version):
        """Does a DELETE request to /organisation/accounts/{id}.

        Delete account

        Args:
            id (uuid|str): Account Id
            version (int): Version

        Returns:
            void: Response from the API. Account deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/accounts/{id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('version')
                         .value(version))
            .auth(Single('OAuth2'))
        ).execute()

    def fetch_account(self,
                      id):
        """Does a GET request to /organisation/accounts/{id}.

        Fetch account

        Args:
            id (uuid|str): Account Id

        Returns:
            AccountDetailsResponse: Response from the API. Account details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/accounts/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountDetailsResponse.from_dictionary)
        ).execute()

    def amend_account(self,
                      id,
                      account_amend_request=None):
        """Does a PATCH request to /organisation/accounts/{id}.

        Amend account

        Args:
            id (uuid|str): Account Id
            account_amend_request (AccountAmendment, optional): TODO: type
                description here.

        Returns:
            AccountDetailsResponse: Response from the API. Account updated

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/accounts/{id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(account_amend_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountDetailsResponse.from_dictionary)
        ).execute()

    def fetch_account_events(self,
                             id,
                             page_number=None,
                             page_size=None):
        """Does a GET request to /organisation/accounts/{id}/events.

        Fetch account events

        Args:
            id (uuid|str): Account Id
            page_number (str, optional): Which page to select
            page_size (int, optional): Number of items to select

        Returns:
            AccountEventListResponse: Response from the API. Account event
                list

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/accounts/{id}/events')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page[number]')
                         .value(page_number))
            .query_param(Parameter()
                         .key('page[size]')
                         .value(page_size))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountEventListResponse.from_dictionary)
        ).execute()
