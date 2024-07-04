# Claims

```python
claims_controller = client.claims
```

## Class Name

`ClaimsController`

## Methods

* [List Claims](../../doc/controllers/claims.md#list-claims)
* [Create Claim](../../doc/controllers/claims.md#create-claim)
* [Fetch Claim](../../doc/controllers/claims.md#fetch-claim)
* [Create Claim Reversal](../../doc/controllers/claims.md#create-claim-reversal)
* [Fetch Claim Reversal](../../doc/controllers/claims.md#fetch-claim-reversal)
* [Create Claim Reversal Submission](../../doc/controllers/claims.md#create-claim-reversal-submission)
* [Fetch Claim Reversal Submission](../../doc/controllers/claims.md#fetch-claim-reversal-submission)
* [Create Claim Submission](../../doc/controllers/claims.md#create-claim-submission)
* [Fetch Claim Submission](../../doc/controllers/claims.md#fetch-claim-submission)


# List Claims

List claims

```python
def list_claims(self,
               page_number=None,
               page_size=None,
               filter_organisation_id=None,
               filter_payment_scheme=None,
               filter_clearing_id=None,
               filter_reference=None,
               filter_reason_code=None,
               filter_contact_name=None,
               filter_debtor_party_account_number=None,
               filter_debtor_party_bank_id=None,
               filter_beneficiary_party_account_number=None,
               filter_beneficiary_party_bank_id=None,
               filter_original_instruction_reference=None,
               filter_submission_status=None,
               filter_submission_submission_date_from=None,
               filter_submission_submission_date_to=None,
               filter_reversal_status=None,
               filter_reversal_submission_date_from=None,
               filter_reversal_submission_date_to=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_payment_scheme` | `str` | Query, Optional | - |
| `filter_clearing_id` | `str` | Query, Optional | - |
| `filter_reference` | `str` | Query, Optional | - |
| `filter_reason_code` | `str` | Query, Optional | - |
| `filter_contact_name` | `str` | Query, Optional | - |
| `filter_debtor_party_account_number` | `str` | Query, Optional | - |
| `filter_debtor_party_bank_id` | `str` | Query, Optional | - |
| `filter_beneficiary_party_account_number` | `str` | Query, Optional | - |
| `filter_beneficiary_party_bank_id` | `str` | Query, Optional | - |
| `filter_original_instruction_reference` | `str` | Query, Optional | - |
| `filter_submission_status` | `str` | Query, Optional | - |
| `filter_submission_submission_date_from` | `datetime` | Query, Optional | - |
| `filter_submission_submission_date_to` | `datetime` | Query, Optional | - |
| `filter_reversal_status` | `str` | Query, Optional | - |
| `filter_reversal_submission_date_from` | `datetime` | Query, Optional | - |
| `filter_reversal_submission_date_to` | `datetime` | Query, Optional | - |

## Response Type

[`ClaimDetailsListResponse`](../../doc/models/claim-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = claims_controller.list_claims(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Create Claim

Create Claim

```python
def create_claim(self,
                claim_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `claim_creation_request` | [`ClaimCreation`](../../doc/models/claim-creation.md) | Body, Optional | - |

## Response Type

[`ClaimDetailsResponse`](../../doc/models/claim-details-response.md)

## Example Usage

```python
result = claims_controller.create_claim()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Claim creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Claim

Fetch claim

```python
def fetch_claim(self,
               id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Claim Id |

## Response Type

[`ClaimDetailsResponse`](../../doc/models/claim-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = claims_controller.fetch_claim(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Claim Reversal

Create Claim Reversal

```python
def create_claim_reversal(self,
                         id,
                         claim_reversal_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Claim Id |
| `claim_reversal_creation_request` | [`ClaimReversalCreation`](../../doc/models/claim-reversal-creation.md) | Body, Optional | - |

## Response Type

[`ClaimReversalDetailsResponse`](../../doc/models/claim-reversal-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = claims_controller.create_claim_reversal(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Claim Reversal creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Claim Reversal

Fetch Claim Reversal

```python
def fetch_claim_reversal(self,
                        id,
                        reversal_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Claim Id |
| `reversal_id` | `uuid\|str` | Template, Required | Claim Reversal Id |

## Response Type

[`ClaimReversalDetailsResponse`](../../doc/models/claim-reversal-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

result = claims_controller.fetch_claim_reversal(
    id,
    reversal_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Claim Reversal Submission

Create Claim Reversal Submission

```python
def create_claim_reversal_submission(self,
                                    id,
                                    reversal_id,
                                    claim_reversal_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Claim Id |
| `reversal_id` | `uuid\|str` | Template, Required | Claim Reversal Id |
| `claim_reversal_submission_creation_request` | [`ClaimReversalSubmissionCreation`](../../doc/models/claim-reversal-submission-creation.md) | Body, Optional | - |

## Response Type

[`ClaimReversalSubmissionDetailsResponse`](../../doc/models/claim-reversal-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

result = claims_controller.create_claim_reversal_submission(
    id,
    reversal_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Claim Reversal creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Claim Reversal Submission

Fetch Claim Reversal Submission

```python
def fetch_claim_reversal_submission(self,
                                   id,
                                   reversal_id,
                                   submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Claim Id |
| `reversal_id` | `uuid\|str` | Template, Required | Claim Reversal Id |
| `submission_id` | `uuid\|str` | Template, Required | Claim Reversal Submission Id |

## Response Type

[`ClaimReversalSubmissionDetailsResponse`](../../doc/models/claim-reversal-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = claims_controller.fetch_claim_reversal_submission(
    id,
    reversal_id,
    submission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Claim Submission

Create Claim Submission

```python
def create_claim_submission(self,
                           id,
                           claim_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Claim Id |
| `claim_submission_creation_request` | [`ClaimSubmissionCreation`](../../doc/models/claim-submission-creation.md) | Body, Optional | - |

## Response Type

[`ClaimSubmissionDetailsResponse`](../../doc/models/claim-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = claims_controller.create_claim_submission(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Claim Submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Claim Submission

Fetch Claim Submission

```python
def fetch_claim_submission(self,
                          id,
                          submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Claim Id |
| `submission_id` | `uuid\|str` | Template, Required | Claim Submission Id |

## Response Type

[`ClaimSubmissionDetailsResponse`](../../doc/models/claim-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = claims_controller.fetch_claim_submission(
    id,
    submission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

