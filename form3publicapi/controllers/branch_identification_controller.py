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
from form3publicapi.models.branch_identification_list_response import BranchIdentificationListResponse
from form3publicapi.models.branch_identification_response import BranchIdentificationResponse
from form3publicapi.exceptions.api_error_exception import ApiErrorException
from form3publicapi.exceptions.api_exception import APIException


class BranchIdentificationController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(BranchIdentificationController, self).__init__(config)

    def list_branch_identifications_by_branch(self,
                                              branch_id,
                                              page_number=None,
                                              page_size=None,
                                              filter_organisation_id=None,
                                              filter_secondary_identification=None):
        """Does a GET request to /organisation/branches/{branch_id}/identifications.

        List Branch Identifications by Branch

        Args:
            branch_id (uuid|str): Branch Id to which this identification
                relates to
            page_number (str, optional): Which page to select
            page_size (int, optional): Number of items to select
            filter_organisation_id (List[uuid|str], optional): Filter by
                organisation id
            filter_secondary_identification (List[str], optional): Filter to
                only include branch identifications with specified
                secondary_identification

        Returns:
            BranchIdentificationListResponse: Response from the API. List of
                branch identification

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/branches/{branch_id}/identifications')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('branch_id')
                            .value(branch_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page[number]')
                         .value(page_number))
            .query_param(Parameter()
                         .key('page[size]')
                         .value(page_size))
            .query_param(Parameter()
                         .key('filter[organisation_id]')
                         .value(filter_organisation_id))
            .query_param(Parameter()
                         .key('filter[secondary_identification]')
                         .value(filter_secondary_identification))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BranchIdentificationListResponse.from_dictionary)
        ).execute()

    def create_an_identification_for_an_existing_branch(self,
                                                        branch_id,
                                                        branch_identification_creation_request=None):
        """Does a POST request to /organisation/branches/{branch_id}/identifications.

        Create an identification for an existing Branch

        Args:
            branch_id (uuid|str): Branch Id to which this identification
                relates to
            branch_identification_creation_request
                (BranchIdentificationRequest, optional): TODO: type
                description here.

        Returns:
            BranchIdentificationResponse: Response from the API. Branch
                Identification creation response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/branches/{branch_id}/identifications')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('branch_id')
                            .value(branch_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(branch_identification_creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BranchIdentificationResponse.from_dictionary)
            .local_error('409', 'Branch Identification creation error, constraint violation of secondary identification', ApiErrorException)
        ).execute()

    def delete_branch_identification(self,
                                     branch_id,
                                     identification_id,
                                     version):
        """Does a DELETE request to /organisation/branches/{branch_id}/identifications/{identification_id}.

        Delete branch identification

        Args:
            branch_id (uuid|str): Branch Id
            identification_id (uuid|str): Branch Identification Id
            version (int): Version

        Returns:
            void: Response from the API. Branch Identification deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/branches/{branch_id}/identifications/{identification_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('branch_id')
                            .value(branch_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('identification_id')
                            .value(identification_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('version')
                         .value(version))
            .auth(Single('OAuth2'))
        ).execute()

    def get_a_branch_identification_by_id(self,
                                          branch_id,
                                          identification_id):
        """Does a GET request to /organisation/branches/{branch_id}/identifications/{identification_id}.

        Get a branch identification by id

        Args:
            branch_id (uuid|str): Branch Id
            identification_id (uuid|str): Branch Identification Id

        Returns:
            BranchIdentificationResponse: Response from the API. Branch
                Identification response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/branches/{branch_id}/identifications/{identification_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('branch_id')
                            .value(branch_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('identification_id')
                            .value(identification_id)
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
            .deserialize_into(BranchIdentificationResponse.from_dictionary)
        ).execute()

    def amend_branch_identification(self,
                                    branch_id,
                                    identification_id,
                                    branch_identification_amend_request=None):
        """Does a PATCH request to /organisation/branches/{branch_id}/identifications/{identification_id}.

        Amend Branch Identification

        Args:
            branch_id (uuid|str): Branch Id
            identification_id (uuid|str): Branch Identification Id; Must match
                id in the payload
            branch_identification_amend_request (BranchIdentificationRequest,
                optional): TODO: type description here.

        Returns:
            BranchIdentificationResponse: Response from the API. Branch
                Identification updated

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/organisation/branches/{branch_id}/identifications/{identification_id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('branch_id')
                            .value(branch_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('identification_id')
                            .value(identification_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(branch_identification_amend_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BranchIdentificationResponse.from_dictionary)
            .local_error('409', 'Branch Identification update error, constraint violation of secondary identification', ApiErrorException)
        ).execute()
