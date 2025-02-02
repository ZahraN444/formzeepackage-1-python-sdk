# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationship_links import RelationshipLinks
from form3publicapi.models.relationship_payments import RelationshipPayments
from form3publicapi.models.relationship_return_admission_beneficiary_account import RelationshipReturnAdmissionBeneficiaryAccount
from form3publicapi.models.relationship_returns import RelationshipReturns


class ReturnAdmissionRelationships(object):

    """Implementation of the 'ReturnAdmissionRelationships' model.

    TODO: type model description here.

    Attributes:
        beneficiary_account (RelationshipReturnAdmissionBeneficiaryAccount):
            TODO: type description here.
        payment (RelationshipPayments): TODO: type description here.
        payment_return (RelationshipReturns): TODO: type description here.
        validations (RelationshipLinks): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "beneficiary_account": 'beneficiary_account',
        "payment": 'payment',
        "payment_return": 'payment_return',
        "validations": 'validations'
    }

    _optionals = [
        'beneficiary_account',
        'payment',
        'payment_return',
        'validations',
    ]

    def __init__(self,
                 beneficiary_account=APIHelper.SKIP,
                 payment=APIHelper.SKIP,
                 payment_return=APIHelper.SKIP,
                 validations=APIHelper.SKIP):
        """Constructor for the ReturnAdmissionRelationships class"""

        # Initialize members of the class
        if beneficiary_account is not APIHelper.SKIP:
            self.beneficiary_account = beneficiary_account 
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if payment_return is not APIHelper.SKIP:
            self.payment_return = payment_return 
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
        beneficiary_account = RelationshipReturnAdmissionBeneficiaryAccount.from_dictionary(dictionary.get('beneficiary_account')) if 'beneficiary_account' in dictionary.keys() else APIHelper.SKIP
        payment = RelationshipPayments.from_dictionary(dictionary.get('payment')) if 'payment' in dictionary.keys() else APIHelper.SKIP
        payment_return = RelationshipReturns.from_dictionary(dictionary.get('payment_return')) if 'payment_return' in dictionary.keys() else APIHelper.SKIP
        validations = RelationshipLinks.from_dictionary(dictionary.get('validations')) if 'validations' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(beneficiary_account,
                   payment,
                   payment_return,
                   validations)
