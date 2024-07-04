
# Payment Admission Task Update

## Structure

`PaymentAdmissionTaskUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`Attributes53`](../../doc/models/attributes-53.md) | Optional | - |
| `id` | `uuid\|str` | Optional | - |
| `organisation_id` | `uuid\|str` | Optional | Unique ID of the organisation this resource is created by |
| `mtype` | [`Type9Enum`](../../doc/models/type-9-enum.md) | Optional | - |
| `version` | `int` | Optional | Version number<br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "organisation_id": "ee2fb143-6dfe-4787-b183-ca8ddd4164d2",
  "version": 0,
  "attributes": {
    "output": {
      "key1": "val1",
      "key2": "val2"
    },
    "status": "pending"
  },
  "id": "000017b4-0000-0000-0000-000000000000",
  "type": "payment_admission_tasks"
}
```

