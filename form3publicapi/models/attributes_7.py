# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes7(object):

    """Implementation of the 'Attributes7' model.

    TODO: type model description here.

    Attributes:
        assignee (PaymentAdmissionTaskAssigneeEnum): Helps to identify the
            owner of the task
        name (str): Identifies the payment admission task to be executed
        output (Dict[str, object]): Key Value map that contains the Task
            result.
        status (PaymentAdmissionTaskStatusEnum): status of the task
        workflow (uuid|str): Identifies the workflow for which the task was
            created

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "assignee": 'assignee',
        "name": 'name',
        "output": 'output',
        "status": 'status',
        "workflow": 'workflow'
    }

    _optionals = [
        'assignee',
        'name',
        'output',
        'status',
        'workflow',
    ]

    def __init__(self,
                 assignee=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 output=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 workflow=APIHelper.SKIP):
        """Constructor for the Attributes7 class"""

        # Initialize members of the class
        if assignee is not APIHelper.SKIP:
            self.assignee = assignee 
        if name is not APIHelper.SKIP:
            self.name = name 
        if output is not APIHelper.SKIP:
            self.output = output 
        if status is not APIHelper.SKIP:
            self.status = status 
        if workflow is not APIHelper.SKIP:
            self.workflow = workflow 

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
        assignee = dictionary.get("assignee") if dictionary.get("assignee") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        output = dictionary.get("output") if dictionary.get("output") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        workflow = dictionary.get("workflow") if dictionary.get("workflow") else APIHelper.SKIP
        # Return an object of this model
        return cls(assignee,
                   name,
                   output,
                   status,
                   workflow)
