
# Account Identification

## Structure

`AccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`AccountIdentificationAttributes`](../../doc/models/account-identification-attributes.md) | Required | - |
| `created_on` | `datetime` | Optional | - |
| `id` | `uuid\|str` | Required | Unique resource ID |
| `modified_on` | `datetime` | Optional | - |
| `organisation_id` | `uuid\|str` | Required | Unique ID of the organisation this resource is created by |
| `mtype` | `str` | Optional | Type of this resource, always account_identifications |
| `version` | `int` | Optional | Version number<br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "attributes": {
    "secondary_identification": "secondary_identification2"
  },
  "id": "7826c3cb-d6fd-41d0-b187-dc23ba928772",
  "organisation_id": "ee2fb143-6dfe-4787-b183-ca8ddd4164d2",
  "type": "account_identifications",
  "version": 0,
  "created_on": "2016-03-13T12:52:32.123Z",
  "modified_on": "2016-03-13T12:52:32.123Z"
}
```

