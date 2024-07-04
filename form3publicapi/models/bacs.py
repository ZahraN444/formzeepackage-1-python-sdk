# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class BACS(object):

    """Implementation of the 'BACS' model.

    TODO: type model description here.

    Attributes:
        accepts_payments (bool): TODO: type description here.
        account_switching (AccountSwitchingEnum): TODO: type description
            here.
        allowed_transactions (List[TransactionGroupCodeEnum]): TODO: type
            description here.
        service_status (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accepts_payments": 'accepts_payments',
        "account_switching": 'account_switching',
        "allowed_transactions": 'allowed_transactions',
        "service_status": 'service_status'
    }

    _optionals = [
        'accepts_payments',
        'account_switching',
        'allowed_transactions',
        'service_status',
    ]

    def __init__(self,
                 accepts_payments=False,
                 account_switching=APIHelper.SKIP,
                 allowed_transactions=APIHelper.SKIP,
                 service_status=APIHelper.SKIP):
        """Constructor for the BACS class"""

        # Initialize members of the class
        self.accepts_payments = accepts_payments 
        if account_switching is not APIHelper.SKIP:
            self.account_switching = account_switching 
        if allowed_transactions is not APIHelper.SKIP:
            self.allowed_transactions = allowed_transactions 
        if service_status is not APIHelper.SKIP:
            self.service_status = service_status 

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
        accepts_payments = dictionary.get("accepts_payments") if dictionary.get("accepts_payments") else False
        account_switching = dictionary.get("account_switching") if dictionary.get("account_switching") else APIHelper.SKIP
        allowed_transactions = dictionary.get("allowed_transactions") if dictionary.get("allowed_transactions") else APIHelper.SKIP
        service_status = dictionary.get("service_status") if dictionary.get("service_status") else APIHelper.SKIP
        # Return an object of this model
        return cls(accepts_payments,
                   account_switching,
                   allowed_transactions,
                   service_status)