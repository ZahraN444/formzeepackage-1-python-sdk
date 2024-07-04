
# Beneficiary Party 1

## Structure

`BeneficiaryParty1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Name of beneficiary as given with account |
| `account_number` | `str` | Optional | Beneficiary account number |
| `account_number_code` | [`AccountNumberCodeEnum`](../../doc/models/account-number-code-enum.md) | Optional | The type of identification given at `account_number` attribute |
| `account_proxy` | [`BeneficiaryDebtorAccountProxy`](../../doc/models/beneficiary-debtor-account-proxy.md) | Optional | - |
| `account_type` | `int` | Optional | The type of the account given with `beneficiary_party.account_number`. Single digit number. Only required if requested by the beneficiary party. Defaults to 0. |
| `account_with` | [`BeneficiaryDebtorAccountHoldingEntity`](../../doc/models/beneficiary-debtor-account-holding-entity.md) | Optional | - |
| `additional_address_line` | `str` | Optional | Additional address line of the beneficiary address |
| `address` | `List[str]` | Optional | Beneficiary address |
| `birth_city` | `str` | Optional | Beneficiary birth city |
| `birth_country` | `str` | Optional | Beneficiary birth country, ISO 3166 format country code |
| `birth_date` | `date` | Optional | Beneficiary birth date. Formatted according to ISO 8601 format: YYYY-MM-DD |
| `birth_province` | `str` | Optional | Beneficiary birth province |
| `building_number` | `str` | Optional | Building number of the beneficiary address |
| `city` | `str` | Optional | City/Town of the Beneficiary address |
| `country` | `str` | Optional | Country of the beneficiary address, ISO 3166 format country code |
| `country_of_residence` | `str` | Optional | Country of residence of the beneficiary party, ISO 3166 format country code |
| `name` | `str` | Optional | Beneficiary name |
| `organisation_identification` | `str` | Optional | Organisation identification of a beneficiary, used in the case that the beneficiary is an organisation and not a private person |
| `organisation_identification_code` | `str` | Optional | The code that specifies the type of `organisation_identification` |
| `organisation_identification_issuer` | `str` | Optional | Issuer of the `organisation_identification` |
| `organisation_identification_scheme` | `str` | Optional | The code that specifies the scheme of `organisation_identification` |
| `organisation_identifications` | [`List[BeneficiaryDebtorOrganisationIdentification]`](../../doc/models/beneficiary-debtor-organisation-identification.md) | Optional | Array for additional ID(s) of beneficiary organisation |
| `post_code` | `str` | Optional | Post code of the beneficiary address |
| `private_identification` | [`PrivateIdentification`](../../doc/models/private-identification.md) | Optional | - |
| `province` | `str` | Optional | Province of the beneficiary address |
| `street_name` | `str` | Optional | Street name of the beneficiary address |
| `telephone_number` | `str` | Optional | Beneficiary phone number |

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
  "birth_city": "PARIS",
  "birth_country": "FR",
  "birth_date": "1977-02-28",
  "birth_province": "NORTHSIDE",
  "city": "BRUSSELS",
  "country": "DE",
  "country_of_residence": "PL",
  "name": "James Bond",
  "organisation_identification": "ID1234656",
  "organisation_identification_code": "BIC",
  "organisation_identification_issuer": "NATIONAL WESTMINSTER BANK PLC",
  "organisation_identification_scheme": "CustomerId",
  "street_name": "Park Avenue",
  "telephone_number": "+447921123987",
  "account_proxy": {
    "proxy": "proxy4",
    "proxy_id": "proxy_id4",
    "proxy_id_code": "proxy_id_code4"
  }
}
```

