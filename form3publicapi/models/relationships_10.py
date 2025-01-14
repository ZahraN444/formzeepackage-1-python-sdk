# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.direct_debit_1 import DirectDebit1
from form3publicapi.models.direct_debit_return_admission_2 import DirectDebitReturnAdmission2
from form3publicapi.models.direct_debit_return_reversal_2 import DirectDebitReturnReversal2
from form3publicapi.models.direct_debit_return_submission_2 import DirectDebitReturnSubmission2


class Relationships10(object):

    """Implementation of the 'Relationships10' model.

    TODO: type model description here.

    Attributes:
        direct_debit (DirectDebit1): TODO: type description here.
        direct_debit_return_admission (DirectDebitReturnAdmission2): TODO:
            type description here.
        direct_debit_return_reversal (DirectDebitReturnReversal2): TODO: type
            description here.
        direct_debit_return_submission (DirectDebitReturnSubmission2): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "direct_debit": 'direct_debit',
        "direct_debit_return_admission": 'direct_debit_return_admission',
        "direct_debit_return_reversal": 'direct_debit_return_reversal',
        "direct_debit_return_submission": 'direct_debit_return_submission'
    }

    _optionals = [
        'direct_debit',
        'direct_debit_return_admission',
        'direct_debit_return_reversal',
        'direct_debit_return_submission',
    ]

    def __init__(self,
                 direct_debit=APIHelper.SKIP,
                 direct_debit_return_admission=APIHelper.SKIP,
                 direct_debit_return_reversal=APIHelper.SKIP,
                 direct_debit_return_submission=APIHelper.SKIP):
        """Constructor for the Relationships10 class"""

        # Initialize members of the class
        if direct_debit is not APIHelper.SKIP:
            self.direct_debit = direct_debit 
        if direct_debit_return_admission is not APIHelper.SKIP:
            self.direct_debit_return_admission = direct_debit_return_admission 
        if direct_debit_return_reversal is not APIHelper.SKIP:
            self.direct_debit_return_reversal = direct_debit_return_reversal 
        if direct_debit_return_submission is not APIHelper.SKIP:
            self.direct_debit_return_submission = direct_debit_return_submission 

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
        direct_debit = DirectDebit1.from_dictionary(dictionary.get('direct_debit')) if 'direct_debit' in dictionary.keys() else APIHelper.SKIP
        direct_debit_return_admission = DirectDebitReturnAdmission2.from_dictionary(dictionary.get('direct_debit_return_admission')) if 'direct_debit_return_admission' in dictionary.keys() else APIHelper.SKIP
        direct_debit_return_reversal = DirectDebitReturnReversal2.from_dictionary(dictionary.get('direct_debit_return_reversal')) if 'direct_debit_return_reversal' in dictionary.keys() else APIHelper.SKIP
        direct_debit_return_submission = DirectDebitReturnSubmission2.from_dictionary(dictionary.get('direct_debit_return_submission')) if 'direct_debit_return_submission' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(direct_debit,
                   direct_debit_return_admission,
                   direct_debit_return_reversal,
                   direct_debit_return_submission)
