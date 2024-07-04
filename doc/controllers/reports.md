# Reports

```python
reports_controller = client.reports
```

## Class Name

`ReportsController`

## Methods

* [List Reports](../../doc/controllers/reports.md#list-reports)
* [Get Report](../../doc/controllers/reports.md#get-report)
* [Get Report Admission by ID](../../doc/controllers/reports.md#get-report-admission-by-id)


# List Reports

List reports

```python
def list_reports(self,
                page_number=None,
                page_size=100,
                filter_organisation_id=None,
                filter_report_type=None,
                filter_report_type_description=None,
                filter_report_source=None,
                filter_created_on_after=None,
                filter_created_on_before=None,
                filter_modified_on_after=None,
                filter_modified_on_before=None,
                filter_processing_date_from=None,
                filter_processing_date_to=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation Ids |
| `filter_report_type` | `str` | Query, Optional | Filter by ReportType |
| `filter_report_type_description` | `str` | Query, Optional | Filter by Report Type Description |
| `filter_report_source` | `str` | Query, Optional | Filter by Report Source |
| `filter_created_on_after` | `datetime` | Query, Optional | Request reports created after specific date time |
| `filter_created_on_before` | `datetime` | Query, Optional | Request reports created after specific date time |
| `filter_modified_on_after` | `datetime` | Query, Optional | Request reports modified after specific date time |
| `filter_modified_on_before` | `datetime` | Query, Optional | Request reports modified before specific date time |
| `filter_processing_date_from` | `date` | Query, Optional | Request reports with processing date from specific date (inclusive) |
| `filter_processing_date_to` | `date` | Query, Optional | Request reports with processing date to specific date (inclusive) |

## Response Type

[`ReportDetailsListResponse`](../../doc/models/report-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = reports_controller.list_reports(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Reports bad request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Report

Get report by ID

```python
def get_report(self,
              id,
              accept)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Report ID |
| `accept` | `str` | Header, Required | Acceptable Format |

## Response Type

[`ReportDetailsResponse`](../../doc/models/report-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

accept = 'Accept0'

result = reports_controller.get_report(
    id,
    accept
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Report Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 406 | Report not available in acceptable format | [`ApiErrorException`](../../doc/models/api-error-exception.md) |


# Get Report Admission by ID

Get Report Admission by ID

```python
def get_report_admission_by_id(self,
                              id,
                              admission_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Report Id |
| `admission_id` | `uuid\|str` | Template, Required | Report Admission ID |

## Response Type

[`ReportAdmissionDetailsResponse`](../../doc/models/report-admission-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

admission_id = '00000f44-0000-0000-0000-000000000000'

result = reports_controller.get_report_admission_by_id(
    id,
    admission_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 403 | Forbidden | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

