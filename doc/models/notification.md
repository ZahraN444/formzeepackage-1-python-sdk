
# Notification

## Structure

`Notification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_time` | `str` | Optional | Timestamp when the event that triggered the notification occurred. |
| `actioned_by` | `uuid\|str` | Optional | The ID of the user that made the change that triggered this notification. This can be the user ID of a customer or a Form3 system user. |
| `data` | `object` | Optional | The full resource itself (as you would see from a GET request) |
| `data_record_type` | `str` | Optional | Internal representation of the record type. Field values are subject to frequent change, evaluation of this field is discouraged.<br>**Constraints**: *Pattern*: `^[A-Za-z]*$` |
| `event_type` | `str` | Optional | The type of event<br>**Constraints**: *Pattern*: `^[a-z]*$` |
| `id` | `uuid\|str` | Optional | Unique resource ID |
| `organisation_id` | `uuid\|str` | Optional | Unique ID of the organisation this resource is created by |
| `record_type` | `str` | Optional | The type of resource contained in `data`<br>**Constraints**: *Pattern*: `^[A-Za-z]*$` |
| `version` | `int` | Optional | Version number<br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "action_time": "08/02/2019 12:35:57",
  "actioned_by": "f1b78f08-785a-4638-ad3c-236aec7ee038",
  "data_record_type": "PaymentAdmission",
  "event_type": "created",
  "id": "e1fa2883-940a-44d5-88af-e1a62123c67a",
  "organisation_id": "ee2fb143-6dfe-4787-b183-ca8ddd4164d2",
  "version": 0,
  "data": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

