# Branches

```python
branches_controller = client.branches
```

## Class Name

`BranchesController`

## Methods

* [List Branches](../../doc/controllers/branches.md#list-branches)
* [Create a Branch](../../doc/controllers/branches.md#create-a-branch)
* [Delete Branch](../../doc/controllers/branches.md#delete-branch)
* [Fetch Branch](../../doc/controllers/branches.md#fetch-branch)
* [Amend Branch](../../doc/controllers/branches.md#amend-branch)


# List Branches

List branches

```python
def list_branches(self,
                 page_number=None,
                 page_size=None,
                 filter_organisation_id=None,
                 filter_bank_id=None,
                 filter_bank_id_code=None,
                 filter_acceptance_qualifier=None,
                 filter_validation_type=None,
                 filter_reference_mask=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_bank_id` | `List[str]` | Query, Optional | Filter by bank id e.g. sort code or bic |
| `filter_bank_id_code` | `List[str]` | Query, Optional | Filter by type of bank id e.g. "GBDSC" |
| `filter_acceptance_qualifier` | `List[str]` | Query, Optional | Filter by acceptance qualifier |
| `filter_validation_type` | `List[str]` | Query, Optional | Filter by validation type e.g. card |
| `filter_reference_mask` | `List[str]` | Query, Optional | Filter by reference mask |

## Response Type

[`BranchDetailsListResponse`](../../doc/models/branch-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = branches_controller.list_branches(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Create a Branch

Create a Branch

```python
def create_a_branch(self,
                   branch_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_creation_request` | [`BranchCreation`](../../doc/models/branch-creation.md) | Body, Optional | - |

## Response Type

[`BranchCreationResponse`](../../doc/models/branch-creation-response.md)

## Example Usage

```python
branch_creation_request = BranchCreation(
    data=Branch(
        attributes=BranchAttributes(
            bank_id='400300',
            bank_id_code='GBDSC',
            reference_mask='4929############'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='branches',
        version=0
    )
)

result = branches_controller.create_a_branch(
    branch_creation_request=branch_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 409 | Branch creation error, constraint violation of organisation id and bank id | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Delete Branch

Delete branch

```python
def delete_branch(self,
                 id,
                 version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Branch Id |
| `version` | `int` | Query, Required | Version |

## Response Type

`void`

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

version = 172

result = branches_controller.delete_branch(
    id,
    version
)
print(result)
```


# Fetch Branch

Fetch branch

```python
def fetch_branch(self,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Branch Id |

## Response Type

[`BranchDetailsResponse`](../../doc/models/branch-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = branches_controller.fetch_branch(id)
print(result)
```


# Amend Branch

Amend branch

```python
def amend_branch(self,
                id,
                branch_amend_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Branches Id |
| `branch_amend_request` | [`BranchAmendment`](../../doc/models/branch-amendment.md) | Body, Optional | - |

## Response Type

[`BranchDetailsResponse`](../../doc/models/branch-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = branches_controller.amend_branch(id)
print(result)
```

