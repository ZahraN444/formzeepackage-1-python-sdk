
# Account Event Attributes

## Structure

`AccountEventAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `uuid\|str` | Required | ID of the account this event relates to |
| `date_time` | `datetime` | Required | - |
| `description` | [`DescriptionEnum`](../../doc/models/description-enum.md) | Optional | Contains the event description |
| `reason` | `str` | Optional | Failure reason. Should only be present when description is failed |
| `routing_status` | [`RoutingStatusEnum`](../../doc/models/routing-status-enum.md) | Required | Contains the routing status |
| `status` | [`Status2Enum`](../../doc/models/status-2-enum.md) | Required | Contains the event status |

## Example (as JSON)

```json
{
  "account_id": "cfc09fb8-bbca-40bd-a518-6e58d8a9c7f4",
  "date_time": "2016-03-13T12:52:32.123Z",
  "description": "confirmed",
  "reason": "Invalid BIC",
  "routing_status": "routable",
  "status": "confirmed"
}
```

