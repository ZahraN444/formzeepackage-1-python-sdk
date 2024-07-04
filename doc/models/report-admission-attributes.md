
# Report Admission Attributes

## Structure

`ReportAdmissionAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admission_datetime` | `datetime` | Optional | - |
| `scheme_status_code` | `str` | Optional | - |
| `scheme_status_code_description` | `str` | Optional | - |
| `status` | [`ReportAdmissionStatusEnum`](../../doc/models/report-admission-status-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "admission_datetime": "2016-03-13T12:52:32.123Z",
  "scheme_status_code": "scheme_status_code2",
  "scheme_status_code_description": "scheme_status_code_description0",
  "status": "delivery_confirmed"
}
```

