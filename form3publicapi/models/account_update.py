# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.account_relationships import AccountRelationships
from form3publicapi.models.attributes import Attributes


class AccountUpdate(object):

    """Implementation of the 'AccountUpdate' model.

    TODO: type model description here.

    Attributes:
        attributes (Attributes): TODO: type description here.
        id (uuid|str): Unique resource ID
        organisation_id (uuid|str): Unique ID of the organisation this
            resource is created by
        relationships (AccountRelationships): TODO: type description here.
        mtype (str): Name of the resource type
        version (int): Version number

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes": 'attributes',
        "id": 'id',
        "organisation_id": 'organisation_id',
        "version": 'version',
        "relationships": 'relationships',
        "mtype": 'type'
    }

    _optionals = [
        'relationships',
        'mtype',
    ]

    def __init__(self,
                 attributes=None,
                 id=None,
                 organisation_id=None,
                 version=None,
                 relationships=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the AccountUpdate class"""

        # Initialize members of the class
        self.attributes = attributes 
        self.id = id 
        self.organisation_id = organisation_id 
        if relationships is not APIHelper.SKIP:
            self.relationships = relationships 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        self.version = version 

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
        attributes = Attributes.from_dictionary(dictionary.get('attributes')) if dictionary.get('attributes') else None
        id = dictionary.get("id") if dictionary.get("id") else None
        organisation_id = dictionary.get("organisation_id") if dictionary.get("organisation_id") else None
        version = dictionary.get("version") if dictionary.get("version") else None
        relationships = AccountRelationships.from_dictionary(dictionary.get('relationships')) if 'relationships' in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(attributes,
                   id,
                   organisation_id,
                   version,
                   relationships,
                   mtype)
