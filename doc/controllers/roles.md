# Roles

```python
roles_controller = client.roles
```

## Class Name

`RolesController`

## Methods

* [List All Roles](../../doc/controllers/roles.md#list-all-roles)
* [Create Role](../../doc/controllers/roles.md#create-role)
* [Delete Role](../../doc/controllers/roles.md#delete-role)
* [Fetch Role](../../doc/controllers/roles.md#fetch-role)


# List All Roles

List all roles

```python
def list_all_roles(self,
                  page_number=None,
                  page_size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |

## Response Type

[`RoleDetailsListResponse`](../../doc/models/role-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = roles_controller.list_all_roles(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Create Role

Create role

```python
def create_role(self,
               role_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_creation_request` | [`RoleCreation`](../../doc/models/role-creation.md) | Body, Optional | - |

## Response Type

[`RoleCreationResponse`](../../doc/models/role-creation-response.md)

## Example Usage

```python
role_creation_request = RoleCreation(
    data=Role(
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='role',
        version=0
    )
)

result = roles_controller.create_role(
    role_creation_request=role_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Delete Role

Delete role

```python
def delete_role(self,
               role_id,
               version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `uuid\|str` | Template, Required | Role Id |
| `version` | `int` | Query, Required | Version |

## Response Type

`void`

## Example Usage

```python
role_id = '000010c8-0000-0000-0000-000000000000'

version = 172

result = roles_controller.delete_role(
    role_id,
    version
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Role

Fetch role

```python
def fetch_role(self,
              role_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `uuid\|str` | Template, Required | Role Id |

## Response Type

[`RoleDetailsResponse`](../../doc/models/role-details-response.md)

## Example Usage

```python
role_id = '000010c8-0000-0000-0000-000000000000'

result = roles_controller.fetch_role(role_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

