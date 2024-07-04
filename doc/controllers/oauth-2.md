# Oauth 2

```python
oauth_2_controller = client.oauth_2
```

## Class Name

`Oauth2Controller`


# Request Access Token

Request Access Token

```python
def request_access_token(self)
```

## Response Type

[`Token`](../../doc/models/token.md)

## Example Usage

```python
result = oauth_2_controller.request_access_token()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | Authentication failed | `APIException` |

