
# Beneficiary Debtor Organisation Identification

## Structure

`BeneficiaryDebtorOrganisationIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `identification` | `str` | Optional | Another ID of the organisation |
| `identification_code` | `str` | Optional | Code for the type of other ID of organisation |
| `identification_issuer` | `str` | Optional | Issuer of the other ID of organisation |
| `identification_scheme` | `str` | Optional | Custom internal code for the type of other ID of organisation |

## Example (as JSON)

```json
{
  "identification": "H7FNTJ4851HG0EXQ1Z70",
  "identification_code": "LEI",
  "identification_issuer": "London Stock Exchange",
  "identification_scheme": "Custom code"
}
```

