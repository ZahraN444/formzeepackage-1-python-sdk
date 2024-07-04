
# Query Attributes

## Structure

`QueryAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agents` | [`List[RequestForInformationAgent]`](../../doc/models/request-for-information-agent.md) | Optional | - |
| `auto_handled` | `bool` | Optional | - |
| `creator_party` | [`RequestForInformationCreatorParty`](../../doc/models/request-for-information-creator-party.md) | Optional | - |
| `message_id` | `str` | Optional | - |
| `processing_date` | `date` | Optional | - |
| `query_sub_types` | `List[str]` | Optional | - |
| `query_type` | [`QueryTypeEnum`](../../doc/models/query-type-enum.md) | Required | - |
| `references` | [`List[RequestForInformationReference]`](../../doc/models/request-for-information-reference.md) | Optional | - |
| `requested_information` | [`List[RequestForInformationRequestedInformation]`](../../doc/models/request-for-information-requested-information.md) | Optional | - |
| `scheme_transaction_id` | `str` | Optional | - |
| `status` | [`ReportRequestStatusEnum`](../../doc/models/report-request-status-enum.md) | Optional | - |
| `unstructured_message` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "agents": [
    {
      "identification": {
        "bank_id": "bank_id4",
        "bank_id_code": "bank_id_code2",
        "bank_ids": [
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          }
        ]
      },
      "role": "role6"
    },
    {
      "identification": {
        "bank_id": "bank_id4",
        "bank_id_code": "bank_id_code2",
        "bank_ids": [
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          }
        ]
      },
      "role": "role6"
    }
  ],
  "auto_handled": false,
  "creator_party": {
    "birth_city": "birth_city6",
    "birth_country": "birth_country0",
    "birth_date": "birth_date8",
    "birth_province": "birth_province6",
    "name": "name6"
  },
  "message_id": "message_id2",
  "processing_date": "2016-03-13",
  "query_type": "claim_non_receipt"
}
```

