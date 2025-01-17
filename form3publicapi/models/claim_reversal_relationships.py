# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.claim_1 import Claim1
from form3publicapi.models.claim_reversal_submission_2 import ClaimReversalSubmission2


class ClaimReversalRelationships(object):

    """Implementation of the 'ClaimReversalRelationships' model.

    TODO: type model description here.

    Attributes:
        claim (Claim1): TODO: type description here.
        claim_reversal_submission (ClaimReversalSubmission2): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "claim": 'claim',
        "claim_reversal_submission": 'claim_reversal_submission'
    }

    _optionals = [
        'claim',
        'claim_reversal_submission',
    ]

    def __init__(self,
                 claim=APIHelper.SKIP,
                 claim_reversal_submission=APIHelper.SKIP):
        """Constructor for the ClaimReversalRelationships class"""

        # Initialize members of the class
        if claim is not APIHelper.SKIP:
            self.claim = claim 
        if claim_reversal_submission is not APIHelper.SKIP:
            self.claim_reversal_submission = claim_reversal_submission 

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
        claim = Claim1.from_dictionary(dictionary.get('claim')) if 'claim' in dictionary.keys() else APIHelper.SKIP
        claim_reversal_submission = ClaimReversalSubmission2.from_dictionary(dictionary.get('claim_reversal_submission')) if 'claim_reversal_submission' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(claim,
                   claim_reversal_submission)
