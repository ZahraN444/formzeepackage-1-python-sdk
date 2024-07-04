
# Attributes 9

## Structure

`Attributes9`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admission_datetime` | `datetime` | Optional | Date and time the payment admission was created |
| `route` | [`Route1Enum`](../../doc/models/route-1-enum.md) | Optional | Route taken for a return |
| `scheme_status_code` | `str` | Optional | Refer to individual scheme where applicable |
| `scheme_status_code_description` | `str` | Optional | [Description](http://api-docs.form3.tech/api.html#enumerations-scheme-status-codes-for-bacs) of `scheme_status_code` |
| `settlement_cycle` | `int` | Optional | Cycle in which the payment will be settled<br>**Constraints**: `>= 0` |
| `settlement_date` | `date` | Optional | Date on which the payment will be settled |
| `status` | [`ReturnAdmissionStatusEnum`](../../doc/models/return-admission-status-enum.md) | Optional | [Status](http://draft-api-docs.form3.tech/api.html#enumerations-payment-admission-status) of the return admission |
| `status_reason` | `str` | Optional | Further explanation of the status. [See here](http://api-docs.form3.tech/api.html#enumerations-payment-admission-status-reasons) for possible values. |
| `unique_scheme_id` | `str` | Optional | Scheme-specific unique ID (42 character string) |

## Example (as JSON)

```json
{
  "admission_datetime": "09/28/2017 14:21:46",
  "scheme_status_code": "1001",
  "scheme_status_code_description": "Field 1 (destination sorting code) was invalid",
  "settlement_cycle": 1,
  "settlement_date": "2017-01-14",
  "status": "confirmed",
  "status_reason": "Account data invalid",
  "route": "on_us"
}
```

