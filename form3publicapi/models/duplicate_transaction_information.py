# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.query_reference import QueryReference


class DuplicateTransactionInformation(object):

    """Implementation of the 'DuplicateTransactionInformation' model.

    TODO: type model description here.

    Attributes:
        end_to_end_reference (str): Unique identification, as assigned by the
            initiating party, to unambiguously identify the transaction. This
            identification is passed on, unchanged, throughout the entire
            end-to-end chain.
        references (List[QueryReference]): Reference for the duplicated
            payment for this Exception and Investigation case.
        scheme_transaction_id (str): Unique identification, as assigned by the
            first instructing agent, to unambiguously identify the transaction
            that is passed on, unchanged, throughout the entire interbank
            chain.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_to_end_reference": 'end_to_end_reference',
        "references": 'references',
        "scheme_transaction_id": 'scheme_transaction_id'
    }

    _optionals = [
        'end_to_end_reference',
        'references',
        'scheme_transaction_id',
    ]

    def __init__(self,
                 end_to_end_reference=APIHelper.SKIP,
                 references=APIHelper.SKIP,
                 scheme_transaction_id=APIHelper.SKIP):
        """Constructor for the DuplicateTransactionInformation class"""

        # Initialize members of the class
        if end_to_end_reference is not APIHelper.SKIP:
            self.end_to_end_reference = end_to_end_reference 
        if references is not APIHelper.SKIP:
            self.references = references 
        if scheme_transaction_id is not APIHelper.SKIP:
            self.scheme_transaction_id = scheme_transaction_id 

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
        end_to_end_reference = dictionary.get("end_to_end_reference") if dictionary.get("end_to_end_reference") else APIHelper.SKIP
        references = None
        if dictionary.get('references') is not None:
            references = [QueryReference.from_dictionary(x) for x in dictionary.get('references')]
        else:
            references = APIHelper.SKIP
        scheme_transaction_id = dictionary.get("scheme_transaction_id") if dictionary.get("scheme_transaction_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(end_to_end_reference,
                   references,
                   scheme_transaction_id)
