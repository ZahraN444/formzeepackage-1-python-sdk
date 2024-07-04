
# Mandate Return Submission

## Structure

`MandateReturnSubmission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`Attributes47`](../../doc/models/attributes-47.md) | Optional | - |
| `created_on` | `datetime` | Optional | - |
| `id` | `uuid\|str` | Optional | - |
| `modified_on` | `datetime` | Optional | - |
| `organisation_id` | `uuid\|str` | Optional | - |
| `relationships` | [`Relationships18`](../../doc/models/relationships-18.md) | Optional | - |
| `mtype` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Za-z_]*$` |
| `version` | `int` | Optional | **Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "attributes": {
    "status": "delivery_confirmed",
    "status_reason": "status_reason6",
    "submission_datetime": "2016-03-13T12:52:32.123Z",
    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
  },
  "created_on": "2016-03-13T12:52:32.123Z",
  "id": "00001fd6-0000-0000-0000-000000000000",
  "modified_on": "2016-03-13T12:52:32.123Z",
  "organisation_id": "00000ed0-0000-0000-0000-000000000000"
}
```

