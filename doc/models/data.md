
# Data

## Structure

`Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`Attributes49`](../../doc/models/attributes-49.md) | Optional | - |
| `created_on` | `datetime` | Optional | - |
| `id` | `uuid\|str` | Optional | - |
| `modified_on` | `datetime` | Optional | - |
| `organisation_id` | `uuid\|str` | Optional | - |
| `mtype` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Za-z_]*$` |
| `version` | `int` | Optional | **Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "attributes": {
    "file_identifier": "file_identifier6",
    "file_number": "file_number4",
    "last_payment_date": "2016-03-13",
    "status": "validation_passed",
    "status_reason": "status_reason6"
  },
  "created_on": "2016-03-13T12:52:32.123Z",
  "id": "0000255c-0000-0000-0000-000000000000",
  "modified_on": "2016-03-13T12:52:32.123Z",
  "organisation_id": "00001456-0000-0000-0000-000000000000"
}
```

