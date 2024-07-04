# Payments

```python
payments_controller = client.payments
```

## Class Name

`PaymentsController`

## Methods

* [List Positions](../../doc/controllers/payments.md#list-positions)
* [List Payments](../../doc/controllers/payments.md#list-payments)
* [Create Payment](../../doc/controllers/payments.md#create-payment)
* [Fetch Payment](../../doc/controllers/payments.md#fetch-payment)
* [Fetch Admission](../../doc/controllers/payments.md#fetch-admission)
* [List Tasks](../../doc/controllers/payments.md#list-tasks)
* [Get Payment Admission Task by ID](../../doc/controllers/payments.md#get-payment-admission-task-by-id)
* [Patch Payment Admission Task](../../doc/controllers/payments.md#patch-payment-admission-task)
* [Create Advice](../../doc/controllers/payments.md#create-advice)
* [Fetch Advice](../../doc/controllers/payments.md#fetch-advice)
* [Create Advice Submission](../../doc/controllers/payments.md#create-advice-submission)
* [Fetch Advice Submission](../../doc/controllers/payments.md#fetch-advice-submission)
* [Create Recall](../../doc/controllers/payments.md#create-recall)
* [Fetch Recall](../../doc/controllers/payments.md#fetch-recall)
* [Fetch Recall Admission](../../doc/controllers/payments.md#fetch-recall-admission)
* [Create Recall Decision](../../doc/controllers/payments.md#create-recall-decision)
* [Fetch Recall Decision](../../doc/controllers/payments.md#fetch-recall-decision)
* [Fetch Recall Decision Admission](../../doc/controllers/payments.md#fetch-recall-decision-admission)
* [Create Recall Decision Submission](../../doc/controllers/payments.md#create-recall-decision-submission)
* [Fetch Recall Decision Submission](../../doc/controllers/payments.md#fetch-recall-decision-submission)
* [Fetch Recall Reversal](../../doc/controllers/payments.md#fetch-recall-reversal)
* [Fetch Recall Reversal Admission](../../doc/controllers/payments.md#fetch-recall-reversal-admission)
* [Create Recall Submission](../../doc/controllers/payments.md#create-recall-submission)
* [Fetch Recall Submission](../../doc/controllers/payments.md#fetch-recall-submission)
* [Create Return](../../doc/controllers/payments.md#create-return)
* [Fetch Return](../../doc/controllers/payments.md#fetch-return)
* [Fetch Return Admission](../../doc/controllers/payments.md#fetch-return-admission)
* [Create Return Reversal](../../doc/controllers/payments.md#create-return-reversal)
* [Fetch Return Reversal](../../doc/controllers/payments.md#fetch-return-reversal)
* [Fetch Return Reversal Admission](../../doc/controllers/payments.md#fetch-return-reversal-admission)
* [Create Return Submission](../../doc/controllers/payments.md#create-return-submission)
* [Fetch Return Submission](../../doc/controllers/payments.md#fetch-return-submission)
* [Create Reversal](../../doc/controllers/payments.md#create-reversal)
* [Fetch Reversal](../../doc/controllers/payments.md#fetch-reversal)
* [Fetch Reversal Admission](../../doc/controllers/payments.md#fetch-reversal-admission)
* [Create Reversal Submission](../../doc/controllers/payments.md#create-reversal-submission)
* [Fetch Reversal Submission](../../doc/controllers/payments.md#fetch-reversal-submission)
* [Create Submission](../../doc/controllers/payments.md#create-submission)
* [Fetch Submission](../../doc/controllers/payments.md#fetch-submission)
* [Patch Payment Submission Task](../../doc/controllers/payments.md#patch-payment-submission-task)
* [Patch Return Submission Task](../../doc/controllers/payments.md#patch-return-submission-task)


# List Positions

List Positions

```python
def list_positions(self)
```

## Response Type

[`PositionDetailsListResponse`](../../doc/models/position-details-list-response.md)

## Example Usage

```python
result = payments_controller.list_positions()
print(result)
```


# List Payments

List payments

```python
def list_payments(self,
                 page_number=None,
                 page_size=None,
                 page_before=None,
                 page_after=None,
                 filter_organisation_id=None,
                 filter_debtor_party_account_number=None,
                 filter_debtor_party_account_name=None,
                 filter_debtor_party_bank_id=None,
                 filter_beneficiary_party_account_number=None,
                 filter_beneficiary_party_account_name=None,
                 filter_beneficiary_party_bank_id=None,
                 filter_currency=None,
                 filter_end_to_end_reference=None,
                 filter_return_unique_scheme_id=None,
                 filter_scheme_transaction_id=None,
                 filter_payment_scheme=None,
                 filter_payment_type=None,
                 filter_processing_date_from=None,
                 filter_processing_date_to=None,
                 filter_unique_scheme_id=None,
                 filter_amount=None,
                 filter_reference=None,
                 filter_route=None,
                 filter_submission_submission_date_from=None,
                 filter_submission_submission_date_to=None,
                 filter_submission_status=None,
                 filter_submission_scheme_status_code=None,
                 filter_return_submission_submission_date_from=None,
                 filter_return_submission_submission_date_to=None,
                 filter_return_submission_status=None,
                 filter_admission_admission_date_from=None,
                 filter_admission_admission_date_to=None,
                 filter_admission_status=None,
                 filter_admission_scheme_status_code=None,
                 filter_relationships=None,
                 filter_not_relationships=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `page_before` | `str` | Query, Optional | Cursor for previous page (this is a base64-encoded UUID continuation token returned from the application and should not be manually generated, unless requesting the last page, where the value should be set to "end"). |
| `page_after` | `str` | Query, Optional | Cursor for next page (this is a base64-encoded UUID continuation token returned from the application and should not be manually generated, unless requesting the first page, where the value should be set to "start"). |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_debtor_party_account_number` | `str` | Query, Optional | - |
| `filter_debtor_party_account_name` | `str` | Query, Optional | - |
| `filter_debtor_party_bank_id` | `str` | Query, Optional | - |
| `filter_beneficiary_party_account_number` | `str` | Query, Optional | - |
| `filter_beneficiary_party_account_name` | `str` | Query, Optional | - |
| `filter_beneficiary_party_bank_id` | `str` | Query, Optional | - |
| `filter_currency` | `str` | Query, Optional | - |
| `filter_end_to_end_reference` | `str` | Query, Optional | - |
| `filter_return_unique_scheme_id` | `str` | Query, Optional | - |
| `filter_scheme_transaction_id` | `str` | Query, Optional | - |
| `filter_payment_scheme` | `str` | Query, Optional | - |
| `filter_payment_type` | `str` | Query, Optional | - |
| `filter_processing_date_from` | `date` | Query, Optional | - |
| `filter_processing_date_to` | `date` | Query, Optional | - |
| `filter_unique_scheme_id` | `str` | Query, Optional | - |
| `filter_amount` | `str` | Query, Optional | - |
| `filter_reference` | `str` | Query, Optional | - |
| `filter_route` | `str` | Query, Optional | - |
| `filter_submission_submission_date_from` | `datetime` | Query, Optional | - |
| `filter_submission_submission_date_to` | `datetime` | Query, Optional | - |
| `filter_submission_status` | `str` | Query, Optional | Filter by submission status |
| `filter_submission_scheme_status_code` | `str` | Query, Optional | Filter by submission scheme status code |
| `filter_return_submission_submission_date_from` | `datetime` | Query, Optional | - |
| `filter_return_submission_submission_date_to` | `datetime` | Query, Optional | - |
| `filter_return_submission_status` | `str` | Query, Optional | Filter by return submission status |
| `filter_admission_admission_date_from` | `datetime` | Query, Optional | - |
| `filter_admission_admission_date_to` | `datetime` | Query, Optional | - |
| `filter_admission_status` | `str` | Query, Optional | Filter by admission status |
| `filter_admission_scheme_status_code` | `str` | Query, Optional | Filter by admission scheme status code |
| `filter_relationships` | [`List[FilterRelationships1Enum]`](../../doc/models/filter-relationships-1-enum.md) | Query, Optional | Filter for payments containing all of the requested relationships |
| `filter_not_relationships` | [`List[FilterNotRelationships1Enum]`](../../doc/models/filter-not-relationships-1-enum.md) | Query, Optional | Filter for payments containing none of the requested relationships |

## Response Type

[`PaymentDetailsListResponse`](../../doc/models/payment-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = payments_controller.list_payments(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Create Payment

Create payment

```python
def create_payment(self,
                  payment_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_creation_request` | [`PaymentCreation`](../../doc/models/payment-creation.md) | Body, Optional | - |

## Response Type

[`PaymentCreationResponse`](../../doc/models/payment-creation-response.md)

## Example Usage

```python
result = payments_controller.create_payment()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Payment creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Payment

Fetch payment

```python
def fetch_payment(self,
                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |

## Response Type

[`PaymentDetailsResponse`](../../doc/models/payment-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.fetch_payment(id)
print(result)
```


# Fetch Admission

Fetch admission

```python
def fetch_admission(self,
                   id,
                   admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`PaymentAdmissionDetailsResponse`](../../doc/models/payment-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.fetch_admission(
    id,
    admission_id
)
print(result)
```


# List Tasks

List tasks

```python
def list_tasks(self,
              id,
              admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`PaymentAdmissionTaskListResponse`](../../doc/models/payment-admission-task-list-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.list_tasks(
    id,
    admission_id
)
print(result)
```


# Get Payment Admission Task by ID

Get Payment Admission Task By ID

```python
def get_payment_admission_task_by_id(self,
                                    id,
                                    admission_id,
                                    task_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |
| `task_id` | `uuid\|str` | Template, Required | Payment Admission Task Id |

## Response Type

[`PaymentAdmissionTaskDetailsResponse`](../../doc/models/payment-admission-task-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

task_id = '0000075c-0000-0000-0000-000000000000'

result = payments_controller.get_payment_admission_task_by_id(
    id,
    admission_id,
    task_id
)
print(result)
```


# Patch Payment Admission Task

Patch Payment Admission Task

```python
def patch_payment_admission_task(self,
                                id,
                                admission_id,
                                task_id,
                                payment_admission_task_patch_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |
| `task_id` | `uuid\|str` | Template, Required | Payment Admission Task Id |
| `payment_admission_task_patch_request` | [`PaymentAdmissionTaskAmendment`](../../doc/models/payment-admission-task-amendment.md) | Body, Optional | - |

## Response Type

[`PaymentAdmissionTaskDetailsResponse`](../../doc/models/payment-admission-task-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

task_id = '0000075c-0000-0000-0000-000000000000'

result = payments_controller.patch_payment_admission_task(
    id,
    admission_id,
    task_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Advice

Create advice

```python
def create_advice(self,
                 id,
                 advice_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `advice_creation_request` | [`AdviceCreation`](../../doc/models/advice-creation.md) | Body, Optional | - |

## Response Type

[`AdviceCreationResponse`](../../doc/models/advice-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.create_advice(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Advice creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Advice

Fetch advice

```python
def fetch_advice(self,
                id,
                advice_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `advice_id` | `uuid\|str` | Template, Required | Advice Id |

## Response Type

[`AdviceDetailsResponse`](../../doc/models/advice-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

advice_id = '00002670-0000-0000-0000-000000000000'

result = payments_controller.fetch_advice(
    id,
    advice_id
)
print(result)
```


# Create Advice Submission

create advice submission

```python
def create_advice_submission(self,
                            id,
                            advice_id,
                            advice_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `advice_id` | `uuid\|str` | Template, Required | Advice Id |
| `advice_submission_creation_request` | [`AdviceSubmissionCreation`](../../doc/models/advice-submission-creation.md) | Body, Optional | - |

## Response Type

[`AdviceSubmissionCreationResponse`](../../doc/models/advice-submission-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

advice_id = '00002670-0000-0000-0000-000000000000'

result = payments_controller.create_advice_submission(
    id,
    advice_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Advice submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Advice Submission

Fetch advice submission

```python
def fetch_advice_submission(self,
                           id,
                           advice_id,
                           submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `advice_id` | `uuid\|str` | Template, Required | Advice Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |

## Response Type

[`AdviceSubmissionDetailsResponse`](../../doc/models/advice-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

advice_id = '00002670-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = payments_controller.fetch_advice_submission(
    id,
    advice_id,
    submission_id
)
print(result)
```


# Create Recall

Create recall

```python
def create_recall(self,
                 id,
                 recall_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_creation_request` | [`RecallCreation`](../../doc/models/recall-creation.md) | Body, Optional | - |

## Response Type

[`RecallCreationResponse`](../../doc/models/recall-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.create_recall(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Recall creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Recall

Fetch recall

```python
def fetch_recall(self,
                id,
                recall_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |

## Response Type

[`RecallDetailsResponse`](../../doc/models/recall-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall(
    id,
    recall_id
)
print(result)
```


# Fetch Recall Admission

Fetch recall admission

```python
def fetch_recall_admission(self,
                          id,
                          recall_id,
                          admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`RecallAdmissionDetailsResponse`](../../doc/models/recall-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall_admission(
    id,
    recall_id,
    admission_id
)
print(result)
```


# Create Recall Decision

Create recall decision

```python
def create_recall_decision(self,
                          id,
                          recall_id,
                          recall_decision_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `recall_decision_creation_request` | [`RecallDecisionCreation`](../../doc/models/recall-decision-creation.md) | Body, Optional | - |

## Response Type

[`RecallDecisionCreationResponse`](../../doc/models/recall-decision-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

result = payments_controller.create_recall_decision(
    id,
    recall_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Recall decision creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Recall Decision

Fetch recall decision

```python
def fetch_recall_decision(self,
                         id,
                         recall_id,
                         decision_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `decision_id` | `uuid\|str` | Template, Required | Decision Id |

## Response Type

[`RecallDecisionDetailsResponse`](../../doc/models/recall-decision-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

decision_id = '0000256a-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall_decision(
    id,
    recall_id,
    decision_id
)
print(result)
```


# Fetch Recall Decision Admission

Fetch recall decision admission

```python
def fetch_recall_decision_admission(self,
                                   id,
                                   recall_id,
                                   decision_id,
                                   admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `decision_id` | `uuid\|str` | Template, Required | Decision Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`RecallDecisionAdmissionDetailsResponse`](../../doc/models/recall-decision-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

decision_id = '0000256a-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall_decision_admission(
    id,
    recall_id,
    decision_id,
    admission_id
)
print(result)
```


# Create Recall Decision Submission

create recall decision submission

```python
def create_recall_decision_submission(self,
                                     id,
                                     recall_id,
                                     decision_id,
                                     recall_decision_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `decision_id` | `uuid\|str` | Template, Required | Decision Id |
| `recall_decision_submission_creation_request` | [`RecallDecisionSubmissionCreation`](../../doc/models/recall-decision-submission-creation.md) | Body, Optional | - |

## Response Type

[`RecallDecisionSubmissionCreationResponse`](../../doc/models/recall-decision-submission-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

decision_id = '0000256a-0000-0000-0000-000000000000'

result = payments_controller.create_recall_decision_submission(
    id,
    recall_id,
    decision_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Recall decision submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Recall Decision Submission

Fetch recall decision submission

```python
def fetch_recall_decision_submission(self,
                                    id,
                                    recall_id,
                                    decision_id,
                                    submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `decision_id` | `uuid\|str` | Template, Required | Decision Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |

## Response Type

[`RecallDecisionSubmissionDetailsResponse`](../../doc/models/recall-decision-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

decision_id = '0000256a-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall_decision_submission(
    id,
    recall_id,
    decision_id,
    submission_id
)
print(result)
```


# Fetch Recall Reversal

Fetch recall reversal

```python
def fetch_recall_reversal(self,
                         id,
                         recall_id,
                         reversal_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |

## Response Type

[`RecallReversalDetailsResponse`](../../doc/models/recall-reversal-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall_reversal(
    id,
    recall_id,
    reversal_id
)
print(result)
```


# Fetch Recall Reversal Admission

Fetch recall reversal admission

```python
def fetch_recall_reversal_admission(self,
                                   id,
                                   recall_id,
                                   reversal_id,
                                   admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`RecallReversalAdmissionDetailsResponse`](../../doc/models/recall-reversal-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall_reversal_admission(
    id,
    recall_id,
    reversal_id,
    admission_id
)
print(result)
```


# Create Recall Submission

create recall submission

```python
def create_recall_submission(self,
                            id,
                            recall_id,
                            recall_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `recall_submission_creation_request` | [`RecallSubmissionCreation`](../../doc/models/recall-submission-creation.md) | Body, Optional | - |

## Response Type

[`RecallSubmissionCreationResponse`](../../doc/models/recall-submission-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

result = payments_controller.create_recall_submission(
    id,
    recall_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Recall submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Recall Submission

Fetch recall submission

```python
def fetch_recall_submission(self,
                           id,
                           recall_id,
                           submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `recall_id` | `uuid\|str` | Template, Required | Recall Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |

## Response Type

[`RecallSubmissionDetailsResponse`](../../doc/models/recall-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

recall_id = '000009bc-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = payments_controller.fetch_recall_submission(
    id,
    recall_id,
    submission_id
)
print(result)
```


# Create Return

Create return

```python
def create_return(self,
                 id,
                 return_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_creation_request` | [`ReturnCreation`](../../doc/models/return-creation.md) | Body, Optional | - |

## Response Type

[`ReturnCreationResponse`](../../doc/models/return-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.create_return(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Return creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Return

Fetch return

```python
def fetch_return(self,
                id,
                return_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |

## Response Type

[`ReturnDetailsResponse`](../../doc/models/return-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

result = payments_controller.fetch_return(
    id,
    return_id
)
print(result)
```


# Fetch Return Admission

Fetch return admission

```python
def fetch_return_admission(self,
                          id,
                          return_id,
                          admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`ReturnAdmissionFetchResponse`](../../doc/models/return-admission-fetch-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.fetch_return_admission(
    id,
    return_id,
    admission_id
)
print(result)
```


# Create Return Reversal

Create return reversal

```python
def create_return_reversal(self,
                          id,
                          return_id,
                          return_reversal_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `return_reversal_creation_request` | [`ReturnReversalCreation`](../../doc/models/return-reversal-creation.md) | Body, Optional | - |

## Response Type

[`ReturnReversalCreationResponse`](../../doc/models/return-reversal-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

result = payments_controller.create_return_reversal(
    id,
    return_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Reversal creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Return Reversal

Fetch return reversal

```python
def fetch_return_reversal(self,
                         id,
                         return_id,
                         reversal_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |

## Response Type

[`ReturnReversalDetailsResponse`](../../doc/models/return-reversal-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

result = payments_controller.fetch_return_reversal(
    id,
    return_id,
    reversal_id
)
print(result)
```


# Fetch Return Reversal Admission

Fetch return reversal admission

```python
def fetch_return_reversal_admission(self,
                                   id,
                                   return_id,
                                   reversal_id,
                                   admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`ReturnReversalAdmissionDetailsResponse`](../../doc/models/return-reversal-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.fetch_return_reversal_admission(
    id,
    return_id,
    reversal_id,
    admission_id
)
print(result)
```


# Create Return Submission

create return submission

```python
def create_return_submission(self,
                            id,
                            return_id,
                            return_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `return_submission_creation_request` | [`ReturnSubmissionCreation`](../../doc/models/return-submission-creation.md) | Body, Optional | - |

## Response Type

[`ReturnSubmissionCreationResponse`](../../doc/models/return-submission-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

result = payments_controller.create_return_submission(
    id,
    return_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Return submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Return Submission

Fetch return submission

```python
def fetch_return_submission(self,
                           id,
                           return_id,
                           submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `return_id` | `uuid\|str` | Template, Required | Return Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |

## Response Type

[`ReturnSubmissionDetailsResponse`](../../doc/models/return-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = payments_controller.fetch_return_submission(
    id,
    return_id,
    submission_id
)
print(result)
```


# Create Reversal

Create reversal

```python
def create_reversal(self,
                   id,
                   reversal_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `reversal_creation_request` | [`ReversalCreation`](../../doc/models/reversal-creation.md) | Body, Optional | - |

## Response Type

[`ReversalCreationResponse`](../../doc/models/reversal-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.create_reversal(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Reversal creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Reversal

Fetch reversal

```python
def fetch_reversal(self,
                  id,
                  reversal_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |

## Response Type

[`ReversalDetailsResponse`](../../doc/models/reversal-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

result = payments_controller.fetch_reversal(
    id,
    reversal_id
)
print(result)
```


# Fetch Reversal Admission

Fetch reversal admission

```python
def fetch_reversal_admission(self,
                            id,
                            reversal_id,
                            admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |
| `admission_id` | `uuid\|str` | Template, Required | Admission Id |

## Response Type

[`ReversalAdmissionDetailsResponse`](../../doc/models/reversal-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = payments_controller.fetch_reversal_admission(
    id,
    reversal_id,
    admission_id
)
print(result)
```


# Create Reversal Submission

Create reversal submission

```python
def create_reversal_submission(self,
                              id,
                              reversal_id,
                              reversal_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |
| `reversal_submission_creation_request` | [`ReversalSubmissionCreation`](../../doc/models/reversal-submission-creation.md) | Body, Optional | - |

## Response Type

[`ReversalSubmissionCreationResponse`](../../doc/models/reversal-submission-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

result = payments_controller.create_reversal_submission(
    id,
    reversal_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Reversal submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Reversal Submission

Fetch reversal submission

```python
def fetch_reversal_submission(self,
                             id,
                             reversal_id,
                             submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `reversal_id` | `uuid\|str` | Template, Required | Reversal Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |

## Response Type

[`ReversalSubmissionDetailsResponse`](../../doc/models/reversal-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

reversal_id = '0000181a-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = payments_controller.fetch_reversal_submission(
    id,
    reversal_id,
    submission_id
)
print(result)
```


# Create Submission

create submission

```python
def create_submission(self,
                     id,
                     submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `submission_creation_request` | [`PaymentSubmissionCreation`](../../doc/models/payment-submission-creation.md) | Body, Optional | - |

## Response Type

[`PaymentSubmissionCreationResponse`](../../doc/models/payment-submission-creation-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.create_submission(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Submission creation error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Fetch Submission

Fetch submission

```python
def fetch_submission(self,
                    id,
                    submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |

## Response Type

[`PaymentSubmissionDetailsResponse`](../../doc/models/payment-submission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

result = payments_controller.fetch_submission(
    id,
    submission_id
)
print(result)
```


# Patch Payment Submission Task

Patch Payment Submission Task

```python
def patch_payment_submission_task(self,
                                 id,
                                 submission_id,
                                 task_id,
                                 payment_submission_task_patch_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Payment Id |
| `submission_id` | `uuid\|str` | Template, Required | Submission Id |
| `task_id` | `uuid\|str` | Template, Required | Payment Submission Task Id |
| `payment_submission_task_patch_request` | [`PaymentSubmissionTaskAmendment`](../../doc/models/payment-submission-task-amendment.md) | Body, Optional | - |

## Response Type

[`PaymentSubmissionTaskDetailsResponse`](../../doc/models/payment-submission-task-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

submission_id = '0000202c-0000-0000-0000-000000000000'

task_id = '0000075c-0000-0000-0000-000000000000'

result = payments_controller.patch_payment_submission_task(
    id,
    submission_id,
    task_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Patch Return Submission Task

Patch Return Submission Task

```python
def patch_return_submission_task(self,
                                payment_id,
                                return_id,
                                return_submission_id,
                                task_id,
                                return_submission_task_patch_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `uuid\|str` | Template, Required | Payment ID |
| `return_id` | `uuid\|str` | Template, Required | Return ID |
| `return_submission_id` | `uuid\|str` | Template, Required | Return Submission ID |
| `task_id` | `uuid\|str` | Template, Required | Return Submission Task Id |
| `return_submission_task_patch_request` | [`ReturnSubmissionTaskAmendment`](../../doc/models/return-submission-task-amendment.md) | Body, Optional | - |

## Response Type

[`ReturnSubmissionTaskDetailsResponse`](../../doc/models/return-submission-task-details-response.md)

## Example Usage

```python
payment_id = '000003ea-0000-0000-0000-000000000000'

return_id = '00001dea-0000-0000-0000-000000000000'

return_submission_id = '00001b42-0000-0000-0000-000000000000'

task_id = '0000075c-0000-0000-0000-000000000000'

result = payments_controller.patch_return_submission_task(
    payment_id,
    return_id,
    return_submission_id,
    task_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

