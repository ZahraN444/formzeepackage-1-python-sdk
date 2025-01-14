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
from form3publicapi.models.user_details_list_response import UserDetailsListResponse
from form3publicapi.models.user_creation_response import UserCreationResponse
from form3publicapi.models.user_details_response import UserDetailsResponse
from form3publicapi.models.ace_details_list_response import AceDetailsListResponse
from form3publicapi.models.user_credential_list_response import UserCredentialListResponse
from form3publicapi.models.credential_creation_response import CredentialCreationResponse
from form3publicapi.models.user_role_list_response import UserRoleListResponse
from form3publicapi.exceptions.api_error_exception import ApiErrorException


class UsersController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(UsersController, self).__init__(config)

    def list_all_users(self,
                       page_number=None,
                       page_size=None):
        """Does a GET request to /security/users.

        List all users

        Args:
            page_number (int, optional): Which page to select
            page_size (int, optional): Number of items to select

        Returns:
            UserDetailsListResponse: Response from the API. List of user
                details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users')
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
            .deserialize_into(UserDetailsListResponse.from_dictionary)
        ).execute()

    def create_user(self,
                    user_creation_request=None):
        """Does a POST request to /security/users.

        Create user

        Args:
            user_creation_request (UserCreation, optional): TODO: type
                description here.

        Returns:
            UserCreationResponse: Response from the API. User creation
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(user_creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UserCreationResponse.from_dictionary)
            .local_error('400', 'Bad request', ApiErrorException)
            .local_error('409', 'Conflict', ApiErrorException)
        ).execute()

    def delete_user(self,
                    user_id,
                    version):
        """Does a DELETE request to /security/users/{user_id}.

        Delete user

        Args:
            user_id (uuid|str): User Id
            version (int): Version

        Returns:
            void: Response from the API. User deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('version')
                         .value(version))
            .auth(Single('OAuth2'))
        ).execute()

    def fetch_user(self,
                   user_id):
        """Does a GET request to /security/users/{user_id}.

        Fetch user

        Args:
            user_id (uuid|str): User Id

        Returns:
            UserDetailsResponse: Response from the API. User details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UserDetailsResponse.from_dictionary)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()

    def update_user_details(self,
                            user_id,
                            user_update_request=None):
        """Does a PATCH request to /security/users/{user_id}.

        Update user details

        Args:
            user_id (uuid|str): User Id
            user_update_request (UserCreation, optional): TODO: type
                description here.

        Returns:
            UserDetailsResponse: Response from the API. User details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(user_update_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UserDetailsResponse.from_dictionary)
            .local_error('400', 'Bad request', ApiErrorException)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()

    def fetch_access_control_list_for_user(self,
                                           user_id,
                                           filter_record_type=None,
                                           filter_action=None):
        """Does a GET request to /security/users/{user_id}/aces.

        Fetch access control list for user

        Args:
            user_id (uuid|str): User Id
            filter_record_type (str, optional): Record type
            filter_action (str, optional): Access action

        Returns:
            AceDetailsListResponse: Response from the API. List of access
                control entries for this user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}/aces')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('filter[record_type]')
                         .value(filter_record_type))
            .query_param(Parameter()
                         .key('filter[action]')
                         .value(filter_action))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AceDetailsListResponse.from_dictionary)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()

    def fetch_credentials_for_user(self,
                                   user_id):
        """Does a GET request to /security/users/{user_id}/credentials.

        Fetch credentials for user

        Args:
            user_id (uuid|str): User Id

        Returns:
            UserCredentialListResponse: Response from the API. List of
                credentials for user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}/credentials')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UserCredentialListResponse.from_dictionary)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()

    def create_new_credentials_for_user(self,
                                        user_id):
        """Does a POST request to /security/users/{user_id}/credentials.

        Create new credentials for user

        Args:
            user_id (uuid|str): User Id

        Returns:
            CredentialCreationResponse: Response from the API. Credential
                creation response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}/credentials')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CredentialCreationResponse.from_dictionary)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()

    def delete_credentials_for_user(self,
                                    user_id,
                                    client_id):
        """Does a DELETE request to /security/users/{user_id}/credentials/{client_id}.

        Delete credentials for user

        Args:
            user_id (uuid|str): User Id
            client_id (str): client id

        Returns:
            void: Response from the API. Credential deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}/credentials/{client_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('client_id')
                            .value(client_id)
                            .should_encode(True))
            .auth(Single('OAuth2'))
        ).execute()

    def fetch_all_roles_for_user(self,
                                 user_id):
        """Does a GET request to /security/users/{user_id}/roles.

        Fetch all roles for user

        Args:
            user_id (uuid|str): User Id

        Returns:
            UserRoleListResponse: Response from the API. List of roles for
                user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}/roles')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UserRoleListResponse.from_dictionary)
            .local_error('404', 'Not Found', ApiErrorException)
        ).execute()

    def remove_role_from_user(self,
                              user_id,
                              role_id):
        """Does a DELETE request to /security/users/{user_id}/roles/{role_id}.

        Remove role from user

        Args:
            user_id (uuid|str): User Id
            role_id (uuid|str): Role Id

        Returns:
            void: Response from the API. User role deleted OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}/roles/{role_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('role_id')
                            .value(role_id)
                            .should_encode(True))
            .auth(Single('OAuth2'))
        ).execute()

    def add_role_to_user(self,
                         user_id,
                         role_id):
        """Does a POST request to /security/users/{user_id}/roles/{role_id}.

        Add role to user

        Args:
            user_id (uuid|str): User Id
            role_id (uuid|str): Role Id

        Returns:
            void: Response from the API. Role set OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/security/users/{user_id}/roles/{role_id}')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('role_id')
                            .value(role_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .auth(Single('OAuth2'))
        ).execute()
