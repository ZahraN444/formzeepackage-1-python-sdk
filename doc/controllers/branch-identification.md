# Branch Identification

```python
branch_identification_controller = client.branch_identification
```

## Class Name

`BranchIdentificationController`

## Methods

* [List Branch Identifications by Branch](../../doc/controllers/branch-identification.md#list-branch-identifications-by-branch)
* [Create an Identification for an Existing Branch](../../doc/controllers/branch-identification.md#create-an-identification-for-an-existing-branch)
* [Delete Branch Identification](../../doc/controllers/branch-identification.md#delete-branch-identification)
* [Get a Branch Identification by Id](../../doc/controllers/branch-identification.md#get-a-branch-identification-by-id)
* [Amend Branch Identification](../../doc/controllers/branch-identification.md#amend-branch-identification)


# List Branch Identifications by Branch

List Branch Identifications by Branch

```python
def list_branch_identifications_by_branch(self,
                                         branch_id,
                                         page_number=None,
                                         page_size=None,
                                         filter_organisation_id=None,
                                         filter_secondary_identification=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_id` | `uuid\|str` | Template, Required | Branch Id to which this identification relates to |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_secondary_identification` | `List[str]` | Query, Optional | Filter to only include branch identifications with specified secondary_identification |

## Response Type

[`BranchIdentificationListResponse`](../../doc/models/branch-identification-list-response.md)

## Example Usage

```python
branch_id = '000005ee-0000-0000-0000-000000000000'

Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = branch_identification_controller.list_branch_identifications_by_branch(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')branch_id)
print(result)
```


# Create an Identification for an Existing Branch

Create an identification for an existing Branch

```python
def create_an_identification_for_an_existing_branch(self,
                                                   branch_id,
                                                   branch_identification_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_id` | `uuid\|str` | Template, Required | Branch Id to which this identification relates to |
| `branch_identification_creation_request` | [`BranchIdentificationRequest`](../../doc/models/branch-identification-request.md) | Body, Optional | - |

## Response Type

[`BranchIdentificationResponse`](../../doc/models/branch-identification-response.md)

## Example Usage

```python
branch_id = '000005ee-0000-0000-0000-000000000000'

branch_identification_creation_request = BranchIdentificationRequest(
    data=BranchIdentification(
        attributes=BranchIdentificationAttributes(
            secondary_identification='secondary_identification2'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='branch_identifications',
        version=0
    )
)

result = branch_identification_controller.create_an_identification_for_an_existing_branch(
    branch_id,
    branch_identification_creation_request=branch_identification_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 409 | Branch Identification creation error, constraint violation of secondary identification | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Delete Branch Identification

Delete branch identification

```python
def delete_branch_identification(self,
                                branch_id,
                                identification_id,
                                version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_id` | `uuid\|str` | Template, Required | Branch Id |
| `identification_id` | `uuid\|str` | Template, Required | Branch Identification Id |
| `version` | `int` | Query, Required | Version |

## Response Type

`void`

## Example Usage

```python
branch_id = '000005ee-0000-0000-0000-000000000000'

identification_id = '000011c0-0000-0000-0000-000000000000'

version = 172

result = branch_identification_controller.delete_branch_identification(
    branch_id,
    identification_id,
    version
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Branch Identification not found | `APIException` |


# Get a Branch Identification by Id

Get a branch identification by id

```python
def get_a_branch_identification_by_id(self,
                                     branch_id,
                                     identification_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_id` | `uuid\|str` | Template, Required | Branch Id |
| `identification_id` | `uuid\|str` | Template, Required | Branch Identification Id |

## Response Type

[`BranchIdentificationResponse`](../../doc/models/branch-identification-response.md)

## Example Usage

```python
branch_id = '000005ee-0000-0000-0000-000000000000'

identification_id = '000011c0-0000-0000-0000-000000000000'

result = branch_identification_controller.get_a_branch_identification_by_id(
    branch_id,
    identification_id
)
print(result)
```


# Amend Branch Identification

Amend Branch Identification

```python
def amend_branch_identification(self,
                               branch_id,
                               identification_id,
                               branch_identification_amend_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_id` | `uuid\|str` | Template, Required | Branch Id |
| `identification_id` | `uuid\|str` | Template, Required | Branch Identification Id; Must match id in the payload |
| `branch_identification_amend_request` | [`BranchIdentificationRequest`](../../doc/models/branch-identification-request.md) | Body, Optional | - |

## Response Type

[`BranchIdentificationResponse`](../../doc/models/branch-identification-response.md)

## Example Usage

```python
branch_id = '000005ee-0000-0000-0000-000000000000'

identification_id = '000011c0-0000-0000-0000-000000000000'

branch_identification_amend_request = BranchIdentificationRequest(
    data=BranchIdentification(
        attributes=BranchIdentificationAttributes(
            secondary_identification='secondary_identification2'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='branch_identifications',
        version=0
    )
)

result = branch_identification_controller.amend_branch_identification(
    branch_id,
    identification_id,
    branch_identification_amend_request=branch_identification_amend_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 409 | Branch Identification update error, constraint violation of secondary identification | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

