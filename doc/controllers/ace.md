# ACE

```python
ace_controller = client.ace
```

## Class Name

`ACEController`

## Methods

* [List All Access Controls for Role](../../doc/controllers/ace.md#list-all-access-controls-for-role)
* [Create Access Control Entry](../../doc/controllers/ace.md#create-access-control-entry)
* [Delete Access Control Entry](../../doc/controllers/ace.md#delete-access-control-entry)
* [Fetch Access Control Entry](../../doc/controllers/ace.md#fetch-access-control-entry)


# List All Access Controls for Role

List all Access Controls for role

```python
def list_all_access_controls_for_role(self,
                                     role_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `uuid\|str` | Template, Required | Role Id |

## Response Type

[`AceDetailsListResponse`](../../doc/models/ace-details-list-response.md)

## Example Usage

```python
role_id = '000010c8-0000-0000-0000-000000000000'

result = ace_controller.list_all_access_controls_for_role(role_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Access Control Entry

Create Access Control Entry

```python
def create_access_control_entry(self,
                               role_id,
                               ace_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `uuid\|str` | Template, Required | Role Id |
| `ace_creation_request` | [`AceCreation`](../../doc/models/ace-creation.md) | Body, Optional | - |

## Response Type

[`AceCreationResponse`](../../doc/models/ace-creation-response.md)

## Example Usage

```python
role_id = '000010c8-0000-0000-0000-000000000000'

ace_creation_request = AceCreation(
    data=Ace(
        attributes=Attributes2(
            action='CREATE',
            record_type='User',
            role_id='813e371b-c16c-4b86-adbf-82bcda159b27'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='ace',
        version=0
    )
)

result = ace_controller.create_access_control_entry(
    role_id,
    ace_creation_request=ace_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Delete Access Control Entry

Delete Access Control Entry

```python
def delete_access_control_entry(self,
                               role_id,
                               ace_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `uuid\|str` | Template, Required | Role Id |
| `ace_id` | `uuid\|str` | Template, Required | Ace Id |

## Response Type

`void`

## Example Usage

```python
role_id = '000010c8-0000-0000-0000-000000000000'

ace_id = '00000806-0000-0000-0000-000000000000'

result = ace_controller.delete_access_control_entry(
    role_id,
    ace_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Access Control Entry

Fetch Access Control Entry

```python
def fetch_access_control_entry(self,
                              role_id,
                              ace_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `uuid\|str` | Template, Required | Role Id |
| `ace_id` | `uuid\|str` | Template, Required | Ace Id |

## Response Type

[`AceDetailsResponse`](../../doc/models/ace-details-response.md)

## Example Usage

```python
role_id = '000010c8-0000-0000-0000-000000000000'

ace_id = '00000806-0000-0000-0000-000000000000'

result = ace_controller.fetch_access_control_entry(
    role_id,
    ace_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

