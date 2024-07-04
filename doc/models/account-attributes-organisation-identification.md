
# Account Attributes Organisation Identification

## Structure

`AccountAttributesOrganisationIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `actors` | [`List[AccountAttributesOrganisationIdentificationActor]`](../../doc/models/account-attributes-organisation-identification-actor.md) | Optional | - |
| `address` | `List[str]` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `140` |
| `city` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `country` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Z]{2}$` |
| `identification` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `140` |
| `identification_issuer` | `str` | Optional | - |
| `identification_scheme` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `identification_scheme_code` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `registration_number` | `str` | Optional | - |
| `tax_residency` | `str` | Optional | ISO 3166-1 code used to identify the domicile of the account<br>**Constraints**: *Pattern*: `^[A-Z]{2}$` |

## Example (as JSON)

```json
{
  "country": "GB",
  "tax_residency": "GB",
  "actors": [
    {
      "birth_date": "2016-03-13",
      "name": [
        "name8",
        "name9"
      ],
      "residency": "residency8",
      "role": "role8"
    },
    {
      "birth_date": "2016-03-13",
      "name": [
        "name8",
        "name9"
      ],
      "residency": "residency8",
      "role": "role8"
    }
  ],
  "address": [
    "address2",
    "address3"
  ],
  "city": "city2",
  "identification": "identification4"
}
```

