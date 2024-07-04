# Name Verification API

```python
name_verification_api_controller = client.name_verification_api
```

## Class Name

`NameVerificationAPIController`

## Methods

* [List Name Verifications](../../doc/controllers/name-verification-api.md#list-name-verifications)
* [Name Verification Creation Request](../../doc/controllers/name-verification-api.md#name-verification-creation-request)
* [Fetch Name Verification Resource](../../doc/controllers/name-verification-api.md#fetch-name-verification-resource)
* [Name Verification Admission Fetch Request](../../doc/controllers/name-verification-api.md#name-verification-admission-fetch-request)


# List Name Verifications

List name verifications

```python
def list_name_verifications(self,
                           page_number=None,
                           page_size=None,
                           filter_organisation_id=None,
                           filter_account_classification=None,
                           filter_account_number=None,
                           filter_bank_id=None,
                           filter_bank_id_code=None,
                           filter_name=None,
                           filter_secondary_identification=None,
                           filter_created_date_from=None,
                           filter_created_date_to=None,
                           filter_modified_date_from=None,
                           filter_modified_date_to=None,
                           filter_admission_created_date_from=None,
                           filter_admission_created_date_to=None,
                           filter_admission_modified_date_from=None,
                           filter_admission_modified_date_to=None,
                           filter_admission_status=None,
                           filter_admission_answer=None,
                           filter_admission_actual_name=None,
                           filter_admission_reason=None,
                           filter_admission_reason_code=None,
                           filter_submission_created_date_from=None,
                           filter_submission_created_date_to=None,
                           filter_submission_modified_date_from=None,
                           filter_submission_modified_date_to=None,
                           filter_submission_status=None,
                           filter_submission_answer=None,
                           filter_submission_actual_name=None,
                           filter_submission_reason=None,
                           filter_submission_reason_code=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `int` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `uuid\|str` | Query, Optional | Filter by organisation id |
| `filter_account_classification` | `str` | Query, Optional | Filter by account classification |
| `filter_account_number` | `str` | Query, Optional | Filter by account number |
| `filter_bank_id` | `str` | Query, Optional | Filter by bank id |
| `filter_bank_id_code` | `str` | Query, Optional | Filter by bank id code |
| `filter_name` | `List[str]` | Query, Optional | Filter by name |
| `filter_secondary_identification` | `str` | Query, Optional | Filter by secondary identification |
| `filter_created_date_from` | `datetime` | Query, Optional | Filter by created date from |
| `filter_created_date_to` | `datetime` | Query, Optional | Filter by created date to |
| `filter_modified_date_from` | `datetime` | Query, Optional | Filter by modified date from |
| `filter_modified_date_to` | `datetime` | Query, Optional | Filter by modified date to |
| `filter_admission_created_date_from` | `datetime` | Query, Optional | Filter by admission created date from |
| `filter_admission_created_date_to` | `datetime` | Query, Optional | Filter by admission created date to |
| `filter_admission_modified_date_from` | `datetime` | Query, Optional | Filter by admission modified date from |
| `filter_admission_modified_date_to` | `datetime` | Query, Optional | Filter by admission modified date to |
| `filter_admission_status` | `str` | Query, Optional | Filter by admission status |
| `filter_admission_answer` | `str` | Query, Optional | Filter by admission answer |
| `filter_admission_actual_name` | `str` | Query, Optional | Filter by admission actual name |
| `filter_admission_reason` | `str` | Query, Optional | Filter by admission reason |
| `filter_admission_reason_code` | `str` | Query, Optional | Filter by admission reason code |
| `filter_submission_created_date_from` | `datetime` | Query, Optional | Filter by submission created date from |
| `filter_submission_created_date_to` | `datetime` | Query, Optional | Filter by submission created date to |
| `filter_submission_modified_date_from` | `datetime` | Query, Optional | Filter by submission modified date from |
| `filter_submission_modified_date_to` | `datetime` | Query, Optional | Filter by submission modified date to |
| `filter_submission_status` | `str` | Query, Optional | Filter by submission status |
| `filter_submission_answer` | `str` | Query, Optional | Filter by submission answer |
| `filter_submission_actual_name` | `str` | Query, Optional | Filter by submission actual name |
| `filter_submission_reason` | `str` | Query, Optional | Filter by submission reason |
| `filter_submission_reason_code` | `str` | Query, Optional | Filter by submission reason code |

## Response Type

[`NameVerificationDetailsListResponse`](../../doc/models/name-verification-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = name_verification_api_controller.list_name_verifications(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Name Verification Creation Request

Name verification creation request

```python
def name_verification_creation_request(self,
                                      name_verification_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name_verification_creation_request` | [`NameVerificationCreation`](../../doc/models/name-verification-creation.md) | Body, Optional | - |

## Response Type

[`NameVerificationCreationResponse`](../../doc/models/name-verification-creation-response.md)

## Example Usage

```python
name_verification_creation_request = NameVerificationCreation(
    data=NameVerification(
        attributes=NameVerificationAttributes(
            account_classification=AccountClassificationEnum.PERSONAL,
            account_number='account_number4',
            account_number_code=AccountNumberCodeEnum.IBAN,
            bank_id='bank_id6',
            bank_id_code='GBDSC',
            name=[
                'name4',
                'name5',
                'name6'
            ]
        ),
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='00000b24-0000-0000-0000-000000000000'
    )
)

result = name_verification_api_controller.name_verification_creation_request(
    name_verification_creation_request=name_verification_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Name Verification Resource

Fetch name verification resource

```python
def fetch_name_verification_resource(self,
                                    id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Name Verification ID |

## Response Type

[`NameVerificationDetailsResponse`](../../doc/models/name-verification-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = name_verification_api_controller.fetch_name_verification_resource(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Name Verification Admission Fetch Request

Name verification admission fetch request

```python
def name_verification_admission_fetch_request(self,
                                             name_verification_id,
                                             id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name_verification_id` | `uuid\|str` | Template, Required | - |
| `id` | `uuid\|str` | Template, Required | - |

## Response Type

[`NameVerificationAdmissionDetailsResponse`](../../doc/models/name-verification-admission-details-response.md)

## Example Usage

```python
name_verification_id = '00001302-0000-0000-0000-000000000000'

id = '00001770-0000-0000-0000-000000000000'

result = name_verification_api_controller.name_verification_admission_fetch_request(
    name_verification_id,
    id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

