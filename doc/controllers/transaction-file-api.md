# Transaction File API

```python
transaction_file_api_controller = client.transaction_file_api
```

## Class Name

`TransactionFileAPIController`

## Methods

* [List Transaction Files](../../doc/controllers/transaction-file-api.md#list-transaction-files)
* [Create Transaction File](../../doc/controllers/transaction-file-api.md#create-transaction-file)
* [Get Transaction File](../../doc/controllers/transaction-file-api.md#get-transaction-file)
* [Upload Transaction File](../../doc/controllers/transaction-file-api.md#upload-transaction-file)
* [Create Transaction File Admission](../../doc/controllers/transaction-file-api.md#create-transaction-file-admission)
* [Get Transaction File Admission](../../doc/controllers/transaction-file-api.md#get-transaction-file-admission)
* [Create Transaction File Submission](../../doc/controllers/transaction-file-api.md#create-transaction-file-submission)
* [Get Transaction File Submission](../../doc/controllers/transaction-file-api.md#get-transaction-file-submission)


# List Transaction Files

List transaction files

```python
def list_transaction_files(self,
                          page_number=None,
                          page_size=100,
                          filter_organisation_id=None,
                          filter_payment_scheme=None,
                          filter_file_format=None,
                          filter_created_on_from=None,
                          filter_created_on_to=None,
                          filter_submission_status=None,
                          filter_submission_submission_date_from=None,
                          filter_submission_submission_date_to=None,
                          filter_submission_scheme_references_file_identifier=None,
                          filter_submission_scheme_references_file_number=None,
                          filter_submission_scheme_references_clearing_id=None,
                          filter_admission_status=None,
                          filter_admission_admission_date_from=None,
                          filter_admission_admission_date_to=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Find all File resources with a given organisation ID |
| `filter_payment_scheme` | `str` | Query, Optional | Find File resources by a certain scheme |
| `filter_file_format` | `str` | Query, Optional | Find File resources by the format of the file |
| `filter_created_on_from` | `date` | Query, Optional | Find all File resources created from this date, in format YYYY-MM-DD |
| `filter_created_on_to` | `date` | Query, Optional | Find all File resources created up to this date, in format YYYY-MM-DD |
| `filter_submission_status` | `str` | Query, Optional | Find all File resources with a certain submission status |
| `filter_submission_submission_date_from` | `datetime` | Query, Optional | Find all File resources submitted from and including this date/time |
| `filter_submission_submission_date_to` | `datetime` | Query, Optional | Find all File resources submitted up to and included this date/time |
| `filter_submission_scheme_references_file_identifier` | `str` | Query, Optional | Find File resources the id of the submission to to the scheme |
| `filter_submission_scheme_references_file_number` | `str` | Query, Optional | Find File resources by the id of the file sent to the scheme |
| `filter_submission_scheme_references_clearing_id` | `str` | Query, Optional | Find File resources by the Service User Number (SUN) of the payment originator |
| `filter_admission_status` | `str` | Query, Optional | Find all File resources with a certain admission status |
| `filter_admission_admission_date_from` | `datetime` | Query, Optional | Find all File resources admitted from and including this date/time |
| `filter_admission_admission_date_to` | `datetime` | Query, Optional | Find all File resources admitted up to and included this date/time |

## Response Type

[`ListTransactionFilesResponse`](../../doc/models/list-transaction-files-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = transaction_file_api_controller.list_transaction_files(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Reports bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Transaction File

Creates a Transaction File

```python
def create_transaction_file(self,
                           transaction_file_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_file_creation_request` | [`TransactionFileCreation`](../../doc/models/transaction-file-creation.md) | Body, Optional | - |

## Response Type

[`TransactionFileResponse`](../../doc/models/transaction-file-response.md)

## Example Usage

```python
transaction_file_creation_request = TransactionFileCreation(
    data=NewTransactionFile(
        attributes=Attributes52(
            file_format=FileFormatEnum.NDJSON,
            file_hash='f60071837de834af950f070aa08fc1e0e3e4b1f7014a6251eabf207eba10c817',
            file_size=1024,
            hashing_algorithm='SHA256',
            number_of_parts=1,
            payment_scheme='BACS',
            transaction_count=1,
            transaction_sum='1.00'
        ),
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        created_on=dateutil.parser.parse('09/26/2017 15:26:57'),
        modified_on=dateutil.parser.parse('09/26/2017 15:26:57'),
        version=0
    )
)

result = transaction_file_api_controller.create_transaction_file(
    transaction_file_creation_request=transaction_file_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Transaction File

Fetch transaction file

```python
def get_transaction_file(self,
                        transaction_file_id,
                        accept=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_file_id` | `uuid\|str` | Template, Required | Transaction File Id |
| `accept` | `str` | Header, Optional | Acceptable Formats, possible values are "application/vnd.api+json", "application/x-ndjson" and "application/x.form3.standard18" |

## Response Type

[`TransactionFileResponse`](../../doc/models/transaction-file-response.md)

## Example Usage

```python
transaction_file_id = '00001854-0000-0000-0000-000000000000'

result = transaction_file_api_controller.get_transaction_file(transaction_file_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Upload Transaction File

Put Transaction file chunk

```python
def upload_transaction_file(self,
                           transaction_file_id,
                           x_form_3_upload_part,
                           payload)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_file_id` | `uuid\|str` | Template, Required | Transaction File Id |
| `x_form_3_upload_part` | `str` | Header, Required | Which part of the file we are uploading |
| `payload` | `typing.BinaryIO` | Form, Required | - |

## Response Type

[`TransactionFileResponse`](../../doc/models/transaction-file-response.md)

## Example Usage

```python
transaction_file_id = '00001854-0000-0000-0000-000000000000'

x_form_3_upload_part = 'X-Form3-Upload-Part2'

payload = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = transaction_file_api_controller.upload_transaction_file(
    transaction_file_id,
    x_form_3_upload_part,
    payload
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Transaction File Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Transaction File Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Transaction File Admission

Creates a Transaction File Admission

```python
def create_transaction_file_admission(self,
                                     transaction_file_id,
                                     transaction_file_admission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_file_id` | `uuid\|str` | Template, Required | Transaction File Id |
| `transaction_file_admission_creation_request` | [`TransactionFileAdmissionCreation`](../../doc/models/transaction-file-admission-creation.md) | Body, Optional | - |

## Response Type

[`TransactionFileAdmissionResponse`](../../doc/models/transaction-file-admission-response.md)

## Example Usage

```python
transaction_file_id = '00001854-0000-0000-0000-000000000000'

transaction_file_admission_creation_request = TransactionFileAdmissionCreation(
    data=TransactionFileAdmission(
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        created_on=dateutil.parser.parse('09/26/2017 15:26:57'),
        modified_on=dateutil.parser.parse('09/26/2017 15:26:57'),
        version=0
    )
)

result = transaction_file_api_controller.create_transaction_file_admission(
    transaction_file_id,
    transaction_file_admission_creation_request=transaction_file_admission_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Transaction File Admission Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Transaction File Admission

Fetch transaction file admission

```python
def get_transaction_file_admission(self,
                                  transaction_file_id,
                                  transaction_file_admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_file_id` | `uuid\|str` | Template, Required | Transaction File Id |
| `transaction_file_admission_id` | `uuid\|str` | Template, Required | Transaction File Admission Id |

## Response Type

[`TransactionFileAdmissionResponse`](../../doc/models/transaction-file-admission-response.md)

## Example Usage

```python
transaction_file_id = '00001854-0000-0000-0000-000000000000'

transaction_file_admission_id = '00001a86-0000-0000-0000-000000000000'

result = transaction_file_api_controller.get_transaction_file_admission(
    transaction_file_id,
    transaction_file_admission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Transaction File Submission

Creates a Transaction File Submission

```python
def create_transaction_file_submission(self,
                                      transaction_file_id,
                                      transaction_file_submission_creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_file_id` | `uuid\|str` | Template, Required | Transaction File Id |
| `transaction_file_submission_creation_request` | [`TransactionFileSubmissionCreation`](../../doc/models/transaction-file-submission-creation.md) | Body, Optional | - |

## Response Type

[`TransactionFileSubmissionResponse`](../../doc/models/transaction-file-submission-response.md)

## Example Usage

```python
transaction_file_id = '00001854-0000-0000-0000-000000000000'

transaction_file_submission_creation_request = TransactionFileSubmissionCreation(
    data=TransactionFileSubmission(
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        created_on=dateutil.parser.parse('09/26/2017 15:26:57'),
        modified_on=dateutil.parser.parse('09/26/2017 15:26:57'),
        version=0
    )
)

result = transaction_file_api_controller.create_transaction_file_submission(
    transaction_file_id,
    transaction_file_submission_creation_request=transaction_file_submission_creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Transaction File Submission Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Transaction File Submission

Fetch transaction file submission

```python
def get_transaction_file_submission(self,
                                   transaction_file_id,
                                   transaction_file_submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_file_id` | `uuid\|str` | Template, Required | Transaction File Id |
| `transaction_file_submission_id` | `uuid\|str` | Template, Required | Transaction File Submission Id |

## Response Type

[`TransactionFileSubmissionResponse`](../../doc/models/transaction-file-submission-response.md)

## Example Usage

```python
transaction_file_id = '00001854-0000-0000-0000-000000000000'

transaction_file_submission_id = '00000bd8-0000-0000-0000-000000000000'

result = transaction_file_api_controller.get_transaction_file_submission(
    transaction_file_id,
    transaction_file_submission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Server Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

