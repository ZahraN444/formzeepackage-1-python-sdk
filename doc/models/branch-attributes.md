
# Branch Attributes

## Structure

`BranchAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acceptance_qualifier` | [`AcceptanceQualifierEnum`](../../doc/models/acceptance-qualifier-enum.md) | Optional | All accepted payments will receive the matching qualifier code |
| `bank_id` | `str` | Required | Local country bank identifier. In the UK this is the sort code.<br>**Constraints**: *Pattern*: `^[A-Z0-9]{1,11}$` |
| `bank_id_code` | `str` | Required | ISO 20022 code used to identify the type of bank ID being used<br>**Constraints**: *Pattern*: `^[A-Z]{0,16}$` |
| `reference_mask` | `str` | Optional | if present – has effect of making secondary reference in payment mandatory |
| `user_defined_data` | [`List[UserDefinedData]`](../../doc/models/user-defined-data.md) | Optional | All purpose list of key-value pairs to store specific data.<br>**Constraints**: *Maximum Items*: `5` |
| `validation_type` | [`BranchValidationTypeEnum`](../../doc/models/branch-validation-type-enum.md) | Optional | optional validation to apply to the branch |

## Example (as JSON)

```json
{
  "bank_id": "400300",
  "bank_id_code": "GBDSC",
  "reference_mask": "4929############",
  "acceptance_qualifier": "after_next_working_day",
  "user_defined_data": [
    {
      "key": "key6",
      "value": "value8"
    },
    {
      "key": "key6",
      "value": "value8"
    },
    {
      "key": "key6",
      "value": "value8"
    }
  ],
  "validation_type": "card"
}
```

