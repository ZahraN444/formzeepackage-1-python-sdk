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
from form3publicapi.models.organisation_details_list_response import OrganisationDetailsListResponse
from form3publicapi.models.organisation_creation_response import OrganisationCreationResponse
from form3publicapi.models.organisation_details_response import OrganisationDetailsResponse
from form3publicapi.exceptions.api_error_exception import ApiErrorException


class OrganisationsController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(OrganisationsController, self).__init__(config)

    def list_all_organisations(self,
                               filter_child_organisation_id=None,
                               filter_organisation_ids=None):
        """Does a GET request to /organisation/units.

        List all organisations

        Args:
            filter_child_organisation_id (uuid|str, optional): Child org id
            filter_organisation_ids (List[uuid|str], optional): Organisation
                ids

        Returns:
            OrganisationDetailsListResponse: Response from the API. List of
                organisation details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/units')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('filter[child_organisation_id]')
                         .value(filter_child_organisation_id))
            .query_param(Parameter()
                         .key('filter[organisation_ids]')
                         .value(filter_organisation_ids))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OrganisationDetailsListResponse.from_dictionary)
        ).execute()

    def create_organisation(self,
                            organisation_creation_request=None):
        """Does a POST request to /organisation/units.

        Create organisation

        Args:
            organisation_creation_request (OrganisationCreation, optional):
                TODO: type description here.

        Returns:
            OrganisationCreationResponse: Response from the API. Organisation
                creation response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/units')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(organisation_creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OrganisationCreationResponse.from_dictionary)
            .local_error('400', 'Bad Request', ApiErrorException)
            .local_error('409', 'Conflict', ApiErrorException)
        ).execute()

    def fetch_organisation(self,
                           id):
        """Does a GET request to /organisation/units/{id}.

        Fetch organisation

        Args:
            id (uuid|str): Organisation Id

        Returns:
            OrganisationDetailsResponse: Response from the API. Organisation
                details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/units/{id}')
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
            .deserialize_into(OrganisationDetailsResponse.from_dictionary)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()

    def update_organisation(self,
                            id,
                            organisation_update_request=None):
        """Does a PATCH request to /organisation/units/{id}.

        Update organisation

        Args:
            id (uuid|str): Organisation Id
            organisation_update_request (OrganisationUpdate, optional): TODO:
                type description here.

        Returns:
            OrganisationDetailsResponse: Response from the API. Organisation
                details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/units/{id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(organisation_update_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OrganisationDetailsResponse.from_dictionary)
            .local_error('400', 'Bad request', ApiErrorException)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()
