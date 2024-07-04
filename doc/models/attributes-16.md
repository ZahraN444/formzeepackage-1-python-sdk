
# Attributes 16

## Structure

`Attributes16`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `clearing_system` | `str` | Optional | Clearing infrastructure through which the payment instruction was processed<br>**Constraints**: *Pattern*: `^[0-9A-Za-z_]*$` |
| `file_identifier` | `str` | Optional | Identification code of the file sent to scheme.<br>**Constraints**: *Pattern*: `^[0-9a-zA-Z]+$` |
| `file_number` | `str` | Optional | Number of the file sent to scheme.<br>**Constraints**: *Pattern*: `^[0-9]+$` |
| `limit_breach_end_datetime` | `datetime` | Optional | Time a payment was released from being held due to a limit breach |
| `limit_breach_start_datetime` | `datetime` | Optional | Start time a payment was held due to a limit breach |
| `redirected_account_number` | `str` | Optional | Details of the account to which funds are redirected (if applicable) |
| `redirected_bank_id` | `str` | Optional | Details of the bank to which funds are redirected (if applicable) |
| `route` | [`RouteEnum`](../../doc/models/route-enum.md) | Optional | Route taken for an outbound payment |
| `scheme_status_code` | `str` | Optional | Scheme-specific status (if submission has been submitted to a scheme) |
| `scheme_status_code_description` | `str` | Optional | [Description](http://api-docs.form3.tech/api.html#enumerations-scheme-status-codes-for-bacs) of `scheme_status_code` |
| `settlement_cycle` | `int` | Optional | Cycle in which the payment will be settled<br>**Constraints**: `>= 0` |
| `settlement_date` | `date` | Optional | Date that the payment will be settled |
| `status` | [`PaymentSubmissionStatusEnum`](../../doc/models/payment-submission-status-enum.md) | Optional | [Status of the submission](https://api-docs.form3.tech/api.html#enumerations-payment-status-codes-submission-status) |
| `status_reason` | `str` | Optional | Description of the submission status |
| `submission_datetime` | `datetime` | Optional | Date of the submission |
| `transaction_start_datetime` | `datetime` | Optional | Time the request was received by Form3. Used to compute the total transaction time of a payment. |

## Example (as JSON)

```json
{
  "clearing_system": "TIPS",
  "file_identifier": "123456",
  "file_number": "001",
  "limit_breach_end_datetime": "03/12/2018 14:11:55",
  "limit_breach_start_datetime": "03/12/2018 14:11:50",
  "redirected_account_number": "12345678",
  "redirected_bank_id": "400300",
  "scheme_status_code": "0000",
  "scheme_status_code_description": "Field 1 (destination sorting code) was invalid",
  "settlement_cycle": 1,
  "settlement_date": "2017-07-23",
  "status": "delivery_confirmed",
  "status_reason": "Accepted without qualification",
  "submission_datetime": "03/12/2018 14:11:48",
  "transaction_start_datetime": "03/12/2018 14:11:49"
}
```

