
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `basic_credentials` | [`BasicCredentials`]($a/basic-authentication.md) | The credential object for Basic Authentication |
| `o_auth_2_credentials` | [`OAuth2Credentials`]($a/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

```python
client = Form3publicapiClient(
    basic_credentials=BasicCredentials(
        username='Username',
        password='Password'
    ),
    o_auth_2_credentials=OAuth2Credentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.PRODUCTION
)
```

## Form3 Public API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| audit | Gets AuditController |
| scheme_file_api | Gets SchemeFileAPIController |
| transaction_file_api | Gets TransactionFileAPIController |
| metrics_api | Gets MetricsAPIController |
| reports | Gets ReportsController |
| scheme_messages | Gets SchemeMessagesController |
| subscriptions | Gets SubscriptionsController |
| oauth_2 | Gets Oauth2Controller |
| accounts | Gets AccountsController |
| account_identification | Gets AccountIdentificationController |
| branches | Gets BranchesController |
| branch_identification | Gets BranchIdentificationController |
| name_verification_api | Gets NameVerificationAPIController |
| payments | Gets PaymentsController |
| organisations | Gets OrganisationsController |
| platformsecurityapi | Gets PlatformsecurityapiController |
| roles | Gets RolesController |
| ace | Gets ACEController |
| users | Gets UsersController |
| claims | Gets ClaimsController |
| direct_debits | Gets DirectDebitsController |
| mandates | Gets MandatesController |
| query_api | Gets QueryApiController |
| account_validation | Gets AccountValidationController |
| o_auth_authorization | Gets OAuthAuthorizationController |

