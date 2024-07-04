# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationship_links import RelationshipLinks
from form3publicapi.models.relationship_payments import RelationshipPayments
from form3publicapi.models.relationship_reversals import RelationshipReversals


class ReversalSubmissionRelationships(object):

    """Implementation of the 'ReversalSubmissionRelationships' model.

    TODO: type model description here.

    Attributes:
        payment (RelationshipPayments): TODO: type description here.
        reversal (RelationshipReversals): TODO: type description here.
        validations (RelationshipLinks): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment',
        "reversal": 'reversal',
        "validations": 'validations'
    }

    _optionals = [
        'payment',
        'reversal',
        'validations',
    ]

    def __init__(self,
                 payment=APIHelper.SKIP,
                 reversal=APIHelper.SKIP,
                 validations=APIHelper.SKIP):
        """Constructor for the ReversalSubmissionRelationships class"""

        # Initialize members of the class
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if reversal is not APIHelper.SKIP:
            self.reversal = reversal 
        if validations is not APIHelper.SKIP:
            self.validations = validations 

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
        payment = RelationshipPayments.from_dictionary(dictionary.get('payment')) if 'payment' in dictionary.keys() else APIHelper.SKIP
        reversal = RelationshipReversals.from_dictionary(dictionary.get('reversal')) if 'reversal' in dictionary.keys() else APIHelper.SKIP
        validations = RelationshipLinks.from_dictionary(dictionary.get('validations')) if 'validations' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment,
                   reversal,
                   validations)
