
# Attributes 18

## Structure

`Attributes18`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_time` | `datetime` | Optional | Timestamp when the change was requested |
| `actioned_by` | `uuid\|str` | Optional | User ID of the user who requested the change |
| `after_data` | `object` | Optional | Snapshot of what the data would be after the change (empty if the request was to DELETE a record) |
| `before_data` | `object` | Optional | Snapshot of the data before the change (empty if the request was to CREATE a new record) |
| `description` | `str` | Optional | Textual description of the change being made<br>**Constraints**: *Pattern*: `^[A-Za-z0-9 .,@:]*$` |
| `record_id` | `uuid\|str` | Optional | ID of the resource that is being changed |
| `record_type` | `str` | Optional | Type of the resource that is being changed<br>**Constraints**: *Pattern*: `^[A-Za-z]*$` |

## Example (as JSON)

```json
{
  "action_time": "03/20/2017 17:13:41",
  "actioned_by": "9a120694-2308-4044-9a6b-b667a9fc3e48",
  "record_id": "e90c3385-e299-4d1c-95f3-fc1075e047a4",
  "record_type": "User",
  "after_data": {
    "key1": "val1",
    "key2": "val2"
  },
  "before_data": {
    "key1": "val1",
    "key2": "val2"
  },
  "description": "description2"
}
```

