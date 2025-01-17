# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.relationships_payment import RelationshipsPayment
from form3publicapi.models.relationships_payment_admission import RelationshipsPaymentAdmission
from form3publicapi.models.relationships_payment_recall import RelationshipsPaymentRecall
from form3publicapi.models.relationships_payment_recall_submission import RelationshipsPaymentRecallSubmission
from form3publicapi.models.relationships_payment_submission import RelationshipsPaymentSubmission
from form3publicapi.models.relationships_query import RelationshipsQuery


class NewQueryRelationships(object):

    """Implementation of the 'NewQueryRelationships' model.

    TODO: type model description here.

    Attributes:
        payment (RelationshipsPayment): TODO: type description here.
        payment_admission (RelationshipsPaymentAdmission): TODO: type
            description here.
        payment_submission (RelationshipsPaymentSubmission): TODO: type
            description here.
        query (RelationshipsQuery): TODO: type description here.
        recall (RelationshipsPaymentRecall): TODO: type description here.
        recall_submission (RelationshipsPaymentRecallSubmission): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment": 'payment',
        "payment_admission": 'payment_admission',
        "payment_submission": 'payment_submission',
        "query": 'query',
        "recall": 'recall',
        "recall_submission": 'recall_submission'
    }

    _optionals = [
        'payment',
        'payment_admission',
        'payment_submission',
        'query',
        'recall',
        'recall_submission',
    ]

    def __init__(self,
                 payment=APIHelper.SKIP,
                 payment_admission=APIHelper.SKIP,
                 payment_submission=APIHelper.SKIP,
                 query=APIHelper.SKIP,
                 recall=APIHelper.SKIP,
                 recall_submission=APIHelper.SKIP):
        """Constructor for the NewQueryRelationships class"""

        # Initialize members of the class
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if payment_admission is not APIHelper.SKIP:
            self.payment_admission = payment_admission 
        if payment_submission is not APIHelper.SKIP:
            self.payment_submission = payment_submission 
        if query is not APIHelper.SKIP:
            self.query = query 
        if recall is not APIHelper.SKIP:
            self.recall = recall 
        if recall_submission is not APIHelper.SKIP:
            self.recall_submission = recall_submission 

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
        payment = RelationshipsPayment.from_dictionary(dictionary.get('payment')) if 'payment' in dictionary.keys() else APIHelper.SKIP
        payment_admission = RelationshipsPaymentAdmission.from_dictionary(dictionary.get('payment_admission')) if 'payment_admission' in dictionary.keys() else APIHelper.SKIP
        payment_submission = RelationshipsPaymentSubmission.from_dictionary(dictionary.get('payment_submission')) if 'payment_submission' in dictionary.keys() else APIHelper.SKIP
        query = RelationshipsQuery.from_dictionary(dictionary.get('query')) if 'query' in dictionary.keys() else APIHelper.SKIP
        recall = RelationshipsPaymentRecall.from_dictionary(dictionary.get('recall')) if 'recall' in dictionary.keys() else APIHelper.SKIP
        recall_submission = RelationshipsPaymentRecallSubmission.from_dictionary(dictionary.get('recall_submission')) if 'recall_submission' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment,
                   payment_admission,
                   payment_submission,
                   query,
                   recall,
                   recall_submission)
