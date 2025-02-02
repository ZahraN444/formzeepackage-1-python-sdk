# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.header import Header


class Swift(object):

    """Implementation of the 'Swift' model.

    TODO: type model description here.

    Attributes:
        bank_operation_code (str): SWIFT service level
        header (Header): TODO: type description here.
        instruction_code (str): A SWIFT instruction code
        sender_receiver_information (str): This field specifies additional
            information for the Receiver or other party specified.
        time_indication (str): This repetitive field specifies one or several
            time indication(s) related to the processing of the payment
            instruction.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_operation_code": 'bank_operation_code',
        "header": 'header',
        "instruction_code": 'instruction_code',
        "sender_receiver_information": 'sender_receiver_information',
        "time_indication": 'time_indication'
    }

    _optionals = [
        'bank_operation_code',
        'header',
        'instruction_code',
        'sender_receiver_information',
        'time_indication',
    ]

    def __init__(self,
                 bank_operation_code=APIHelper.SKIP,
                 header=APIHelper.SKIP,
                 instruction_code=APIHelper.SKIP,
                 sender_receiver_information=APIHelper.SKIP,
                 time_indication=APIHelper.SKIP):
        """Constructor for the Swift class"""

        # Initialize members of the class
        if bank_operation_code is not APIHelper.SKIP:
            self.bank_operation_code = bank_operation_code 
        if header is not APIHelper.SKIP:
            self.header = header 
        if instruction_code is not APIHelper.SKIP:
            self.instruction_code = instruction_code 
        if sender_receiver_information is not APIHelper.SKIP:
            self.sender_receiver_information = sender_receiver_information 
        if time_indication is not APIHelper.SKIP:
            self.time_indication = time_indication 

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
        bank_operation_code = dictionary.get("bank_operation_code") if dictionary.get("bank_operation_code") else APIHelper.SKIP
        header = Header.from_dictionary(dictionary.get('header')) if 'header' in dictionary.keys() else APIHelper.SKIP
        instruction_code = dictionary.get("instruction_code") if dictionary.get("instruction_code") else APIHelper.SKIP
        sender_receiver_information = dictionary.get("sender_receiver_information") if dictionary.get("sender_receiver_information") else APIHelper.SKIP
        time_indication = dictionary.get("time_indication") if dictionary.get("time_indication") else APIHelper.SKIP
        # Return an object of this model
        return cls(bank_operation_code,
                   header,
                   instruction_code,
                   sender_receiver_information,
                   time_indication)
