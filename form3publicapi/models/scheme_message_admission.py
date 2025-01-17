# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.scheme_message_admission_attributes import SchemeMessageAdmissionAttributes
from form3publicapi.models.scheme_message_admission_relationships import SchemeMessageAdmissionRelationships


class SchemeMessageAdmission(object):

    """Implementation of the 'SchemeMessageAdmission' model.

    TODO: type model description here.

    Attributes:
        attributes (SchemeMessageAdmissionAttributes): TODO: type description
            here.
        id (uuid|str): TODO: type description here.
        organisation_id (uuid|str): TODO: type description here.
        relationships (SchemeMessageAdmissionRelationships): TODO: type
            description here.
        mtype (Type15Enum): TODO: type description here.
        version (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "organisation_id": 'organisation_id',
        "attributes": 'attributes',
        "relationships": 'relationships',
        "mtype": 'type',
        "version": 'version'
    }

    _optionals = [
        'attributes',
        'relationships',
        'mtype',
        'version',
    ]

    def __init__(self,
                 id=None,
                 organisation_id=None,
                 attributes=APIHelper.SKIP,
                 relationships=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 version=APIHelper.SKIP):
        """Constructor for the SchemeMessageAdmission class"""

        # Initialize members of the class
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 
        self.id = id 
        self.organisation_id = organisation_id 
        if relationships is not APIHelper.SKIP:
            self.relationships = relationships 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if version is not APIHelper.SKIP:
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
        id = dictionary.get("id") if dictionary.get("id") else None
        organisation_id = dictionary.get("organisation_id") if dictionary.get("organisation_id") else None
        attributes = SchemeMessageAdmissionAttributes.from_dictionary(dictionary.get('attributes')) if 'attributes' in dictionary.keys() else APIHelper.SKIP
        relationships = SchemeMessageAdmissionRelationships.from_dictionary(dictionary.get('relationships')) if 'relationships' in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   organisation_id,
                   attributes,
                   relationships,
                   mtype,
                   version)
