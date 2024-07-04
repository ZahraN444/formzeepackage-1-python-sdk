
# Basic Authentication



Documentation for accessing and setting credentials for Basic.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| Username | `str` | The username to use with basic authentication | `username` |
| Password | `str` | The password to use with basic authentication | `password` |



**Note:** Auth credentials can be set using `BasicCredentials` object, passed in as named parameter `basic_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
client = Form3publicapiClient(
    basic_credentials=BasicCredentials(
        username='Username',
        password='Password'
    )
)
```


