
# Account Holding Entity

Information about the financial institution servicing the account.

## Structure

`AccountHoldingEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_address` | `List[str]` | Optional | Financial institution address |
| `bank_id` | `str` | Required | **Constraints**: *Pattern*: `^[A-Z0-9]{0,16}$` |
| `bank_id_code` | [`BankIdCodeEnum`](../../doc/models/bank-id-code-enum.md) | Required | - |
| `bank_ids` | [`List[AccountWithBankId]`](../../doc/models/account-with-bank-id.md) | Optional | Array for additional ID(s) for agent |
| `bank_name` | `str` | Optional | Financial institution name |
| `bank_party_id` | `str` | Optional | Identifier of the financial institution which services the account |

## Example (as JSON)

```json
{
  "bank_address": [
    "Liverpool Customer Service Centre",
    "Stevenson Way",
    "Wavertree",
    "L13 1NW"
  ],
  "bank_id": "bank_id0",
  "bank_id_code": "ESNCC",
  "bank_name": "NATIONAL WESTMINSTER BANK PLC",
  "bank_party_id": "//AT12345",
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

