
# Account Attributes Private Identification

## Structure

`AccountAttributesPrivateIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `List[str]` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `140` |
| `birth_country` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Z]{2}$` |
| `birth_date` | `date` | Optional | Customer birth date |
| `city` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `country` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Z]{2}$` |
| `identification` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `140` |
| `identification_issuer` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `identification_scheme` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `identification_scheme_code` | `str` | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |

## Example (as JSON)

```json
{
  "birth_country": "GB",
  "birth_date": "2017-07-23",
  "country": "GB",
  "identification": "L-123456789",
  "address": [
    "address2",
    "address3"
  ],
  "city": "city8"
}
```

