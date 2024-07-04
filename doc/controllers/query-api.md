# Query Api

```python
query_api_controller = client.query_api
```

## Class Name

`QueryApiController`

## Methods

* [List Queries](../../doc/controllers/query-api.md#list-queries)
* [Create Query](../../doc/controllers/query-api.md#create-query)
* [Get Query](../../doc/controllers/query-api.md#get-query)
* [Get Query Admission](../../doc/controllers/query-api.md#get-query-admission)
* [Create Query Response](../../doc/controllers/query-api.md#create-query-response)
* [Get Query Response](../../doc/controllers/query-api.md#get-query-response)
* [Get Query Response Admission](../../doc/controllers/query-api.md#get-query-response-admission)
* [Create Query Response Submission](../../doc/controllers/query-api.md#create-query-response-submission)
* [Get Query Response Submission](../../doc/controllers/query-api.md#get-query-response-submission)
* [Create Query Submission](../../doc/controllers/query-api.md#create-query-submission)
* [Get Query Submission](../../doc/controllers/query-api.md#get-query-submission)


# List Queries

Get Query

```python
def list_queries(self,
                filter_organisation_id=None,
                filter_status=None,
                filter_query_type=None,
                filter_auto_handled=None,
                filter_processing_date_from=None,
                filter_processing_date_to=None,
                filter_created_on_from=None,
                filter_created_on_to=None,
                filter_payment_id=None,
                filter_payment_admission_id=None,
                filter_payment_submission_id=None,
                filter_recall_id=None,
                filter_recall_submission_id=None,
                filter_query_id=None,
                page_number=None,
                page_size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | The organisations to filter on |
| `filter_status` | [`ReportRequestStatusEnum`](../../doc/models/report-request-status-enum.md) | Query, Optional | Find all queries for a given status |
| `filter_query_type` | `str` | Query, Optional | Find all queries for a given query type |
| `filter_auto_handled` | `bool` | Query, Optional | Find all queries for given auto handled flag |
| `filter_processing_date_from` | `date` | Query, Optional | Find all queries from a certain value date. |
| `filter_processing_date_to` | `date` | Query, Optional | Find all queries up to a certain value date. |
| `filter_created_on_from` | `datetime` | Query, Optional | Find all queries from a certain created date. |
| `filter_created_on_to` | `datetime` | Query, Optional | Find all queries up to a certain created date. |
| `filter_payment_id` | `uuid\|str` | Query, Optional | Find all queries with a certain payment id. |
| `filter_payment_admission_id` | `uuid\|str` | Query, Optional | Find all queries with a certain payment admission id. |
| `filter_payment_submission_id` | `uuid\|str` | Query, Optional | Find all queries with a certain payment submission id. |
| `filter_recall_id` | `uuid\|str` | Query, Optional | Find all queries with a certain recall id. |
| `filter_recall_submission_id` | `uuid\|str` | Query, Optional | Find all queries with a certain recall submission id. |
| `filter_query_id` | `uuid\|str` | Query, Optional | Find all queries with a certain query id. |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |

## Response Type

[`QueryListResponse`](../../doc/models/query-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = query_api_controller.list_queries(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Query bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 502 | Query gateway issue | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Query

Create a Query

```python
def create_query(self,
                creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creation_request` | [`QueryCreation`](../../doc/models/query-creation.md) | Body, Optional | - |

## Response Type

[`QueryFetchResponse`](../../doc/models/query-fetch-response.md)

## Example Usage

```python
creation_request = QueryCreation(
    data=NewQuery(
        attributes=QueryAttributes(
            query_type=QueryTypeEnum.CLAIM_NON_RECEIPT
        ),
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='00000b24-0000-0000-0000-000000000000',
        mtype='queries'
    )
)

result = query_api_controller.create_query(
    creation_request=creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 502 | gateway issue | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Query

Fetch a Query

```python
def get_query(self,
             query_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |

## Response Type

[`QueryFetchResponse`](../../doc/models/query-fetch-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

result = query_api_controller.get_query(query_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Query Admission

Fetch a Query Admission

```python
def get_query_admission(self,
                       query_id,
                       query_admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `query_admission_id` | `uuid\|str` | Template, Required | Query Admission ID |

## Response Type

[`QueryAdmissionResponse`](../../doc/models/query-admission-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

query_admission_id = '00001fc0-0000-0000-0000-000000000000'

result = query_api_controller.get_query_admission(
    query_id,
    query_admission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Query Response

Create a Query Response

```python
def create_query_response(self,
                         query_id,
                         creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `creation_request` | [`QueryResponseCreation`](../../doc/models/query-response-creation.md) | Body, Optional | - |

## Response Type

[`QueryResponseResponse`](../../doc/models/query-response-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

creation_request = QueryResponseCreation(
    data=NewQueryResponse(
        attributes=QueryResponseAttributes(
            answer=QueryResponseAnswerEnum.TRANSACTION_NOT_PROCESSED
        ),
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='00000b24-0000-0000-0000-000000000000',
        mtype='query_responses'
    )
)

result = query_api_controller.create_query_response(
    query_id,
    creation_request=creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 502 | gateway issue | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Query Response

Fetch a Query Response

```python
def get_query_response(self,
                      query_id,
                      query_response_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `query_response_id` | `uuid\|str` | Template, Required | Query Response ID |

## Response Type

[`QueryResponseResponse`](../../doc/models/query-response-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

query_response_id = '00000e02-0000-0000-0000-000000000000'

result = query_api_controller.get_query_response(
    query_id,
    query_response_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Query Response Admission

Fetch a Query Response Admission

```python
def get_query_response_admission(self,
                                query_id,
                                query_response_id,
                                query_response_admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `query_response_id` | `uuid\|str` | Template, Required | Query Response ID |
| `query_response_admission_id` | `uuid\|str` | Template, Required | Query Response Admission ID |

## Response Type

[`QueryResponseAdmissionResponse`](../../doc/models/query-response-admission-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

query_response_id = '00000e02-0000-0000-0000-000000000000'

query_response_admission_id = '00000f22-0000-0000-0000-000000000000'

result = query_api_controller.get_query_response_admission(
    query_id,
    query_response_id,
    query_response_admission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Query Response Submission

Create a Query Response Submission

```python
def create_query_response_submission(self,
                                    query_id,
                                    query_response_id,
                                    creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `query_response_id` | `uuid\|str` | Template, Required | Query Response ID |
| `creation_request` | [`QueryResponseSubmissionCreation`](../../doc/models/query-response-submission-creation.md) | Body, Optional | - |

## Response Type

[`QueryResponseSubmissionResponse`](../../doc/models/query-response-submission-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

query_response_id = '00000e02-0000-0000-0000-000000000000'

creation_request = QueryResponseSubmissionCreation(
    data=NewQueryResponseSubmission(
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='00000b24-0000-0000-0000-000000000000',
        mtype='query_response_submissions'
    )
)

result = query_api_controller.create_query_response_submission(
    query_id,
    query_response_id,
    creation_request=creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 502 | gateway issue | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Query Response Submission

Fetch a Query Response Submission

```python
def get_query_response_submission(self,
                                 query_id,
                                 query_response_id,
                                 query_response_submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `query_response_id` | `uuid\|str` | Template, Required | Query Response ID |
| `query_response_submission_id` | `uuid\|str` | Template, Required | Query Response Submission ID |

## Response Type

[`QueryResponseSubmissionResponse`](../../doc/models/query-response-submission-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

query_response_id = '00000e02-0000-0000-0000-000000000000'

query_response_submission_id = '00000a82-0000-0000-0000-000000000000'

result = query_api_controller.get_query_response_submission(
    query_id,
    query_response_id,
    query_response_submission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Create Query Submission

Create a Query submission

```python
def create_query_submission(self,
                           query_id,
                           creation_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `creation_request` | [`QuerySubmissionCreation`](../../doc/models/query-submission-creation.md) | Body, Optional | - |

## Response Type

[`QuerySubmissionResponse`](../../doc/models/query-submission-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

creation_request = QuerySubmissionCreation(
    data=NewQuerySubmission(
        id='00001c2a-0000-0000-0000-000000000000',
        organisation_id='00000b24-0000-0000-0000-000000000000',
        mtype='query_submissions'
    )
)

result = query_api_controller.create_query_submission(
    query_id,
    creation_request=creation_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 502 | gateway issue | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Query Submission

Fetch a Query submission

```python
def get_query_submission(self,
                        query_id,
                        query_submission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `uuid\|str` | Template, Required | Query ID |
| `query_submission_id` | `uuid\|str` | Template, Required | Query Submission ID |

## Response Type

[`QuerySubmissionResponse`](../../doc/models/query-submission-response.md)

## Example Usage

```python
query_id = '00000eba-0000-0000-0000-000000000000'

query_submission_id = '00001434-0000-0000-0000-000000000000'

result = query_api_controller.get_query_submission(
    query_id,
    query_submission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

