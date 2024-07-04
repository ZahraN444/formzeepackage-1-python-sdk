
# Query Submission

## Structure

`QuerySubmission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`QuerySubmissionAttributes`](../../doc/models/query-submission-attributes.md) | Required | - |
| `created_on` | `datetime` | Optional | - |
| `id` | `uuid\|str` | Required | - |
| `modified_on` | `datetime` | Optional | - |
| `organisation_id` | `uuid\|str` | Required | - |
| `relationships` | [`QuerySubmissionRelationships`](../../doc/models/query-submission-relationships.md) | Optional | - |
| `mtype` | `str` | Required, Constant | **Default**: `'query_submissions'` |
| `version` | `int` | Required | **Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "attributes": {
    "status": "submitted",
    "status_reason": "status_reason6"
  },
  "id": "00002292-0000-0000-0000-000000000000",
  "organisation_id": "0000118c-0000-0000-0000-000000000000",
  "type": "query_submissions",
  "version": 134,
  "created_on": "2016-03-13T12:52:32.123Z",
  "modified_on": "2016-03-13T12:52:32.123Z",
  "relationships": {
    "query": {
      "data": [
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        }
      ]
    }
  }
}
```

