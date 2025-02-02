# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.callback_uri import CallbackURI
from form3publicapi.models.subscription_user_defined_data import SubscriptionUserDefinedData


class SubscriptionUpdateAttributes(object):

    """Implementation of the 'SubscriptionUpdateAttributes' model.

    TODO: type model description here.

    Attributes:
        callback_transport (CallbackTransportEnum): TODO: type description
            here.
        callback_uri (str): Deprecated. Please use callback_uris instead
        callback_uris (List[CallbackURI]): TODO: type description here.
        deactivated (bool): TODO: type description here.
        event_type (str): TODO: type description here.
        filter (str): TODO: type description here.
        record_type (str): TODO: type description here.
        user_defined_data (List[SubscriptionUserDefinedData]): All purpose
            list of key-value pairs to store specific data for the associated
            subscription.
        user_id (uuid|str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "callback_transport": 'callback_transport',
        "callback_uri": 'callback_uri',
        "callback_uris": 'callback_uris',
        "deactivated": 'deactivated',
        "event_type": 'event_type',
        "filter": 'filter',
        "record_type": 'record_type',
        "user_defined_data": 'user_defined_data',
        "user_id": 'user_id'
    }

    _optionals = [
        'callback_transport',
        'callback_uri',
        'callback_uris',
        'deactivated',
        'event_type',
        'filter',
        'record_type',
        'user_defined_data',
        'user_id',
    ]

    def __init__(self,
                 callback_transport=APIHelper.SKIP,
                 callback_uri=APIHelper.SKIP,
                 callback_uris=APIHelper.SKIP,
                 deactivated=APIHelper.SKIP,
                 event_type=APIHelper.SKIP,
                 filter=APIHelper.SKIP,
                 record_type=APIHelper.SKIP,
                 user_defined_data=APIHelper.SKIP,
                 user_id=APIHelper.SKIP):
        """Constructor for the SubscriptionUpdateAttributes class"""

        # Initialize members of the class
        if callback_transport is not APIHelper.SKIP:
            self.callback_transport = callback_transport 
        if callback_uri is not APIHelper.SKIP:
            self.callback_uri = callback_uri 
        if callback_uris is not APIHelper.SKIP:
            self.callback_uris = callback_uris 
        if deactivated is not APIHelper.SKIP:
            self.deactivated = deactivated 
        if event_type is not APIHelper.SKIP:
            self.event_type = event_type 
        if filter is not APIHelper.SKIP:
            self.filter = filter 
        if record_type is not APIHelper.SKIP:
            self.record_type = record_type 
        if user_defined_data is not APIHelper.SKIP:
            self.user_defined_data = user_defined_data 
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        callback_transport = dictionary.get("callback_transport") if dictionary.get("callback_transport") else APIHelper.SKIP
        callback_uri = dictionary.get("callback_uri") if dictionary.get("callback_uri") else APIHelper.SKIP
        callback_uris = None
        if dictionary.get('callback_uris') is not None:
            callback_uris = [CallbackURI.from_dictionary(x) for x in dictionary.get('callback_uris')]
        else:
            callback_uris = APIHelper.SKIP
        deactivated = dictionary.get("deactivated") if "deactivated" in dictionary.keys() else APIHelper.SKIP
        event_type = dictionary.get("event_type") if dictionary.get("event_type") else APIHelper.SKIP
        filter = dictionary.get("filter") if dictionary.get("filter") else APIHelper.SKIP
        record_type = dictionary.get("record_type") if dictionary.get("record_type") else APIHelper.SKIP
        user_defined_data = None
        if dictionary.get('user_defined_data') is not None:
            user_defined_data = [SubscriptionUserDefinedData.from_dictionary(x) for x in dictionary.get('user_defined_data')]
        else:
            user_defined_data = APIHelper.SKIP
        user_id = dictionary.get("user_id") if dictionary.get("user_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(callback_transport,
                   callback_uri,
                   callback_uris,
                   deactivated,
                   event_type,
                   filter,
                   record_type,
                   user_defined_data,
                   user_id)
