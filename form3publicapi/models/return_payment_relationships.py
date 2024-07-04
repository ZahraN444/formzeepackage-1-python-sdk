# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationship_links import RelationshipLinks
from form3publicapi.models.relationship_payments import RelationshipPayments
from form3publicapi.models.return_admission_2 import ReturnAdmission2
from form3publicapi.models.return_submission_2 import ReturnSubmission2


class ReturnPaymentRelationships(object):

    """Implementation of the 'ReturnPaymentRelationships' model.

    TODO: type model description here.

    Attributes:
        payment (RelationshipPayments): TODO: type description here.
        return_admission (ReturnAdmission2): TODO: type description here.
        return_reversal (RelationshipLinks): TODO: type description here.
        return_submission (ReturnSubmission2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment',
        "return_admission": 'return_admission',
        "return_reversal": 'return_reversal',
        "return_submission": 'return_submission'
    }

    _optionals = [
        'payment',
        'return_admission',
        'return_reversal',
        'return_submission',
    ]

    def __init__(self,
                 payment=APIHelper.SKIP,
                 return_admission=APIHelper.SKIP,
                 return_reversal=APIHelper.SKIP,
                 return_submission=APIHelper.SKIP):
        """Constructor for the ReturnPaymentRelationships class"""

        # Initialize members of the class
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if return_admission is not APIHelper.SKIP:
            self.return_admission = return_admission 
        if return_reversal is not APIHelper.SKIP:
            self.return_reversal = return_reversal 
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
        return_admission = ReturnAdmission2.from_dictionary(dictionary.get('return_admission')) if 'return_admission' in dictionary.keys() else APIHelper.SKIP
        return_reversal = RelationshipLinks.from_dictionary(dictionary.get('return_reversal')) if 'return_reversal' in dictionary.keys() else APIHelper.SKIP
        return_submission = ReturnSubmission2.from_dictionary(dictionary.get('return_submission')) if 'return_submission' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment,
                   return_admission,
                   return_reversal,
                   return_submission)
