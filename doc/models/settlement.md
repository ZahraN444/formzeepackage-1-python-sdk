
# Settlement

Specifies the details on how the settlement of the transaction between the instructing agent and the instructed agent is completed

## Structure

`Settlement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | - |
| `account_number_code` | [`AccountNumberCodeEnum`](../../doc/models/account-number-code-enum.md) | Optional | The type of identification given at `account_number` attribute |
| `bank_id` | `str` | Optional | - |
| `bank_id_code` | [`BankIdCodeEnum`](../../doc/models/bank-id-code-enum.md) | Optional | - |
| `method` | [`MethodEnum`](../../doc/models/method-enum.md) | Optional | Method used to settle the payment instruction. Acceptable Values for SEPA: CLRG. Acceptable Values for SWIFT: INDA (settled by Instructed Agent), INGA (Settled by Instructing Agent), COVE (Cover Payment) |

## Example (as JSON)

```json
{
  "account_number": "12345678",
  "account_number_code": "IBAN",
  "method": "CLRG",
  "bank_id": "bank_id8",
  "bank_id_code": "CHBCC"
}
```

