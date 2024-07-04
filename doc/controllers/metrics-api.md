# Metrics API

```python
metrics_api_controller = client.metrics_api
```

## Class Name

`MetricsAPIController`

## Methods

* [Query Endpoint for Metrics](../../doc/controllers/metrics-api.md#query-endpoint-for-metrics)
* [Query Endpoint for Metrics 1](../../doc/controllers/metrics-api.md#query-endpoint-for-metrics-1)
* [Query Range Endpoint for Metrics](../../doc/controllers/metrics-api.md#query-range-endpoint-for-metrics)
* [Query Range Endpoint for Metrics 1](../../doc/controllers/metrics-api.md#query-range-endpoint-for-metrics-1)
* [Federate Endpoint for Metrics](../../doc/controllers/metrics-api.md#federate-endpoint-for-metrics)


# Query Endpoint for Metrics

Query Endpoint for metrics

```python
def query_endpoint_for_metrics(self,
                              query,
                              time=None,
                              timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | `str` | Query, Required | Query to Execute |
| `time` | `str` | Query, Optional | RFC3339 or unix_timestamp |
| `timeout` | `str` | Query, Optional | See https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations |

## Response Type

[`MetricsQueryResponse`](../../doc/models/metrics-query-response.md)

## Example Usage

```python
query = 'query0'

result = metrics_api_controller.query_endpoint_for_metrics(query)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MetricsQueryResponseErrorException`](../../doc/models/metrics-query-response-error-exception.md) |
| 403 | Forbidden | `APIException` |
| 500 | Internal Server Error | `APIException` |


# Query Endpoint for Metrics 1

Query Endpoint for metrics

```python
def query_endpoint_for_metrics_1(self,
                                query,
                                time=None,
                                timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | `str` | Form, Required | Query to Execute |
| `time` | `str` | Form, Optional | RFC3339 or unix_timestamp |
| `timeout` | `str` | Form, Optional | See https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations |

## Response Type

[`MetricsQueryResponse`](../../doc/models/metrics-query-response.md)

## Example Usage

```python
query = 'query0'

result = metrics_api_controller.query_endpoint_for_metrics_1(query)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MetricsQueryResponseErrorException`](../../doc/models/metrics-query-response-error-exception.md) |
| 403 | Forbidden | `APIException` |
| 500 | Internal Server Error | `APIException` |


# Query Range Endpoint for Metrics

Query Range Endpoint for metrics

```python
def query_range_endpoint_for_metrics(self,
                                    query,
                                    time=None,
                                    timeout=None,
                                    start=None,
                                    end=None,
                                    step=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | `str` | Query, Required | Query to Execute |
| `time` | `str` | Query, Optional | RFC3339 or unix_timestamp |
| `timeout` | `str` | Query, Optional | See https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations |
| `start` | `str` | Query, Optional | RFC3339 or unix_timestamp |
| `end` | `str` | Query, Optional | RFC3339 or unix_timestamp |
| `step` | `str` | Query, Optional | duration or float |

## Response Type

[`MetricsQueryResponse`](../../doc/models/metrics-query-response.md)

## Example Usage

```python
query = 'query0'

result = metrics_api_controller.query_range_endpoint_for_metrics(query)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MetricsQueryResponseErrorException`](../../doc/models/metrics-query-response-error-exception.md) |
| 403 | Forbidden | `APIException` |
| 500 | Internal Server Error | `APIException` |


# Query Range Endpoint for Metrics 1

Query Range Endpoint for metrics

```python
def query_range_endpoint_for_metrics_1(self,
                                      query,
                                      time=None,
                                      timeout=None,
                                      start=None,
                                      end=None,
                                      step=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | `str` | Form, Required | Query to Execute |
| `time` | `str` | Form, Optional | RFC3339 or unix_timestamp |
| `timeout` | `str` | Form, Optional | See https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations |
| `start` | `str` | Form, Optional | RFC3339 or unix_timestamp |
| `end` | `str` | Form, Optional | RFC3339 or unix_timestamp |
| `step` | `str` | Form, Optional | duration or float |

## Response Type

[`MetricsQueryResponse`](../../doc/models/metrics-query-response.md)

## Example Usage

```python
query = 'query0'

result = metrics_api_controller.query_range_endpoint_for_metrics_1(query)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MetricsQueryResponseErrorException`](../../doc/models/metrics-query-response-error-exception.md) |
| 403 | Forbidden | `APIException` |
| 500 | Internal Server Error | `APIException` |


# Federate Endpoint for Metrics

Federate Endpoint for metrics

```python
def federate_endpoint_for_metrics(self,
                                 match)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `match` | `List[str]` | Query, Required | See https://prometheus.io/docs/prometheus/latest/querying/basics/#instant-vector-selectors |

## Response Type

`str`

## Example Usage

```python
match = [
    'match5',
    'match6'
]

result = metrics_api_controller.federate_endpoint_for_metrics(match)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`MetricsQueryResponseErrorException`](../../doc/models/metrics-query-response-error-exception.md) |
| 403 | Forbidden | `APIException` |
| 500 | Internal Server Error | `APIException` |

