# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes70(object):

    """Implementation of the 'Attributes70' model.

    TODO: type model description here.

    Attributes:
        client_credential_ids (List[str]): TODO: type description here.
        email (str): Email address
        public_key_ids (List[uuid|str]): TODO: type description here.
        role_ids (List[uuid|str]): List of roles that this user belongs to
        username (str): User name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_credential_ids": 'client_credential_ids',
        "email": 'email',
        "public_key_ids": 'public_key_ids',
        "role_ids": 'role_ids',
        "username": 'username'
    }

    _optionals = [
        'client_credential_ids',
        'email',
        'public_key_ids',
        'role_ids',
        'username',
    ]

    def __init__(self,
                 client_credential_ids=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 public_key_ids=APIHelper.SKIP,
                 role_ids=APIHelper.SKIP,
                 username=APIHelper.SKIP):
        """Constructor for the Attributes70 class"""

        # Initialize members of the class
        if client_credential_ids is not APIHelper.SKIP:
            self.client_credential_ids = client_credential_ids 
        if email is not APIHelper.SKIP:
            self.email = email 
        if public_key_ids is not APIHelper.SKIP:
            self.public_key_ids = public_key_ids 
        if role_ids is not APIHelper.SKIP:
            self.role_ids = role_ids 
        if username is not APIHelper.SKIP:
            self.username = username 

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
        client_credential_ids = dictionary.get("client_credential_ids") if dictionary.get("client_credential_ids") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        public_key_ids = dictionary.get("public_key_ids") if dictionary.get("public_key_ids") else APIHelper.SKIP
        role_ids = dictionary.get("role_ids") if dictionary.get("role_ids") else APIHelper.SKIP
        username = dictionary.get("username") if dictionary.get("username") else APIHelper.SKIP
        # Return an object of this model
        return cls(client_credential_ids,
                   email,
                   public_key_ids,
                   role_ids,
                   username)
