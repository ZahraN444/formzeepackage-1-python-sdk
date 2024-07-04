
# Attributes 40

## Structure

`Attributes40`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admission_datetime` | `datetime` | Optional | Time when the Form3 system begins processing of the admission |
| `start_datetime` | `datetime` | Optional | Time the admission request was received by Form3. Used to compute the total processing time |
| `status` | [`SchemeFileAdmissionStatusEnum`](../../doc/models/scheme-file-admission-status-enum.md) | Optional | Status of the scheme file admission |
| `status_reason` | `str` | Optional | Plain-text description of the status attribute |

## Example (as JSON)

```json
{
  "admission_datetime": "03/13/2019 14:48:29",
  "start_datetime": "03/13/2019 14:48:29",
  "status": "confirmed",
  "status_reason": "accepted"
}
```

