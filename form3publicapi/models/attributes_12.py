# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from form3publicapi.api_helper import APIHelper


class Attributes12(object):

    """Implementation of the 'Attributes12' model.

    TODO: type model description here.

    Attributes:
        assignee (ReturnSubmissionTaskAssigneeEnum): Helps to identify the
            owner of the task
        input (Dict[str, object]): Key Value map that contains additional data
            for executing the task.
        name (str): Identifies the return submission task to be executed
        output (Dict[str, object]): Key Value map that contains the Task
            result.
        status (ReturnSubmissionTaskStatusEnum): status of the return
            submission task

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "assignee": 'assignee',
        "input": 'input',
        "name": 'name',
        "output": 'output',
        "status": 'status'
    }

    _optionals = [
        'assignee',
        'input',
        'name',
        'output',
        'status',
    ]

    def __init__(self,
                 assignee=APIHelper.SKIP,
                 input=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 output=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the Attributes12 class"""

        # Initialize members of the class
        if assignee is not APIHelper.SKIP:
            self.assignee = assignee 
        if input is not APIHelper.SKIP:
            self.input = input 
        if name is not APIHelper.SKIP:
            self.name = name 
        if output is not APIHelper.SKIP:
            self.output = output 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        input = dictionary.get("input") if dictionary.get("input") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        output = dictionary.get("output") if dictionary.get("output") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(assignee,
                   input,
                   name,
                   output,
                   status)
