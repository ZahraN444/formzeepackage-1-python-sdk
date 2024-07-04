# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.name_verification_admission_attributes import NameVerificationAdmissionAttributes
from form3publicapi.models.name_verification_admission_relationships import NameVerificationAdmissionRelationships


class NameVerificationAdmission(object):

    """Implementation of the 'NameVerificationAdmission' model.

    TODO: type model description here.

    Attributes:
        attributes (NameVerificationAdmissionAttributes): TODO: type
            description here.
        created_on (datetime): TODO: type description here.
        id (uuid|str): TODO: type description here.
        modified_on (datetime): TODO: type description here.
        organisation_id (uuid|str): TODO: type description here.
        relationships (NameVerificationAdmissionRelationships): TODO: type
            description here.
        mtype (str): TODO: type description here.
        version (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes": 'attributes',
        "id": 'id',
        "organisation_id": 'organisation_id',
        "created_on": 'created_on',
        "modified_on": 'modified_on',
        "relationships": 'relationships',
        "mtype": 'type',
        "version": 'version'
    }

    _optionals = [
        'created_on',
        'modified_on',
        'relationships',
        'mtype',
        'version',
    ]

    def __init__(self,
                 attributes=None,
                 id=None,
                 organisation_id=None,
                 created_on=APIHelper.SKIP,
                 modified_on=APIHelper.SKIP,
                 relationships=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 version=APIHelper.SKIP):
        """Constructor for the NameVerificationAdmission class"""

        # Initialize members of the class
        self.attributes = attributes 
        if created_on is not APIHelper.SKIP:
            self.created_on = APIHelper.apply_datetime_converter(created_on, APIHelper.RFC3339DateTime) if created_on else None 
        self.id = id 
        if modified_on is not APIHelper.SKIP:
            self.modified_on = APIHelper.apply_datetime_converter(modified_on, APIHelper.RFC3339DateTime) if modified_on else None 
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
        attributes = NameVerificationAdmissionAttributes.from_dictionary(dictionary.get('attributes')) if dictionary.get('attributes') else None
        id = dictionary.get("id") if dictionary.get("id") else None
        organisation_id = dictionary.get("organisation_id") if dictionary.get("organisation_id") else None
        created_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_on")).datetime if dictionary.get("created_on") else APIHelper.SKIP
        modified_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("modified_on")).datetime if dictionary.get("modified_on") else APIHelper.SKIP
        relationships = NameVerificationAdmissionRelationships.from_dictionary(dictionary.get('relationships')) if 'relationships' in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        # Return an object of this model
        return cls(attributes,
                   id,
                   organisation_id,
                   created_on,
                   modified_on,
                   relationships,
                   mtype,
                   version)
