
# Mandate Attributes Beneficiary Party

## Structure

`MandateAttributesBeneficiaryParty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `account_number` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Z0-9]{6,34}$` |
| `account_number_code` | [`AccountNumberCodeEnum`](../../doc/models/account-number-code-enum.md) | Optional | The type of identification given at `account_number` attribute |
| `account_type` | `int` | Optional | - |
| `account_with` | [`AccountHoldingEntity`](../../doc/models/account-holding-entity.md) | Optional | Information about the financial institution servicing the account. |
| `address` | `List[str]` | Optional | - |
| `country` | `str` | Optional | - |
| `private_identification` | [`PrivateIdentification`](../../doc/models/private-identification.md) | Optional | - |

## Example (as JSON)

```json
{
  "account_number_code": "IBAN",
  "account_name": "account_name4",
  "account_number": "account_number6",
  "account_type": 184,
  "account_with": {
    "bank_address": [
      "bank_address4",
      "bank_address3",
      "bank_address2"
    ],
    "bank_id": "bank_id2",
    "bank_id_code": "PLKNR",
    "bank_ids": [
      {
        "bank_id": "bank_id4",
        "bank_id_code": "bank_id_code8"
      },
      {
        "bank_id": "bank_id4",
        "bank_id_code": "bank_id_code8"
      }
    ],
    "bank_name": "bank_name4",
    "bank_party_id": "bank_party_id6"
  }
}
```

