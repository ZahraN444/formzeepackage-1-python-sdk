
# Mandate Attributes

## Structure

`MandateAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Optional | **Constraints**: *Pattern*: `^[0-9.]{0,20}$` |
| `beneficiary_party` | [`MandateAttributesBeneficiaryParty`](../../doc/models/mandate-attributes-beneficiary-party.md) | Optional | - |
| `clearing_id` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `debtor_party` | [`MandateAttributesDebtorParty`](../../doc/models/mandate-attributes-debtor-party.md) | Optional | - |
| `frequency` | [`MandateFrequencyEnum`](../../doc/models/mandate-frequency-enum.md) | Optional | - |
| `numeric_reference` | `str` | Optional | - |
| `payment_scheme` | `str` | Optional | - |
| `processing_date` | `date` | Optional | - |
| `reference` | `str` | Optional | - |
| `scheme_payment_type` | `str` | Optional | - |
| `scheme_processing_date` | `date` | Optional | - |
| `source` | `str` | Optional | - |
| `status` | [`MandateStatusEnum`](../../doc/models/mandate-status-enum.md) | Optional | - |
| `status_reason` | `str` | Optional | - |
| `unique_scheme_id` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "amount": "amount2",
  "beneficiary_party": {
    "account_name": "account_name0",
    "account_number": "account_number8",
    "account_number_code": "IBAN",
    "account_type": 6,
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
  },
  "clearing_id": "clearing_id2",
  "currency": "currency0",
  "debtor_party": {
    "account_name": "account_name2",
    "account_number": "account_number4",
    "account_number_code": "IBAN",
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
    },
    "address": [
      "address8"
    ]
  }
}
```

