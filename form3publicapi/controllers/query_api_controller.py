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
from form3publicapi.models.query_list_response import QueryListResponse
from form3publicapi.models.query_fetch_response import QueryFetchResponse
from form3publicapi.models.query_admission_response import QueryAdmissionResponse
from form3publicapi.models.query_response_response import QueryResponseResponse
from form3publicapi.models.query_response_admission_response import QueryResponseAdmissionResponse
from form3publicapi.models.query_response_submission_response import QueryResponseSubmissionResponse
from form3publicapi.models.query_submission_response import QuerySubmissionResponse
from form3publicapi.exceptions.api_error_exception import ApiErrorException


class QueryApiController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(QueryApiController, self).__init__(config)

    def list_queries(self,
                     filter_organisation_id=None,
                     filter_status=None,
                     filter_query_type=None,
                     filter_auto_handled=None,
                     filter_processing_date_from=None,
                     filter_processing_date_to=None,
                     filter_created_on_from=None,
                     filter_created_on_to=None,
                     filter_payment_id=None,
                     filter_payment_admission_id=None,
                     filter_payment_submission_id=None,
                     filter_recall_id=None,
                     filter_recall_submission_id=None,
                     filter_query_id=None,
                     page_number=None,
                     page_size=None):
        """Does a GET request to /transaction/queries.

        Get Query

        Args:
            filter_organisation_id (List[uuid|str], optional): The
                organisations to filter on
            filter_status (ReportRequestStatusEnum, optional): Find all
                queries for a given status
            filter_query_type (str, optional): Find all queries for a given
                query type
            filter_auto_handled (bool, optional): Find all queries for given
                auto handled flag
            filter_processing_date_from (date, optional): Find all queries
                from a certain value date.
            filter_processing_date_to (date, optional): Find all queries up to
                a certain value date.
            filter_created_on_from (datetime, optional): Find all queries from
                a certain created date.
            filter_created_on_to (datetime, optional): Find all queries up to
                a certain created date.
            filter_payment_id (uuid|str, optional): Find all queries with a
                certain payment id.
            filter_payment_admission_id (uuid|str, optional): Find all queries
                with a certain payment admission id.
            filter_payment_submission_id (uuid|str, optional): Find all
                queries with a certain payment submission id.
            filter_recall_id (uuid|str, optional): Find all queries with a
                certain recall id.
            filter_recall_submission_id (uuid|str, optional): Find all queries
                with a certain recall submission id.
            filter_query_id (uuid|str, optional): Find all queries with a
                certain query id.
            page_number (str, optional): Which page to select
            page_size (int, optional): Number of items to select

        Returns:
            QueryListResponse: Response from the API. Query response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('filter[organisation_id]')
                         .value(filter_organisation_id))
            .query_param(Parameter()
                         .key('filter[status]')
                         .value(filter_status))
            .query_param(Parameter()
                         .key('filter[query_type]')
                         .value(filter_query_type))
            .query_param(Parameter()
                         .key('filter[auto_handled]')
                         .value(filter_auto_handled))
            .query_param(Parameter()
                         .key('filter[processing_date_from]')
                         .value(filter_processing_date_from))
            .query_param(Parameter()
                         .key('filter[processing_date_to]')
                         .value(filter_processing_date_to))
            .query_param(Parameter()
                         .key('filter[created_on_from]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, filter_created_on_from)))
            .query_param(Parameter()
                         .key('filter[created_on_to]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, filter_created_on_to)))
            .query_param(Parameter()
                         .key('filter[payment.id]')
                         .value(filter_payment_id))
            .query_param(Parameter()
                         .key('filter[payment_admission.id]')
                         .value(filter_payment_admission_id))
            .query_param(Parameter()
                         .key('filter[payment_submission.id]')
                         .value(filter_payment_submission_id))
            .query_param(Parameter()
                         .key('filter[recall.id]')
                         .value(filter_recall_id))
            .query_param(Parameter()
                         .key('filter[recall_submission.id]')
                         .value(filter_recall_submission_id))
            .query_param(Parameter()
                         .key('filter[query.id]')
                         .value(filter_query_id))
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
            .deserialize_into(QueryListResponse.from_dictionary)
            .local_error('400', 'Query bad request', ApiErrorException)
            .local_error('502', 'Query gateway issue', ApiErrorException)
        ).execute()

    def create_query(self,
                     creation_request=None):
        """Does a POST request to /transaction/queries.

        Create a Query

        Args:
            creation_request (QueryCreation, optional): TODO: type description
                here.

        Returns:
            QueryFetchResponse: Response from the API. creation response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryFetchResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
            .local_error('502', 'gateway issue', ApiErrorException)
        ).execute()

    def get_query(self,
                  query_id):
        """Does a GET request to /transaction/queries/{query_id}.

        Fetch a Query

        Args:
            query_id (uuid|str): Query ID

        Returns:
            QueryFetchResponse: Response from the API. query response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryFetchResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
        ).execute()

    def get_query_admission(self,
                            query_id,
                            query_admission_id):
        """Does a GET request to /transaction/queries/{query_id}/admissions/{query_admission_id}.

        Fetch a Query Admission

        Args:
            query_id (uuid|str): Query ID
            query_admission_id (uuid|str): Query Admission ID

        Returns:
            QueryAdmissionResponse: Response from the API. query admission
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/admissions/{query_admission_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_admission_id')
                            .value(query_admission_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryAdmissionResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
        ).execute()

    def create_query_response(self,
                              query_id,
                              creation_request=None):
        """Does a POST request to /transaction/queries/{query_id}/responses.

        Create a Query Response

        Args:
            query_id (uuid|str): Query ID
            creation_request (QueryResponseCreation, optional): TODO: type
                description here.

        Returns:
            QueryResponseResponse: Response from the API. creation response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/responses')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryResponseResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
            .local_error('502', 'gateway issue', ApiErrorException)
        ).execute()

    def get_query_response(self,
                           query_id,
                           query_response_id):
        """Does a GET request to /transaction/queries/{query_id}/responses/{query_response_id}.

        Fetch a Query Response

        Args:
            query_id (uuid|str): Query ID
            query_response_id (uuid|str): Query Response ID

        Returns:
            QueryResponseResponse: Response from the API. Query Response
                Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/responses/{query_response_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_response_id')
                            .value(query_response_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryResponseResponse.from_dictionary)
            .local_error('400', 'Bad Request', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
        ).execute()

    def get_query_response_admission(self,
                                     query_id,
                                     query_response_id,
                                     query_response_admission_id):
        """Does a GET request to /transaction/queries/{query_id}/responses/{query_response_id}/admissions/{query_response_admission_id}.

        Fetch a Query Response Admission

        Args:
            query_id (uuid|str): Query ID
            query_response_id (uuid|str): Query Response ID
            query_response_admission_id (uuid|str): Query Response Admission
                ID

        Returns:
            QueryResponseAdmissionResponse: Response from the API. query
                response admission response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/responses/{query_response_id}/admissions/{query_response_admission_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_response_id')
                            .value(query_response_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_response_admission_id')
                            .value(query_response_admission_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryResponseAdmissionResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
        ).execute()

    def create_query_response_submission(self,
                                         query_id,
                                         query_response_id,
                                         creation_request=None):
        """Does a POST request to /transaction/queries/{query_id}/responses/{query_response_id}/submissions.

        Create a Query Response Submission

        Args:
            query_id (uuid|str): Query ID
            query_response_id (uuid|str): Query Response ID
            creation_request (QueryResponseSubmissionCreation, optional):
                TODO: type description here.

        Returns:
            QueryResponseSubmissionResponse: Response from the API. creation
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/responses/{query_response_id}/submissions')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_response_id')
                            .value(query_response_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryResponseSubmissionResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
            .local_error('502', 'gateway issue', ApiErrorException)
        ).execute()

    def get_query_response_submission(self,
                                      query_id,
                                      query_response_id,
                                      query_response_submission_id):
        """Does a GET request to /transaction/queries/{query_id}/responses/{query_response_id}/submissions/{query_response_submission_id}.

        Fetch a Query Response Submission

        Args:
            query_id (uuid|str): Query ID
            query_response_id (uuid|str): Query Response ID
            query_response_submission_id (uuid|str): Query Response Submission
                ID

        Returns:
            QueryResponseSubmissionResponse: Response from the API. query
                response submission response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/responses/{query_response_id}/submissions/{query_response_submission_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_response_id')
                            .value(query_response_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_response_submission_id')
                            .value(query_response_submission_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QueryResponseSubmissionResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
        ).execute()

    def create_query_submission(self,
                                query_id,
                                creation_request=None):
        """Does a POST request to /transaction/queries/{query_id}/submissions.

        Create a Query submission

        Args:
            query_id (uuid|str): Query ID
            creation_request (QuerySubmissionCreation, optional): TODO: type
                description here.

        Returns:
            QuerySubmissionResponse: Response from the API. creation response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/submissions')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/vnd.api+json'))
            .body_param(Parameter()
                        .value(creation_request))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QuerySubmissionResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
            .local_error('502', 'gateway issue', ApiErrorException)
        ).execute()

    def get_query_submission(self,
                             query_id,
                             query_submission_id):
        """Does a GET request to /transaction/queries/{query_id}/submissions/{query_submission_id}.

        Fetch a Query submission

        Args:
            query_id (uuid|str): Query ID
            query_submission_id (uuid|str): Query Submission ID

        Returns:
            QuerySubmissionResponse: Response from the API. query submission
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transaction/queries/{query_id}/submissions/{query_submission_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('query_id')
                            .value(query_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('query_submission_id')
                            .value(query_submission_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(QuerySubmissionResponse.from_dictionary)
            .local_error('400', 'bad request', ApiErrorException)
            .local_error('403', 'forbidden', ApiErrorException)
        ).execute()
