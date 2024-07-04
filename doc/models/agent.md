
# Agent

## Structure

`Agent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | Account number of the financial institution. Can be BBAN or IBAN. |
| `account_number_code` | [`AccountNumberCodeEnum`](../../doc/models/account-number-code-enum.md) | Optional | The type of identification given at `account_number` attribute |
| `address` | `List[str]` | Optional | - |
| `identification` | [`Identification`](../../doc/models/identification.md) | Optional | - |
| `name` | `str` | Optional | Name by which the financial institution is known |
| `role` | [`AgentRoleEnum`](../../doc/models/agent-role-enum.md) | Optional | Role of the agent in the payment chain. Enum of pre-defined values, new values can be added when needed |

## Example (as JSON)

```json
{
  "account_number": "BBAN",
  "account_number_code": "IBAN",
  "address": [
    "1 Clarence Mew, Horsforth, Leeds UK 4EP"
  ],
  "name": "Lloyds Bank",
  "role": "IntermediaryAgent1",
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
  }
}
```

