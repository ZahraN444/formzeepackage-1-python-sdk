# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationship_branch import RelationshipBranch


class BranchIdentificationEventRelationships(object):

    """Implementation of the 'BranchIdentificationEventRelationships' model.

    TODO: type model description here.

    Attributes:
        branch (RelationshipBranch): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "branch": 'branch'
    }

    _optionals = [
        'branch',
    ]

    def __init__(self,
                 branch=APIHelper.SKIP):
        """Constructor for the BranchIdentificationEventRelationships class"""

        # Initialize members of the class
        if branch is not APIHelper.SKIP:
            self.branch = branch 

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
        branch = RelationshipBranch.from_dictionary(dictionary.get('branch')) if 'branch' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(branch)
