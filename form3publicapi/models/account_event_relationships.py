# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationship_account import RelationshipAccount


class AccountEventRelationships(object):

    """Implementation of the 'AccountEventRelationships' model.

    TODO: type model description here.

    Attributes:
        account (RelationshipAccount): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account": 'account'
    }

    _optionals = [
        'account',
    ]

    def __init__(self,
                 account=APIHelper.SKIP):
        """Constructor for the AccountEventRelationships class"""

        # Initialize members of the class
        if account is not APIHelper.SKIP:
            self.account = account 

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
        account = RelationshipAccount.from_dictionary(dictionary.get('account')) if 'account' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account)
