
# Query Response Admission

## Structure

`QueryResponseAdmission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`QueryResponseAdmissionAttributes`](../../doc/models/query-response-admission-attributes.md) | Required | - |
| `created_on` | `datetime` | Optional | - |
| `id` | `uuid\|str` | Required | - |
| `modified_on` | `datetime` | Optional | - |
| `organisation_id` | `uuid\|str` | Required | - |
| `relationships` | [`QueryResponseAdmissionRelationships`](../../doc/models/query-response-admission-relationships.md) | Optional | - |
| `mtype` | `str` | Required, Constant | **Default**: `'query_response_admissions'` |
| `version` | `int` | Required | **Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "attributes": {
    "status": "failed",
    "status_reason": "status_reason6"
  },
  "id": "00002162-0000-0000-0000-000000000000",
  "organisation_id": "0000105c-0000-0000-0000-000000000000",
  "type": "query_response_admissions",
  "version": 102,
  "created_on": "2016-03-13T12:52:32.123Z",
  "modified_on": "2016-03-13T12:52:32.123Z",
  "relationships": {
    "payment": {
      "data": [
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        },
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        },
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        }
      ]
    },
    "query": {
      "data": [
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        }
      ]
    },
    "query_response": {
      "data": [
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        }
      ]
    },
    "recall": {
      "data": [
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        },
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        },
        {
          "id": "00001c2a-0000-0000-0000-000000000000",
          "type": "type0"
        }
      ]
    }
  }
}
```
