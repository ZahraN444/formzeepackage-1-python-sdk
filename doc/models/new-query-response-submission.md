
# New Query Response Submission

## Structure

`NewQueryResponseSubmission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`Attributes50`](../../doc/models/attributes-50.md) | Optional | - |
| `id` | `uuid\|str` | Required | - |
| `organisation_id` | `uuid\|str` | Required | - |
| `mtype` | `str` | Required, Constant | **Default**: `'query_response_submissions'` |

## Example (as JSON)

```json
{
  "id": "00001b3a-0000-0000-0000-000000000000",
  "organisation_id": "00000a34-0000-0000-0000-000000000000",
  "type": "query_response_submissions",
  "attributes": {
    "auto": false
  }
}
```

