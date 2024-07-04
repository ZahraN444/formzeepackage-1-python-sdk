
# Role

## Structure

`Role`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`RoleAttributes`](../../doc/models/role-attributes.md) | Optional | - |
| `id` | `uuid\|str` | Optional | Unique resource ID |
| `organisation_id` | `uuid\|str` | Optional | Unique ID of the organisation this resource is created by |
| `mtype` | `str` | Optional | Name of the resource type |
| `version` | `int` | Optional | Version number<br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "id": "7826c3cb-d6fd-41d0-b187-dc23ba928772",
  "organisation_id": "ee2fb143-6dfe-4787-b183-ca8ddd4164d2",
  "type": "role",
  "version": 0,
  "attributes": {
    "name": "name4",
    "parent_role_id": "00000bf4-0000-0000-0000-000000000000"
  }
}
```

