
# Attributes 26

## Structure

`Attributes26`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admission_datetime` | `datetime` | Optional | - |
| `source_gateway` | `str` | Optional | - |
| `status` | [`DirectDebitDecisionAdmissionStatusEnum`](../../doc/models/direct-debit-decision-admission-status-enum.md) | Optional | - |
| `status_reason` | [`DirectDebitDecisionAdmissionStatusReasonEnum`](../../doc/models/direct-debit-decision-admission-status-reason-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "admission_datetime": "2016-03-13T12:52:32.123Z",
  "source_gateway": "source_gateway2",
  "status": "failed",
  "status_reason": "invalid_beneficiary_details"
}
```

