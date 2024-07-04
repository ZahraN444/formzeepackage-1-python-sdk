
# Senders Correspondent Account Holding Entity

## Structure

`SendersCorrespondentAccountHoldingEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_address` | `List[str]` | Optional | Sender's correspondent's address |
| `bank_id` | `str` | Optional | SWIFT BIC for sender's correspondent |
| `bank_id_code` | `str` | Optional | The type of identification provided at `bank_id` attribute. Must be ISO code as listed in the [External Code Sets spreadsheet](https://www.iso20022.org/external_code_list.page) |
| `bank_name` | `str` | Optional | Sender's correspondent's name |
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
  "bank_id": "333333",
  "bank_name": "XYZ BANK PLC",
  "bank_party_id": "//AT12345",
  "bank_id_code": "bank_id_code8"
}
```

