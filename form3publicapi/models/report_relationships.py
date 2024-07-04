# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper
from form3publicapi.models.report_admission_2 import ReportAdmission2
from form3publicapi.models.report_request_1 import ReportRequest1
from form3publicapi.models.thin_relationship import ThinRelationship


class ReportRelationships(object):

    """Implementation of the 'ReportRelationships' model.

    TODO: type model description here.

    Attributes:
        report_admission (ReportAdmission2): TODO: type description here.
        report_request (ReportRequest1): TODO: type description here.
        transaction_file (ThinRelationship): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "report_admission": 'report_admission',
        "report_request": 'report_request',
        "transaction_file": 'transaction_file'
    }

    _optionals = [
        'report_admission',
        'report_request',
        'transaction_file',
    ]

    def __init__(self,
                 report_admission=APIHelper.SKIP,
                 report_request=APIHelper.SKIP,
                 transaction_file=APIHelper.SKIP):
        """Constructor for the ReportRelationships class"""

        # Initialize members of the class
        if report_admission is not APIHelper.SKIP:
            self.report_admission = report_admission 
        if report_request is not APIHelper.SKIP:
            self.report_request = report_request 
        if transaction_file is not APIHelper.SKIP:
            self.transaction_file = transaction_file 

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
        report_admission = ReportAdmission2.from_dictionary(dictionary.get('report_admission')) if 'report_admission' in dictionary.keys() else APIHelper.SKIP
        report_request = ReportRequest1.from_dictionary(dictionary.get('report_request')) if 'report_request' in dictionary.keys() else APIHelper.SKIP
        transaction_file = ThinRelationship.from_dictionary(dictionary.get('transaction_file')) if 'transaction_file' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(report_admission,
                   report_request,
                   transaction_file)