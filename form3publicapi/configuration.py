# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from enum import Enum
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    PRODUCTION = 0


class Server(Enum):
    """An enum for API servers"""
    DEFAULT = 0


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def basic_credentials(self):
        return self._basic_credentials

    @property
    def o_auth_2_credentials(self):
        return self._o_auth_2_credentials

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION, basic_credentials=None,
                 o_auth_2_credentials=None):
        if retry_methods is None:
            retry_methods = ['GET', 'PUT']

        if retry_statuses is None:
            retry_statuses = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]

        super().__init__(http_client_instance,
                         override_http_client_configuration, http_call_back,
                         timeout, max_retries, backoff_factor, retry_statuses,
                         retry_methods)

        # Current API environment
        self._environment = environment

        # The object holding Basic Authentication credentials
        self._basic_credentials = basic_credentials

        # The object holding OAuth 2 Client Credentials Grant credentials
        self._o_auth_2_credentials = o_auth_2_credentials

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   basic_credentials=None, o_auth_2_credentials=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        basic_credentials = basic_credentials or self.basic_credentials
        o_auth_2_credentials = o_auth_2_credentials or self.o_auth_2_credentials
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, basic_credentials=basic_credentials,
            o_auth_2_credentials=o_auth_2_credentials
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout, max_retries=self.max_retries,
            backoff_factor=self.backoff_factor, retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
            response_factory=self.http_response_factory
        )

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'https://api.form3.tech/v1'
        }
    }

    def get_base_uri(self, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        return self.environments[self.environment][server]
