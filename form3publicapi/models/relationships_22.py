# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationship_payments import RelationshipPayments
from form3publicapi.models.relationship_recall_reversals import RelationshipRecallReversals
from form3publicapi.models.relationship_recalls import RelationshipRecalls


class Relationships22(object):

    """Implementation of the 'Relationships22' model.

    TODO: type model description here.

    Attributes:
        payment (RelationshipPayments): TODO: type description here.
        recall (RelationshipRecalls): TODO: type description here.
        recall_reversal (RelationshipRecallReversals): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment',
        "recall": 'recall',
        "recall_reversal": 'recall_reversal'
    }

    _optionals = [
        'payment',
        'recall',
        'recall_reversal',
    ]

    def __init__(self,
                 payment=APIHelper.SKIP,
                 recall=APIHelper.SKIP,
                 recall_reversal=APIHelper.SKIP):
        """Constructor for the Relationships22 class"""

        # Initialize members of the class
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if recall is not APIHelper.SKIP:
            self.recall = recall 
        if recall_reversal is not APIHelper.SKIP:
            self.recall_reversal = recall_reversal 

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
        recall = RelationshipRecalls.from_dictionary(dictionary.get('recall')) if 'recall' in dictionary.keys() else APIHelper.SKIP
        recall_reversal = RelationshipRecallReversals.from_dictionary(dictionary.get('recall_reversal')) if 'recall_reversal' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment,
                   recall,
                   recall_reversal)
