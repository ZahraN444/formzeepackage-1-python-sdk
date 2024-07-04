
# Account Attributes

## Structure

`AccountAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acceptance_qualifier` | [`AcceptanceQualifierEnum`](../../doc/models/acceptance-qualifier-enum.md) | Optional | All accepted payments will receive the matching qualifier code |
| `account_classification` | [`AccountClassification1Enum`](../../doc/models/account-classification-1-enum.md) | Optional | Is the account business or personal?<br>**Default**: `'Personal'` |
| `account_matching_opt_out` | `bool` | Optional | - deprecated - Is the account opted out of account matching, e.g. CoP?<br>**Default**: `False` |
| `account_number` | `str` | Optional | Account number of the account. A unique number will automatically be generated if not provided.<br>**Constraints**: *Pattern*: `^[A-Z0-9]{0,64}$` |
| `alternative_bank_account_names` | `List[str]` | Optional | - deprecated - Alternative account names. Used for Confirmation of Payee matching.<br>**Constraints**: *Maximum Items*: `3`, *Minimum Length*: `1`, *Maximum Length*: `140` |
| `alternative_names` | `List[str]` | Optional | Alternative names. Used for Confirmation of Payee matching.<br>**Constraints**: *Maximum Items*: `3`, *Minimum Length*: `1`, *Maximum Length*: `140` |
| `bank_account_name` | `str` | Optional | - deprecated - Primary account name. Used for Confirmation of Payee matching. Required if confirmation_of_payee_enabled is true for the organisation.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `140` |
| `bank_id` | `str` | Optional | Local country bank identifier. In the UK this is the sort code.<br>**Constraints**: *Pattern*: `^[A-Z0-9]{0,16}$` |
| `bank_id_code` | `str` | Optional | ISO 20022 code used to identify the type of bank ID being used<br>**Constraints**: *Pattern*: `^[A-Z]{0,16}$` |
| `base_currency` | `str` | Optional | ISO 4217 code used to identify the base currency of the account<br>**Constraints**: *Pattern*: `^[A-Z]{3}$` |
| `bic` | `str` | Optional | SWIFT BIC in either 8 or 11 character format<br>**Constraints**: *Pattern*: `^([A-Z]{6}[A-Z0-9]{2}\|[A-Z]{6}[A-Z0-9]{5})$` |
| `country` | `str` | Required | ISO 3166-1 code used to identify the domicile of the account<br>**Constraints**: *Pattern*: `^[A-Z]{2}$` |
| `customer_id` | `str` | Optional | A free-format reference that can be used to link this account to an external system<br>**Constraints**: *Pattern*: `^[a-zA-Z0-9-$@., ]{0,256}$` |
| `first_name` | `str` | Optional | - deprecated - Customer first name.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `iban` | `str` | Optional | IBAN of the account. Will be calculated from other fields if not supplied.<br>**Constraints**: *Pattern*: `^[A-Z]{2}[0-9]{2}[A-Z0-9]{0,64}$` |
| `joint_account` | `bool` | Optional | Is the account joint?<br>**Default**: `False` |
| `name` | `List[str]` | Optional | Account holder names (for example title, first name, last name). Used for Confirmation of Payee matching.<br>**Constraints**: *Maximum Items*: `4`, *Minimum Length*: `1`, *Maximum Length*: `140` |
| `name_matching_status` | [`NameMatchingStatusEnum`](../../doc/models/name-matching-status-enum.md) | Optional | Describes the status of the account for name matching via CoP. The value determines the code with which Form3 responds to matched CoP requests to this account.<br>**Default**: `'supported'` |
| `organisation_identification` | [`AccountAttributesOrganisationIdentification`](../../doc/models/account-attributes-organisation-identification.md) | Optional | - |
| `private_identification` | [`AccountAttributesPrivateIdentification`](../../doc/models/account-attributes-private-identification.md) | Optional | - |
| `processing_service` | `str` | Optional | - deprecated - Accounting system or service. It will be added to each payment received to an account.<br>**Constraints**: *Maximum Length*: `35` |
| `reference_mask` | `str` | Optional | When set will apply a validation mask on the payment reference to each payment received to an account.<br>**Constraints**: *Maximum Length*: `35` |
| `secondary_identification` | `str` | Optional | Secondary identification, e.g. building society roll number. Used for Confirmation of Payee.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `140` |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Current status of the account |
| `status_reason` | [`StatusReasonEnum`](../../doc/models/status-reason-enum.md) | Optional | Used to determine appropriate scheme or internal payment reject code. Account status field must be set to closed to use this functionality. |
| `switched` | `bool` | Optional | - deprecated - Indicates whether the account has been switched using the Current Account Switch Service.<br>**Default**: `False` |
| `switched_account_details` | [`SwitchedAccountDetails`](../../doc/models/switched-account-details.md) | Optional | Alternate Account details to use in case the account has been switched away from this organisation. |
| `title` | `str` | Optional | - deprecated - Customer title.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `user_defined_data` | [`List[UserDefinedData]`](../../doc/models/user-defined-data.md) | Optional | All purpose list of key-value pairs to store specific data for the associated account. It will be added to each payment received to an account.<br>**Constraints**: *Maximum Items*: `5` |
| `user_defined_information` | `str` | Optional | - deprecated - All purpose field to store specific data for the associated account. It will be added to each payment received to an account.<br>**Constraints**: *Maximum Length*: `35` |
| `validation_type` | [`ValidationTypeEnum`](../../doc/models/validation-type-enum.md) | Optional | optional validation to apply to the account |

## Example (as JSON)

```json
{
  "account_classification": "Personal",
  "account_matching_opt_out": false,
  "account_number": "41426819",
  "bank_id": "400300",
  "bank_id_code": "GBDSC",
  "base_currency": "GBP",
  "bic": "NWBKGB22",
  "country": "GB",
  "customer_id": "12345",
  "iban": "GB11NWBK40030041426819",
  "joint_account": false,
  "name_matching_status": "supported",
  "reference_mask": "4929############",
  "status_reason": "transferred",
  "switched": false,
  "title": "Ms",
  "acceptance_qualifier": "some_other_time",
  "alternative_bank_account_names": [
    "alternative_bank_account_names1"
  ]
}
```

