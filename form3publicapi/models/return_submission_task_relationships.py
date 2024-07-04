# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationship_payments import RelationshipPayments
from form3publicapi.models.relationship_return_submissions import RelationshipReturnSubmissions
from form3publicapi.models.relationship_returns import RelationshipReturns


class ReturnSubmissionTaskRelationships(object):

    """Implementation of the 'ReturnSubmissionTaskRelationships' model.

    TODO: type model description here.

    Attributes:
        payment (RelationshipPayments): TODO: type description here.
        payment_return (RelationshipReturns): TODO: type description here.
        return_submission (RelationshipReturnSubmissions): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment',
        "payment_return": 'payment_return',
        "return_submission": 'return_submission'
    }

    _optionals = [
        'payment',
        'payment_return',
        'return_submission',
    ]

    def __init__(self,
                 payment=APIHelper.SKIP,
                 payment_return=APIHelper.SKIP,
                 return_submission=APIHelper.SKIP):
        """Constructor for the ReturnSubmissionTaskRelationships class"""

        # Initialize members of the class
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if payment_return is not APIHelper.SKIP:
            self.payment_return = payment_return 
        if return_submission is not APIHelper.SKIP:
            self.return_submission = return_submission 

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
        payment_return = RelationshipReturns.from_dictionary(dictionary.get('payment_return')) if 'payment_return' in dictionary.keys() else APIHelper.SKIP
        return_submission = RelationshipReturnSubmissions.from_dictionary(dictionary.get('return_submission')) if 'return_submission' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment,
                   payment_return,
                   return_submission)
