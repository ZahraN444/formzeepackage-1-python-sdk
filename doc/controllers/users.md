# Users

```python
users_controller = client.users
```

## Class Name

`UsersController`

## Methods

* [List All Users](../../doc/controllers/users.md#list-all-users)
* [Create User](../../doc/controllers/users.md#create-user)
* [Delete User](../../doc/controllers/users.md#delete-user)
* [Fetch User](../../doc/controllers/users.md#fetch-user)
* [Update User Details](../../doc/controllers/users.md#update-user-details)
* [Fetch Access Control List for User](../../doc/controllers/users.md#fetch-access-control-list-for-user)
* [Fetch Credentials for User](../../doc/controllers/users.md#fetch-credentials-for-user)
* [Create New Credentials for User](../../doc/controllers/users.md#create-new-credentials-for-user)
* [Delete Credentials for User](../../doc/controllers/users.md#delete-credentials-for-user)
* [Fetch All Roles for User](../../doc/controllers/users.md#fetch-all-roles-for-user)
* [Remove Role From User](../../doc/controllers/users.md#remove-role-from-user)
* [Add Role to User](../../doc/controllers/users.md#add-role-to-user)


# List All Users

List all users

```python
def list_all_users(self,
                  page_number=None,
                  page_size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |

## Response Type

[`UserDetailsListResponse`](../../doc/models/user-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = users_controller.list_all_users(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Create User

Create user

```python
def create_user(self,
               user_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_creation_request` | [`UserCreation`](../../doc/models/user-creation.md) | Body, Optional | - |

## Response Type

[`UserCreationResponse`](../../doc/models/user-creation-response.md)

## Example Usage

```python
user_creation_request = UserCreation(
    data=User(
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='User',
        version=0
    )
)

result = users_controller.create_user(
    user_creation_request=user_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Delete User

Delete user

```python
def delete_user(self,
               user_id,
               version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |
| `version` | `int` | Query, Required | Version |

## Response Type

`void`

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

version = 172

result = users_controller.delete_user(
    user_id,
    version
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch User

Fetch user

```python
def fetch_user(self,
              user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |

## Response Type

[`UserDetailsResponse`](../../doc/models/user-details-response.md)

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

result = users_controller.fetch_user(user_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Update User Details

Update user details

```python
def update_user_details(self,
                       user_id,
                       user_update_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |
| `user_update_request` | [`UserCreation`](../../doc/models/user-creation.md) | Body, Optional | - |

## Response Type

[`UserDetailsResponse`](../../doc/models/user-details-response.md)

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

user_update_request = UserCreation(
    data=User(
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='User',
        version=0
    )
)

result = users_controller.update_user_details(
    user_id,
    user_update_request=user_update_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Access Control List for User

Fetch access control list for user

```python
def fetch_access_control_list_for_user(self,
                                      user_id,
                                      filter_record_type=None,
                                      filter_action=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |
| `filter_record_type` | `str` | Query, Optional | Record type |
| `filter_action` | `str` | Query, Optional | Access action |

## Response Type

[`AceDetailsListResponse`](../../doc/models/ace-details-list-response.md)

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = users_controller.fetch_access_control_list_for_user(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')user_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Credentials for User

Fetch credentials for user

```python
def fetch_credentials_for_user(self,
                              user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |

## Response Type

[`UserCredentialListResponse`](../../doc/models/user-credential-list-response.md)

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

result = users_controller.fetch_credentials_for_user(user_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create New Credentials for User

Create new credentials for user

```python
def create_new_credentials_for_user(self,
                                   user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |

## Response Type

[`CredentialCreationResponse`](../../doc/models/credential-creation-response.md)

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

result = users_controller.create_new_credentials_for_user(user_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Delete Credentials for User

Delete credentials for user

```python
def delete_credentials_for_user(self,
                               user_id,
                               client_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |
| `client_id` | `str` | Template, Required | client id |

## Response Type

`void`

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

client_id = 'client_id8'

result = users_controller.delete_credentials_for_user(
    user_id,
    client_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch All Roles for User

Fetch all roles for user

```python
def fetch_all_roles_for_user(self,
                            user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |

## Response Type

[`UserRoleListResponse`](../../doc/models/user-role-list-response.md)

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

result = users_controller.fetch_all_roles_for_user(user_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Remove Role From User

Remove role from user

```python
def remove_role_from_user(self,
                         user_id,
                         role_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |
| `role_id` | `uuid\|str` | Template, Required | Role Id |

## Response Type

`void`

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

role_id = '000010c8-0000-0000-0000-000000000000'

result = users_controller.remove_role_from_user(
    user_id,
    role_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Add Role to User

Add role to user

```python
def add_role_to_user(self,
                    user_id,
                    role_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `uuid\|str` | Template, Required | User Id |
| `role_id` | `uuid\|str` | Template, Required | Role Id |

## Response Type

`void`

## Example Usage

```python
user_id = '00001e80-0000-0000-0000-000000000000'

role_id = '000010c8-0000-0000-0000-000000000000'

result = users_controller.add_role_to_user(
    user_id,
    role_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

