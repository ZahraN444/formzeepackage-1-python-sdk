# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class PrivateIdentification(object):

    """Implementation of the 'PrivateIdentification' model.

    TODO: type model description here.

    Attributes:
        identification (str): Private Identification of an debtor/beneficiary
            or ultimate debtor/beneficiary
        identification_issuer (str): Issuer of the `identification`
        identification_scheme (str): Scheme of the `identification`
        identification_scheme_code (str): The code that specifies the type of
            `identification`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "identification": 'identification',
        "identification_issuer": 'identification_issuer',
        "identification_scheme": 'identification_scheme',
        "identification_scheme_code": 'identification_scheme_code'
    }

    _optionals = [
        'identification',
        'identification_issuer',
        'identification_scheme',
        'identification_scheme_code',
    ]

    def __init__(self,
                 identification=APIHelper.SKIP,
                 identification_issuer=APIHelper.SKIP,
                 identification_scheme=APIHelper.SKIP,
                 identification_scheme_code=APIHelper.SKIP):
        """Constructor for the PrivateIdentification class"""

        # Initialize members of the class
        if identification is not APIHelper.SKIP:
            self.identification = identification 
        if identification_issuer is not APIHelper.SKIP:
            self.identification_issuer = identification_issuer 
        if identification_scheme is not APIHelper.SKIP:
            self.identification_scheme = identification_scheme 
        if identification_scheme_code is not APIHelper.SKIP:
            self.identification_scheme_code = identification_scheme_code 

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
        identification = dictionary.get("identification") if dictionary.get("identification") else APIHelper.SKIP
        identification_issuer = dictionary.get("identification_issuer") if dictionary.get("identification_issuer") else APIHelper.SKIP
        identification_scheme = dictionary.get("identification_scheme") if dictionary.get("identification_scheme") else APIHelper.SKIP
        identification_scheme_code = dictionary.get("identification_scheme_code") if dictionary.get("identification_scheme_code") else APIHelper.SKIP
        # Return an object of this model
        return cls(identification,
                   identification_issuer,
                   identification_scheme,
                   identification_scheme_code)
