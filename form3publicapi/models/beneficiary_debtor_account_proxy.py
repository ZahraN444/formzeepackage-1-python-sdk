# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class BeneficiaryDebtorAccountProxy(object):

    """Implementation of the 'BeneficiaryDebtorAccountProxy' model.

    TODO: type model description here.

    Attributes:
        proxy (str): Name of the identification scheme, in a free text form.
            When used proxy_id_code must not be present
        proxy_id (str): Identification used to indicate the account
            identification under another specified name
        proxy_id_code (str): Name of the identification scheme, in a coded
            form as published in an external list. When used proxy field must
            not be present

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "proxy": 'proxy',
        "proxy_id": 'proxy_id',
        "proxy_id_code": 'proxy_id_code'
    }

    _optionals = [
        'proxy',
        'proxy_id',
        'proxy_id_code',
    ]

    def __init__(self,
                 proxy=APIHelper.SKIP,
                 proxy_id=APIHelper.SKIP,
                 proxy_id_code=APIHelper.SKIP):
        """Constructor for the BeneficiaryDebtorAccountProxy class"""

        # Initialize members of the class
        if proxy is not APIHelper.SKIP:
            self.proxy = proxy 
        if proxy_id is not APIHelper.SKIP:
            self.proxy_id = proxy_id 
        if proxy_id_code is not APIHelper.SKIP:
            self.proxy_id_code = proxy_id_code 

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
        proxy = dictionary.get("proxy") if dictionary.get("proxy") else APIHelper.SKIP
        proxy_id = dictionary.get("proxy_id") if dictionary.get("proxy_id") else APIHelper.SKIP
        proxy_id_code = dictionary.get("proxy_id_code") if dictionary.get("proxy_id_code") else APIHelper.SKIP
        # Return an object of this model
        return cls(proxy,
                   proxy_id,
                   proxy_id_code)
