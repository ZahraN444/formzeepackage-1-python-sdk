
# Report Request Submission Attributes

## Structure

`ReportRequestSubmissionAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_status_code` | `str` | Optional | - |
| `status` | [`ReportRequestSubmissionStatusEnum`](../../doc/models/report-request-submission-status-enum.md) | Required | - |
| `status_reason` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "scheme_status_code": "scheme_status_code6",
  "status": "delivery_confirmed",
  "status_reason": "status_reason4"
}
```

