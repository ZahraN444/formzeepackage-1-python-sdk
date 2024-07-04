# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from form3publicapi.api_helper import APIHelper
from form3publicapi.configuration import Server
from form3publicapi.utilities.file_wrapper import FileWrapper
from form3publicapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from form3publicapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from form3publicapi.models.list_transaction_files_response import ListTransactionFilesResponse
from form3publicapi.models.transaction_file_response import TransactionFileResponse
from form3publicapi.models.transaction_file_admission_response import TransactionFileAdmissionResponse
from form3publicapi.models.transaction_file_submission_response import TransactionFileSubmissionResponse
from form3publicapi.exceptions.api_error_exception import ApiErrorException


class TransactionFileAPIController(BaseController):

    """A Controller to access Endpoints in the form3publicapi API."""
    def __init__(self, config):
        super(TransactionFileAPIController, self).__init__(config)

    def list_transaction_files(self,
                               page_number=None,
                               page_size=100,
                               filter_organisation_id=None,
                               filter_payment_scheme=None,
                               filter_file_format=None,
                               filter_created_on_from=None,
                               filter_created_on_to=None,
                               filter_submission_status=None,
                               filter_submission_submission_date_from=None,
                               filter_submission_submission_date_to=None,
                               filter_submission_scheme_references_file_identifier=None,
                               filter_submission_scheme_references_file_number=None,
                               filter_submission_scheme_references_clearing_id=None,
                               filter_admission_status=None,
                               filter_admission_admission_date_from=None,
                               filter_admission_admission_date_to=None):
        """Does a GET request to /files/transactions.

        List transaction files

        Args:
            page_number (str, optional): Which page to select
            page_size (int, optional): Number of items to select
            filter_organisation_id (List[uuid|str], optional): Find all File
                resources with a given organisation ID
            filter_payment_scheme (str, optional): Find File resources by a
                certain scheme
            filter_file_format (str, optional): Find File resources by the
                format of the file
            filter_created_on_from (date, optional): Find all File resources
                created from this date, in format YYYY-MM-DD
            filter_created_on_to (date, optional): Find all File resources
                created up to this date, in format YYYY-MM-DD
            filter_submission_status (str, optional): Find all File resources
                with a certain submission status
            filter_submission_submission_date_from (datetime, optional): Find
                all File resources submitted from and including this
                date/time
            filter_submission_submission_date_to (datetime, optional): Find
                all File resources submitted up to and included this
                date/time
            filter_submission_scheme_references_file_identifier (str,
                optional): Find File resources the id of the submission to to
                the scheme
            filter_submission_scheme_references_file_number (str, optional):
                Find File resources by the id of the file sent to the scheme
            filter_submission_scheme_references_clearing_id (str, optional):
                Find File resources by the Service User Number (SUN) of the
                payment originator
            filter_admission_status (str, optional): Find all File resources
                with a certain admission status
            filter_admission_admission_date_from (datetime, optional): Find
                all File resources admitted from and including this date/time
            filter_admission_admission_date_to (datetime, optional): Find all
                File resources admitted up to and included this date/time

        Returns:
            ListTransactionFilesResponse: Response from the API. List of
                transaction files

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions')
            .http_method(HttpMethodEnum.GET)
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
                         .key('filter[payment_scheme]')
                         .value(filter_payment_scheme))
            .query_param(Parameter()
                         .key('filter[file_format]')
                         .value(filter_file_format))
            .query_param(Parameter()
                         .key('filter[created_on_from]')
                         .value(filter_created_on_from))
            .query_param(Parameter()
                         .key('filter[created_on_to]')
                         .value(filter_created_on_to))
            .query_param(Parameter()
                         .key('filter[submission.status]')
                         .value(filter_submission_status))
            .query_param(Parameter()
                         .key('filter[submission.submission_date_from]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, filter_submission_submission_date_from)))
            .query_param(Parameter()
                         .key('filter[submission.submission_date_to]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, filter_submission_submission_date_to)))
            .query_param(Parameter()
                         .key('filter[submission.scheme_references.file_identifier]')
                         .value(filter_submission_scheme_references_file_identifier))
            .query_param(Parameter()
                         .key('filter[submission.scheme_references.file_number]')
                         .value(filter_submission_scheme_references_file_number))
            .query_param(Parameter()
                         .key('filter[submission.scheme_references.clearing_id]')
                         .value(filter_submission_scheme_references_clearing_id))
            .query_param(Parameter()
                         .key('filter[admission.status]')
                         .value(filter_admission_status))
            .query_param(Parameter()
                         .key('filter[admission.admission_date_from]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, filter_admission_admission_date_from)))
            .query_param(Parameter()
                         .key('filter[admission.admission_date_to]')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, filter_admission_admission_date_to)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListTransactionFilesResponse.from_dictionary)
            .local_error('400', 'Reports bad request', ApiErrorException)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()

    def create_transaction_file(self,
                                transaction_file_creation_request=None):
        """Does a POST request to /files/transactions.

        Creates a Transaction File

        Args:
            transaction_file_creation_request (TransactionFileCreation,
                optional): TODO: type description here.

        Returns:
            TransactionFileResponse: Response from the API. Transaction File
                Creation Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(transaction_file_creation_request))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionFileResponse.from_dictionary)
            .local_error('400', 'Bad Request', ApiErrorException)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('409', 'Conflict', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()

    def get_transaction_file(self,
                             transaction_file_id,
                             accept=None):
        """Does a GET request to /files/transactions/{transaction_file_id}.

        Fetch transaction file

        Args:
            transaction_file_id (uuid|str): Transaction File Id
            accept (str, optional): Acceptable Formats, possible values are
                "application/vnd.api+json", "application/x-ndjson" and
                "application/x.form3.standard18"

        Returns:
            TransactionFileResponse: Response from the API. Transaction File
                Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions/{transaction_file_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('transaction_file_id')
                            .value(transaction_file_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Accept')
                          .value(accept))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionFileResponse.from_dictionary)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('404', 'Not Found', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()

    def upload_transaction_file(self,
                                transaction_file_id,
                                x_form_3_upload_part,
                                payload):
        """Does a PUT request to /files/transactions/{transaction_file_id}.

        Put Transaction file chunk

        Args:
            transaction_file_id (uuid|str): Transaction File Id
            x_form_3_upload_part (str): Which part of the file we are
                uploading
            payload (typing.BinaryIO): TODO: type description here.

        Returns:
            TransactionFileResponse: Response from the API. Transaction File
                Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions/{transaction_file_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('transaction_file_id')
                            .value(transaction_file_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('X-Form3-Upload-Part')
                          .value(x_form_3_upload_part))
            .multipart_param(Parameter()
                             .key('payload')
                             .value(payload)
                             .default_content_type('application/octet-stream'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionFileResponse.from_dictionary)
            .local_error('400', 'Bad Request', ApiErrorException)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('404', 'Transaction File Not Found', ApiErrorException)
            .local_error('409', 'Transaction File Conflict', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()

    def create_transaction_file_admission(self,
                                          transaction_file_id,
                                          transaction_file_admission_creation_request=None):
        """Does a POST request to /files/transactions/{transaction_file_id}/admissions.

        Creates a Transaction File Admission

        Args:
            transaction_file_id (uuid|str): Transaction File Id
            transaction_file_admission_creation_request
                (TransactionFileAdmissionCreation, optional): TODO: type
                description here.

        Returns:
            TransactionFileAdmissionResponse: Response from the API.
                Transaction File Admission Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions/{transaction_file_id}/admissions')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('transaction_file_id')
                            .value(transaction_file_id)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(transaction_file_admission_creation_request))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionFileAdmissionResponse.from_dictionary)
            .local_error('400', 'Bad Request', ApiErrorException)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('404', 'Not Found', ApiErrorException)
            .local_error('409', 'Transaction File Admission Conflict', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()

    def get_transaction_file_admission(self,
                                       transaction_file_id,
                                       transaction_file_admission_id):
        """Does a GET request to /files/transactions/{transaction_file_id}/admissions/{transaction_file_admission_id}.

        Fetch transaction file admission

        Args:
            transaction_file_id (uuid|str): Transaction File Id
            transaction_file_admission_id (uuid|str): Transaction File
                Admission Id

        Returns:
            TransactionFileAdmissionResponse: Response from the API.
                Transaction File Admission Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions/{transaction_file_id}/admissions/{transaction_file_admission_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('transaction_file_id')
                            .value(transaction_file_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('transaction_file_admission_id')
                            .value(transaction_file_admission_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionFileAdmissionResponse.from_dictionary)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('404', 'Not Found', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()

    def create_transaction_file_submission(self,
                                           transaction_file_id,
                                           transaction_file_submission_creation_request=None):
        """Does a POST request to /files/transactions/{transaction_file_id}/submissions.

        Creates a Transaction File Submission

        Args:
            transaction_file_id (uuid|str): Transaction File Id
            transaction_file_submission_creation_request
                (TransactionFileSubmissionCreation, optional): TODO: type
                description here.

        Returns:
            TransactionFileSubmissionResponse: Response from the API.
                Transaction File Submission Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions/{transaction_file_id}/submissions')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('transaction_file_id')
                            .value(transaction_file_id)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(transaction_file_submission_creation_request))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionFileSubmissionResponse.from_dictionary)
            .local_error('400', 'Bad Request', ApiErrorException)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('404', 'Not Found', ApiErrorException)
            .local_error('409', 'Transaction File Submission Conflict', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()

    def get_transaction_file_submission(self,
                                        transaction_file_id,
                                        transaction_file_submission_id):
        """Does a GET request to /files/transactions/{transaction_file_id}/submissions/{transaction_file_submission_id}.

        Fetch transaction file submission

        Args:
            transaction_file_id (uuid|str): Transaction File Id
            transaction_file_submission_id (uuid|str): Transaction File
                Submission Id

        Returns:
            TransactionFileSubmissionResponse: Response from the API.
                Transaction File Submission Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/files/transactions/{transaction_file_id}/submissions/{transaction_file_submission_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('transaction_file_id')
                            .value(transaction_file_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('transaction_file_submission_id')
                            .value(transaction_file_submission_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('OAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionFileSubmissionResponse.from_dictionary)
            .local_error('401', 'Unauthorized', ApiErrorException)
            .local_error('403', 'Forbidden', ApiErrorException)
            .local_error('404', 'Not Found', ApiErrorException)
            .local_error('500', 'Internal Server Error', ApiErrorException)
        ).execute()
