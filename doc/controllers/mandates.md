# Mandates

```python
mandates_controller = client.mandates
```

## Class Name

`MandatesController`

## Methods

* [Get Mandates](../../doc/controllers/mandates.md#get-mandates)
* [Post Mandates](../../doc/controllers/mandates.md#post-mandates)
* [Get Mandates ID](../../doc/controllers/mandates.md#get-mandates-id)
* [Patch Mandates ID](../../doc/controllers/mandates.md#patch-mandates-id)
* [Get Mandates ID Admissions Admission ID](../../doc/controllers/mandates.md#get-mandates-id-admissions-admission-id)
* [Post Mandates ID Returns](../../doc/controllers/mandates.md#post-mandates-id-returns)
* [Get Mandates ID Returns Return ID](../../doc/controllers/mandates.md#get-mandates-id-returns-return-id)
* [Post Mandates ID Returns Return ID Submissions](../../doc/controllers/mandates.md#post-mandates-id-returns-return-id-submissions)
* [Get Mandates ID Returns Return ID Submissions Submission ID](../../doc/controllers/mandates.md#get-mandates-id-returns-return-id-submissions-submission-id)
* [Post Mandates ID Submissions](../../doc/controllers/mandates.md#post-mandates-id-submissions)
* [Get Mandates ID Submissions Submission ID](../../doc/controllers/mandates.md#get-mandates-id-submissions-submission-id)


# Get Mandates

List mandates

```python
def get_mandates(self,
                page_number=None,
                page_size=None,
                filter_organisation_id=None,
                filter_debtor_party_account_number=None,
                filter_debtor_party_bank_id=None,
                filter_beneficiary_party_account_number=None,
                filter_beneficiary_party_bank_id=None,
                filter_currency=None,
                filter_payment_scheme=None,
                filter_scheme_payment_type=None,
                filter_processing_date_from=None,
                filter_processing_date_to=None,
                filter_scheme_processing_date_from=None,
                filter_scheme_processing_date_to=None,
                filter_clearing_id=None,
                filter_admission_admission_date_from=None,
                filter_admission_admission_date_to=None,
                filter_admission_status=None,
                filter_admission_scheme_status_code=None,
                filter_amount=None,
                filter_reference=None,
                filter_unique_scheme_id=None,
                filter_all_versions=None,
                filter_submission_submission_date_from=None,
                filter_submission_submission_date_to=None,
                filter_status=None,
                filter_status_reason=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_debtor_party_account_number` | `str` | Query, Optional | - |
| `filter_debtor_party_bank_id` | `str` | Query, Optional | - |
| `filter_beneficiary_party_account_number` | `str` | Query, Optional | - |
| `filter_beneficiary_party_bank_id` | `str` | Query, Optional | - |
| `filter_currency` | `str` | Query, Optional | - |
| `filter_payment_scheme` | `str` | Query, Optional | - |
| `filter_scheme_payment_type` | `str` | Query, Optional | - |
| `filter_processing_date_from` | `date` | Query, Optional | - |
| `filter_processing_date_to` | `date` | Query, Optional | - |
| `filter_scheme_processing_date_from` | `date` | Query, Optional | - |
| `filter_scheme_processing_date_to` | `date` | Query, Optional | - |
| `filter_clearing_id` | `str` | Query, Optional | - |
| `filter_admission_admission_date_from` | `datetime` | Query, Optional | - |
| `filter_admission_admission_date_to` | `datetime` | Query, Optional | - |
| `filter_admission_status` | `str` | Query, Optional | Filter by admission status |
| `filter_admission_scheme_status_code` | `str` | Query, Optional | Filter by admission scheme status code |
| `filter_amount` | `str` | Query, Optional | Filter by amount |
| `filter_reference` | `str` | Query, Optional | Filter by reference |
| `filter_unique_scheme_id` | `str` | Query, Optional | Filter by unique scheme id |
| `filter_all_versions` | `bool` | Query, Optional | Include old versions of mandates |
| `filter_submission_submission_date_from` | `datetime` | Query, Optional | - |
| `filter_submission_submission_date_to` | `datetime` | Query, Optional | - |
| `filter_status` | `str` | Query, Optional | Filter by mandate status |
| `filter_status_reason` | `str` | Query, Optional | Filter by mandate status reason |

## Response Type

[`MandateDetailsListResponse`](../../doc/models/mandate-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = mandates_controller.get_mandates(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Post Mandates

Create Mandate

```python
def post_mandates(self,
                 mandate_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandate_creation_request` | [`MandateCreation`](../../doc/models/mandate-creation.md) | Body, Optional | - |

## Response Type

[`MandateCreationResponse`](../../doc/models/mandate-creation-response.md)

## Example Usage

```python
result = mandates_controller.post_mandates()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Mandate creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Mandate creation conflict Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Mandates ID

Fetch mandate

```python
def get_mandates_id(self,
                   id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |

## Response Type

[`MandateDetailsResponse`](../../doc/models/mandate-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = mandates_controller.get_mandates_id(id)
print(result)
```


# Patch Mandates ID

Update mandate

```python
def patch_mandates_id(self,
                     id,
                     mandate_amendment=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `mandate_amendment` | [`MandateAmendment`](../../doc/models/mandate-amendment.md) | Body, Optional | - |

## Response Type

[`MandateDetailsResponse`](../../doc/models/mandate-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = mandates_controller.patch_mandates_id(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Mandate update error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Mandates ID Admissions Admission ID

Fetch Mandate Admission

```python
def get_mandates_id_admissions_admission_id(self,
                                           id,
                                           admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `admission_id` | `uuid\|str` | Template, Required | Mandate Admission Id |

## Response Type

[`MandateAdmissionDetailsResponse`](../../doc/models/mandate-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = mandates_controller.get_mandates_id_admissions_admission_id(
    id,
    admission_id
)
print(result)
```


# Post Mandates ID Returns

Create mandate return

```python
def post_mandates_id_returns(self,
                            id,
                            return_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `return_creation_request` | [`MandateReturnCreation`](../../doc/models/mandate-return-creation.md) | Body, Optional | - |

## Response Type

[`MandateReturnCreationResponse`](../../doc/models/mandate-return-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = mandates_controller.post_mandates_id_returns(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Return creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Mandates ID Returns Return ID

Fetch mandate return

```python
def get_mandates_id_returns_return_id(self,
                                     id,
                                     return_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |

## Response Type

[`MandateReturnDetailsResponse`](../../doc/models/mandate-return-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

result = mandates_controller.get_mandates_id_returns_return_id(
    id,
    return_id
)
print(result)
```


# Post Mandates ID Returns Return ID Submissions

Create mandate return submission

```python
def post_mandates_id_returns_return_id_submissions(self,
                                                  id,
                                                  return_id,
                                                  return_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `return_submission_creation_request` | [`MandateReturnSubmissionCreation`](../../doc/models/mandate-return-submission-creation.md) | Body, Optional | - |

## Response Type

[`MandateReturnSubmissionCreationResponse`](../../doc/models/mandate-return-submission-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

result = mandates_controller.post_mandates_id_returns_return_id_submissions(
    id,
    return_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Return submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Mandates ID Returns Return ID Submissions Submission ID

Fetch return submission

```python
def get_mandates_id_returns_return_id_submissions_submission_id(self,
                                                               id,
                                                               return_id,
                                                               submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |

## Response Type

[`MandateReturnSubmissionDetailsResponse`](../../doc/models/mandate-return-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = mandates_controller.get_mandates_id_returns_return_id_submissions_submission_id(
    id,
    return_id,
    submission_id
)
print(result)
```


# Post Mandates ID Submissions

Create Mandate Submission

```python
def post_mandates_id_submissions(self,
                                id,
                                mandate_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `mandate_submission_creation_request` | [`MandateSubmissionCreation`](../../doc/models/mandate-submission-creation.md) | Body, Optional | - |

## Response Type

[`MandateSubmissionDetailsResponse`](../../doc/models/mandate-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = mandates_controller.post_mandates_id_submissions(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Mandate Submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Mandates ID Submissions Submission ID

Fetch Mandate Submission

```python
def get_mandates_id_submissions_submission_id(self,
                                             id,
                                             submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Mandate Id |
| `submission_id` | `uuid\|str` | Template, Required | Mandate Submission Id |

## Response Type

[`MandateSubmissionDetailsResponse`](../../doc/models/mandate-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = mandates_controller.get_mandates_id_submissions_submission_id(
    id,
    submission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

