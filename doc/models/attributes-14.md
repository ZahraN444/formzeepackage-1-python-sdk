
# Attributes 14

## Structure

`Attributes14`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_status_code` | `str` | Optional | Scheme-specific status code. Refer to scheme documentation where available. |
| `scheme_status_code_description` | `str` | Optional | Description of `scheme_status_code` |
| `source_gateway` | `str` | Optional | - |
| `status` | [`ReversalAdmissionStatusEnum`](../../doc/models/reversal-admission-status-enum.md) | Optional | Status of the reversal admission |

## Example (as JSON)

```json
{
  "scheme_status_code": "0",
  "scheme_status_code_description": "Field 1 (destination sorting code) was invalid",
  "status": "confirmed",
  "source_gateway": "source_gateway2"
}
```

