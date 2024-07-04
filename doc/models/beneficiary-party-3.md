
# Beneficiary Party 3

## Structure

`BeneficiaryParty3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Name of beneficiary as given with account |
| `account_number` | `str` | Optional | Beneficiary account number |
| `account_number_code` | [`AccountNumberCodeEnum`](../../doc/models/account-number-code-enum.md) | Optional | The type of identification given at `account_number` attribute |
| `account_type` | `int` | Optional | The type of the account given with `beneficiary_party.account_number`. Single digit number. Only required if requested by the beneficiary party. Defaults to 0. |
| `account_with` | [`AccountHoldingEntity`](../../doc/models/account-holding-entity.md) | Optional | Information about the financial institution servicing the account. |
| `address` | `List[str]` | Optional | Beneficiary address |
| `building_number` | `str` | Optional | Building number of the Debtor address |
| `city` | `str` | Optional | City/Town of the Debtor address |
| `country` | `str` | Optional | Country of the beneficiary address, ISO 3166 format country code |
| `name` | `str` | Optional | Beneficiary name |
| `post_code` | `str` | Optional | Post code of the Debtor address |
| `private_identification` | [`PrivateIdentification`](../../doc/models/private-identification.md) | Optional | - |
| `province` | `str` | Optional | Province of the Debtor address |
| `street_name` | `str` | Optional | Street name of the Debtor address |

## Example (as JSON)

```json
{
  "account_name": "James Bond",
  "account_number": "71268996",
  "account_number_code": "IBAN",
  "account_type": 0,
  "address": [
    "1 Clarence Mew",
    "Horsforth",
    "Leeds Ls18 4EP"
  ],
  "city": "BRUSSELS",
  "country": "DE",
  "name": "James Bond",
  "street_name": "Park Avenue",
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

