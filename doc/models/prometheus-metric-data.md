
# Prometheus Metric Data

## Structure

`PrometheusMetricData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | [`List[PrometheusResultItem]`](../../doc/models/prometheus-result-item.md) | Optional | - |
| `result_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "result": [
    {
      "metric": {
        "key0": "metric6",
        "key1": "metric5",
        "key2": "metric4"
      },
      "value": [
        {
          "key1": "val1",
          "key2": "val2"
        }
      ]
    },
    {
      "metric": {
        "key0": "metric6",
        "key1": "metric5",
        "key2": "metric4"
      },
      "value": [
        {
          "key1": "val1",
          "key2": "val2"
        }
      ]
    }
  ],
  "resultType": "resultType6"
}
```

