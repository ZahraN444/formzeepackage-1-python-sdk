# O Auth Authorization

```python
o_auth_authorization_controller = client.o_auth_authorization
```

## Class Name

`OAuthAuthorizationController`


# Request Token O Auth 2

Create a new OAuth 2 token.

:information_source: **Note** This endpoint does not require authentication.

```python
def request_token_o_auth_2(self,
                          authorization,
                          scope=None,
                          _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Authorization header in Basic auth format |
| `scope` | `str` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

[`OAuthToken`](../../doc/models/o-auth-token.md)

## Example Usage

```python
authorization = 'Authorization8'

_optional_form_parameters = {
    'key0': 'additionalFieldParams9'
}

result = o_auth_authorization_controller.request_token_o_auth_2(
    authorization,
    _optional_form_parameters=_optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OAuthProviderException`](../../doc/models/o-auth-provider-exception.md) |

