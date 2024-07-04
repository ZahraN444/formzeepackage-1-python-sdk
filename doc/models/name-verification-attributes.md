
# Name Verification Attributes

## Structure

`NameVerificationAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_classification` | [`AccountClassificationEnum`](../../doc/models/account-classification-enum.md) | Required | - |
| `account_number` | `str` | Required | **Constraints**: *Pattern*: `^[A-Z0-9]{6,34}$` |
| `account_number_code` | [`AccountNumberCodeEnum`](../../doc/models/account-number-code-enum.md) | Required | The type of identification given at `account_number` attribute |
| `bank_id` | `str` | Required | - |
| `bank_id_code` | `str` | Required, Constant | **Default**: `'GBDSC'` |
| `name` | `List[str]` | Required | Account holder names (for example title, first name, last name). Used for Confirmation of Payee matching.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `140` |
| `secondary_identification` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "account_classification": "personal",
  "account_number": "account_number6",
  "account_number_code": "IBAN",
  "bank_id": "bank_id8",
  "bank_id_code": "GBDSC",
  "name": [
    "name6",
    "name7",
    "name8"
  ],
  "secondary_identification": "secondary_identification4"
}
```

