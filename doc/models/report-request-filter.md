
# Report Request Filter

## Structure

`ReportRequestFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_from` | `date` | Optional | - |
| `date_to` | `date` | Optional | - |
| `report_users` | [`List[ReportUser]`](../../doc/models/report-user.md) | Required | - |

## Example (as JSON)

```json
{
  "report_users": [
    {
      "user_id": "123456",
      "user_id_code": "SUN"
    }
  ],
  "date_from": "2016-03-13",
  "date_to": "2016-03-13"
}
```

