
# Account Attributes Organisation Identification Actor

## Structure

`AccountAttributesOrganisationIdentificationActor`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `birth_date` | `date` | Optional | - |
| `name` | `List[str]` | Optional | Actor names (for example title, first name, last name). Used for Confirmation of Payee matching.<br>**Constraints**: *Maximum Items*: `4`, *Minimum Length*: `1`, *Maximum Length*: `255` |
| `residency` | `str` | Optional | ISO 3166-1 code used to identify the domicile of the actor<br>**Constraints**: *Pattern*: `^[A-Z]{2}$` |
| `role` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "birth_date": "2017-07-23",
  "residency": "GB",
  "name": [
    "name2",
    "name3"
  ],
  "role": "role4"
}
```

