# Platformsecurityapi

```python
platformsecurityapi_controller = client.platformsecurityapi
```

## Class Name

`PlatformsecurityapiController`

## Methods

* [Get a List of Signing Keys](../../doc/controllers/platformsecurityapi.md#get-a-list-of-signing-keys)
* [Fetch a Signing Key](../../doc/controllers/platformsecurityapi.md#fetch-a-signing-key)


# Get a List of Signing Keys

Get a list of Signing Keys

```python
def get_a_list_of_signing_keys(self)
```

## Response Type

[`SigningKeysListResponse`](../../doc/models/signing-keys-list-response.md)

## Example Usage

```python
result = platformsecurityapi_controller.get_a_list_of_signing_keys()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Action Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 502 | Bad Gateway | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| Default | Unexpected Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch a Signing Key

Fetch a Signing Key

```python
def fetch_a_signing_key(self,
                       signingkey_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `signingkey_id` | `uuid\|str` | Template, Required | Signing Key ID |

## Response Type

[`SigningKeysResponse`](../../doc/models/signing-keys-response.md)

## Example Usage

```python
signingkey_id = '0000096e-0000-0000-0000-000000000000'

result = platformsecurityapi_controller.fetch_a_signing_key(signingkey_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Action Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 502 | Bad Gateway | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| Default | Unexpected Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

