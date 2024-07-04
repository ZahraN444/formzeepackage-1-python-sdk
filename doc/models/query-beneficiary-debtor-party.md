
# Query Beneficiary Debtor Party

## Structure

`QueryBeneficiaryDebtorParty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | Debtor/Beneficiary account number. Allows upper case and numeric characters.<br>**Constraints**: *Maximum Length*: `34` |
| `account_number_code` | [`QueryAccountNumberCodeEnum`](../../doc/models/query-account-number-code-enum.md) | Optional | The type of identification given at `account_number` attribute<br>**Constraints**: *Maximum Length*: `4` |
| `account_proxy` | [`QueryBeneficiaryDebtorAccountProxy`](../../doc/models/query-beneficiary-debtor-account-proxy.md) | Optional | - |
| `account_with` | [`AccountWith`](../../doc/models/account-with.md) | Optional | Debtor/Beneficiary agents bank information. |
| `additional_address_line` | `str` | Optional | Additional address line of the debtor/beneficiary address |
| `birth_city` | `str` | Optional | Debtor/Beneficiary birth city |
| `birth_country` | `str` | Optional | Debtor/Beneficiary birth country. ISO 3166 format country code |
| `birth_date` | `date` | Optional | Debtor/Beneficiary birth date. Formatted ISO 8601 format YYYY-MM-DD |
| `birth_province` | `str` | Optional | Debtor/Beneficiary birth province |
| `building_number` | `str` | Optional | Building number of the debtor/beneficiary address |
| `city` | `str` | Optional | City/Town of the debtor/beneficiary address |
| `country` | `str` | Optional | Country of debtor/beneficiary address. ISO 3166 format country code |
| `country_of_residence` | `str` | Optional | Country of residence of the debtor/beneficiary, ISO 3166 format country code |
| `name` | `str` | Optional | Debtor/Beneficiary name |
| `organisation_identification` | `str` | Optional | Organisation identification of a debtor/beneficiary, in the case that the debtor/beneficiary is an organisation and not a private person. |
| `organisation_identification_code` | `str` | Optional | The code that specifies the type of `organisation_identification` |
| `organisation_identification_issuer` | `str` | Optional | Issuer of the `organisation_identification` |
| `organisation_identification_scheme` | `str` | Optional | The code that specifies the scheme of `organisation_identification` |
| `organisation_identifications` | [`List[QueryBeneficiaryDebtorOrganisationIdentification]`](../../doc/models/query-beneficiary-debtor-organisation-identification.md) | Optional | Array for additional ID(s) of ultimate organisation |
| `post_code` | `str` | Optional | Post code of the debtor/beneficiary address |
| `private_identification` | [`QueryPrivateIdentification`](../../doc/models/query-private-identification.md) | Optional | - |
| `province` | `str` | Optional | Province of the debtor/beneficiary address |
| `street_name` | `str` | Optional | Street name of the debtor/beneficiary address |

## Example (as JSON)

```json
{
  "account_number": "12345678",
  "account_number_code": "IBAN",
  "birth_city": "New-York",
  "birth_country": "FR",
  "birth_date": "1973-01-31",
  "birth_province": "SOUTH SIDE",
  "city": "BRUSSELS",
  "country": "GB",
  "country_of_residence": "UA",
  "name": "Jane Bond",
  "organisation_identification": "ID1234656",
  "organisation_identification_code": "BIC",
  "organisation_identification_issuer": "NATIONAL WESTMINSTER BANK PLC",
  "organisation_identification_scheme": "CustomerId",
  "street_name": "Park Avenue",
  "account_proxy": {
    "proxy": "proxy4",
    "proxy_id": "proxy_id4",
    "proxy_id_code": "proxy_id_code4"
  },
  "account_with": {
    "bank_id": "bank_id2",
    "bank_id_code": "bank_id_code0",
    "bank_name": "bank_name4"
  },
  "additional_address_line": "additional_address_line6"
}
```

