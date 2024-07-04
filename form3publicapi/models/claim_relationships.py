# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.claim_reversal_2 import ClaimReversal2
from form3publicapi.models.claim_submission_2 import ClaimSubmission2


class ClaimRelationships(object):

    """Implementation of the 'ClaimRelationships' model.

    TODO: type model description here.

    Attributes:
        claim_reversal (ClaimReversal2): TODO: type description here.
        claim_submission (ClaimSubmission2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "claim_reversal": 'claim_reversal',
        "claim_submission": 'claim_submission'
    }

    _optionals = [
        'claim_reversal',
        'claim_submission',
    ]

    def __init__(self,
                 claim_reversal=APIHelper.SKIP,
                 claim_submission=APIHelper.SKIP):
        """Constructor for the ClaimRelationships class"""

        # Initialize members of the class
        if claim_reversal is not APIHelper.SKIP:
            self.claim_reversal = claim_reversal 
        if claim_submission is not APIHelper.SKIP:
            self.claim_submission = claim_submission 

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
        claim_reversal = ClaimReversal2.from_dictionary(dictionary.get('claim_reversal')) if 'claim_reversal' in dictionary.keys() else APIHelper.SKIP
        claim_submission = ClaimSubmission2.from_dictionary(dictionary.get('claim_submission')) if 'claim_submission' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(claim_reversal,
                   claim_submission)
