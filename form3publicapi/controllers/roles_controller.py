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
from form3publicapi.models.role_details_list_response import RoleDetailsListResponse
from form3publicapi.models.role_creation_response import RoleCreationResponse
from form3publicapi.models.role_details_response import RoleDetailsResponse
from form3publicapi.exceptions.api_error_exception import ApiErrorException


class RolesController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(RolesController, self).__init__(config)

    def list_all_roles(self,
                       page_number=None,
                       page_size=None):
        """Does a GET request to /security/roles.

        List all roles

        Args:
            page_number (int, optional): Which page to select
            page_size (int, optional): Number of items to select

        Returns:
            RoleDetailsListResponse: Response from the API. List of role
                details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/roles')
            .http_method(HttpMethodEnum.GET)
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
            .deserialize_into(RoleDetailsListResponse.from_dictionary)
        ).execute()

    def create_role(self,
                    role_creation_request=None):
        """Does a POST request to /security/roles.

        Create role

        Args:
            role_creation_request (RoleCreation, optional): TODO: type
                description here.

        Returns:
            RoleCreationResponse: Response from the API. Role creation
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/roles')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(role_creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RoleCreationResponse.from_dictionary)
            .local_error('400', 'Bad request', ApiErrorException)
            .local_error('409', 'Conflict', ApiErrorException)
        ).execute()

    def delete_role(self,
                    role_id,
                    version):
        """Does a DELETE request to /security/roles/{role_id}.

        Delete role

        Args:
            role_id (uuid|str): Role Id
            version (int): Version

        Returns:
            void: Response from the API. Role deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/roles/{role_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('role_id')
                            .value(role_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('version')
                         .value(version))
            .auth(Single('OAuth2'))
        ).execute()

    def fetch_role(self,
                   role_id):
        """Does a GET request to /security/roles/{role_id}.

        Fetch role

        Args:
            role_id (uuid|str): Role Id

        Returns:
            RoleDetailsResponse: Response from the API. Role details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/roles/{role_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('role_id')
                            .value(role_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RoleDetailsResponse.from_dictionary)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()
