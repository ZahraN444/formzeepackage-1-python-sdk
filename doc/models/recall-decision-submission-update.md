
# Recall Decision Submission Update

## Structure

`RecallDecisionSubmissionUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`Attributes59`](../../doc/models/attributes-59.md) | Optional | - |
| `id` | `uuid\|str` | Required | Unique resource ID |
| `organisation_id` | `uuid\|str` | Required | Unique ID of the organisation this resource is created by |
| `mtype` | `str` | Optional | Name of the resource type<br>**Constraints**: *Pattern*: `^[A-Za-z_]*$` |
| `version` | `int` | Optional | Version number<br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "id": "7826c3cb-d6fd-41d0-b187-dc23ba928772",
  "organisation_id": "ee2fb143-6dfe-4787-b183-ca8ddd4164d2",
  "type": "recall_decision_submissions",
  "version": 0,
  "attributes": {
    "status": "delivery_confirmed",
    "status_reason": "status_reason6"
  }
}
```

