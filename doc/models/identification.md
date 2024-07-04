
# Identification

## Structure

`Identification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_id` | `str` | Optional | Identification code of the financial institution. |
| `bank_id_code` | `str` | Optional | Type of identification provided in bank_id field. Required when bank_id is provided, not used otherwise. |
| `bank_ids` | [`List[AccountWithBankId]`](../../doc/models/account-with-bank-id.md) | Optional | Array for additional ID(s) of instructed (or other type of) agent |

## Example (as JSON)

```json
{
  "bank_id": "LOYDGB2L",
  "bank_id_code": "SWBIC",
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
}
```

