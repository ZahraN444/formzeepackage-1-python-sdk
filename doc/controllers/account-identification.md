# Account Identification

```python
account_identification_controller = client.account_identification
```

## Class Name

`AccountIdentificationController`

## Methods

* [List Account Identifications by Account](../../doc/controllers/account-identification.md#list-account-identifications-by-account)
* [Create an Identification for an Existing Account](../../doc/controllers/account-identification.md#create-an-identification-for-an-existing-account)
* [Delete Account Identification](../../doc/controllers/account-identification.md#delete-account-identification)
* [Get an Account Identification by Id](../../doc/controllers/account-identification.md#get-an-account-identification-by-id)
* [Amend Account Identification](../../doc/controllers/account-identification.md#amend-account-identification)


# List Account Identifications by Account

List Account Identifications by Account

```python
def list_account_identifications_by_account(self,
                                           account_id,
                                           page_number=None,
                                           page_size=None,
                                           filter_organisation_id=None,
                                           filter_secondary_identification=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `uuid\|str` | Template, Required | Account Id to which this identification relates to |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_secondary_identification` | `List[str]` | Query, Optional | Filter to only include account identifications with specified secondary_identification |

## Response Type

[`AccountIdentificationListResponse`](../../doc/models/account-identification-list-response.md)

## Example Usage

```python
account_id = '00001114-0000-0000-0000-000000000000'

Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = account_identification_controller.list_account_identifications_by_account(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')account_id)
print(result)
```


# Create an Identification for an Existing Account

Create an identification for an existing Account

```python
def create_an_identification_for_an_existing_account(self,
                                                    account_id,
                                                    account_identification_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `uuid\|str` | Template, Required | Account Id to which this identification relates to |
| `account_identification_creation_request` | [`AccountIdentificationRequest`](../../doc/models/account-identification-request.md) | Body, Optional | - |

## Response Type

[`AccountIdentificationResponse`](../../doc/models/account-identification-response.md)

## Example Usage

```python
account_id = '00001114-0000-0000-0000-000000000000'

account_identification_creation_request = AccountIdentificationRequest(
    data=AccountIdentification(
        attributes=AccountIdentificationAttributes(
            secondary_identification='secondary_identification2'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='account_identifications',
        version=0
    )
)

result = account_identification_controller.create_an_identification_for_an_existing_account(
    account_id,
    account_identification_creation_request=account_identification_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 409 | Account Identification creation error, constraint violation of secondary identification | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Delete Account Identification

Delete account identification

```python
def delete_account_identification(self,
                                 account_id,
                                 identification_id,
                                 version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `uuid\|str` | Template, Required | Account Id |
| `identification_id` | `uuid\|str` | Template, Required | Account Identification Id |
| `version` | `int` | Query, Required | Version |

## Response Type

`void`

## Example Usage

```python
account_id = '00001114-0000-0000-0000-000000000000'

identification_id = '000011c0-0000-0000-0000-000000000000'

version = 172

result = account_identification_controller.delete_account_identification(
    account_id,
    identification_id,
    version
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Account Identification not found | `APIException` |


# Get an Account Identification by Id

Get an account identification by id

```python
def get_an_account_identification_by_id(self,
                                       account_id,
                                       identification_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `uuid\|str` | Template, Required | Account Id |
| `identification_id` | `uuid\|str` | Template, Required | Account Identification Id |

## Response Type

[`AccountIdentificationResponse`](../../doc/models/account-identification-response.md)

## Example Usage

```python
account_id = '00001114-0000-0000-0000-000000000000'

identification_id = '000011c0-0000-0000-0000-000000000000'

result = account_identification_controller.get_an_account_identification_by_id(
    account_id,
    identification_id
)
print(result)
```


# Amend Account Identification

Amend Account Identification

```python
def amend_account_identification(self,
                                account_id,
                                identification_id,
                                account_identification_amend_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `uuid\|str` | Template, Required | Account Id |
| `identification_id` | `uuid\|str` | Template, Required | Account Identification Id; Must match id in the payload |
| `account_identification_amend_request` | [`AccountIdentificationRequest`](../../doc/models/account-identification-request.md) | Body, Optional | - |

## Response Type

[`AccountIdentificationResponse`](../../doc/models/account-identification-response.md)

## Example Usage

```python
account_id = '00001114-0000-0000-0000-000000000000'

identification_id = '000011c0-0000-0000-0000-000000000000'

account_identification_amend_request = AccountIdentificationRequest(
    data=AccountIdentification(
        attributes=AccountIdentificationAttributes(
            secondary_identification='secondary_identification2'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='account_identifications',
        version=0
    )
)

result = account_identification_controller.amend_account_identification(
    account_id,
    identification_id,
    account_identification_amend_request=account_identification_amend_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 409 | Account Identification update error, constraint violation of secondary identification | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

