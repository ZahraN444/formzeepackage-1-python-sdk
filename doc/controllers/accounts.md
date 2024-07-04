# Accounts

```python
accounts_controller = client.accounts
```

## Class Name

`AccountsController`

## Methods

* [List Accounts](../../doc/controllers/accounts.md#list-accounts)
* [Create Account](../../doc/controllers/accounts.md#create-account)
* [Delete Account](../../doc/controllers/accounts.md#delete-account)
* [Fetch Account](../../doc/controllers/accounts.md#fetch-account)
* [Amend Account](../../doc/controllers/accounts.md#amend-account)
* [Fetch Account Events](../../doc/controllers/accounts.md#fetch-account-events)


# List Accounts

List accounts

```python
def list_accounts(self,
                 page_number=None,
                 page_before=None,
                 page_after=None,
                 page_size=None,
                 filter_organisation_id=None,
                 filter_bank_id_code=None,
                 filter_bank_id=None,
                 filter_account_number=None,
                 filter_country=None,
                 filter_customer_id=None,
                 filter_iban=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_before` | `str` | Query, Optional | Cursor value for getting previous page |
| `page_after` | `str` | Query, Optional | Cursor value for getting next page |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_bank_id_code` | `List[str]` | Query, Optional | Filter by type of bank id e.g. "GBDSC" |
| `filter_bank_id` | `List[str]` | Query, Optional | Filter by bank id e.g. sort code or bic |
| `filter_account_number` | `List[str]` | Query, Optional | Filter by account number |
| `filter_country` | `List[str]` | Query, Optional | Filter by country e.g. FR,GB |
| `filter_customer_id` | `List[str]` | Query, Optional | Filter by customer_id |
| `filter_iban` | `List[str]` | Query, Optional | Filter by IBAN |

## Response Type

[`AccountDetailsListResponse`](../../doc/models/account-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = accounts_controller.list_accounts(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Create Account

Create account

```python
def create_account(self,
                  account_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_creation_request` | [`AccountCreation`](../../doc/models/account-creation.md) | Body, Optional | - |

## Response Type

[`AccountCreationResponse`](../../doc/models/account-creation-response.md)

## Example Usage

```python
account_creation_request = AccountCreation(
    data=Account(
        attributes=AccountAttributes(
            country='GB',
            account_classification=AccountClassification1Enum.PERSONAL,
            account_matching_opt_out=False,
            account_number='41426819',
            bank_id='400300',
            bank_id_code='GBDSC',
            base_currency='GBP',
            bic='NWBKGB22',
            customer_id='12345',
            iban='GB11NWBK40030041426819',
            joint_account=False,
            name_matching_status=NameMatchingStatusEnum.SUPPORTED,
            reference_mask='4929############',
            status_reason=StatusReasonEnum.TRANSFERRED,
            switched=False,
            title='Ms'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='accounts',
        version=0
    )
)

result = accounts_controller.create_account(
    account_creation_request=account_creation_request
)
print(result)
```


# Delete Account

Delete account

```python
def delete_account(self,
                  id,
                  version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Account Id |
| `version` | `int` | Query, Required | Version |

## Response Type

`void`

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

version = 172

result = accounts_controller.delete_account(
    id,
    version
)
print(result)
```


# Fetch Account

Fetch account

```python
def fetch_account(self,
                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Account Id |

## Response Type

[`AccountDetailsResponse`](../../doc/models/account-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = accounts_controller.fetch_account(id)
print(result)
```


# Amend Account

Amend account

```python
def amend_account(self,
                 id,
                 account_amend_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Account Id |
| `account_amend_request` | [`AccountAmendment`](../../doc/models/account-amendment.md) | Body, Optional | - |

## Response Type

[`AccountDetailsResponse`](../../doc/models/account-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = accounts_controller.amend_account(id)
print(result)
```


# Fetch Account Events

Fetch account events

```python
def fetch_account_events(self,
                        id,
                        page_number=None,
                        page_size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Account Id |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |

## Response Type

[`AccountEventListResponse`](../../doc/models/account-event-list-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = accounts_controller.fetch_account_events(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')id)
print(result)
```

