
# Identification 1

## Structure

`Identification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_id` | `str` | Optional | - |
| `bank_id_code` | `str` | Optional | - |
| `bank_ids` | [`List[RequestForInformationAgentBankId]`](../../doc/models/request-for-information-agent-bank-id.md) | Optional | - |

## Example (as JSON)

```json
{
  "bank_id": "bank_id0",
  "bank_id_code": "bank_id_code8",
  "bank_ids": [
    {
      "bank_id": "bank_id4",
      "bank_id_code": "bank_id_code8"
    },
    {
      "bank_id": "bank_id4",
      "bank_id_code": "bank_id_code8"
    }
  ]
}
```

