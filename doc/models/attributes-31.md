
# Attributes 31

## Structure

`Attributes31`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charges_amount` | [`CurrencyAndAmount`](../../doc/models/currency-and-amount.md) | Optional | - |
| `clearing_id` | `str` | Optional | Unique identifier for organisations collecting payments |
| `compensation_amount` | [`CurrencyAndAmount`](../../doc/models/currency-and-amount.md) | Optional | - |
| `processing_date` | `date` | Optional | Date on which the operation is to be debited from the debtor account. Formatted according to ISO 8601 format: YYYY-MM-DD. |
| `return_amount` | [`CurrencyAndAmount`](../../doc/models/currency-and-amount.md) | Optional | - |
| `return_code` | `str` | Optional | - |
| `return_initiator` | [`ReturnInitiatorEnum`](../../doc/models/return-initiator-enum.md) | Optional | - |
| `scheme_processing_date` | `date` | Optional | Date on which the operation is processed by the scheme. Formatted according to ISO 8601 format: YYYY-MM-DD. Only used if different from `processing_date`. |
| `scheme_transaction_id` | `str` | Optional | - |
| `settlement` | [`Settlement`](../../doc/models/settlement.md) | Optional | Specifies the details on how the settlement of the transaction between the instructing agent and the instructed agent is completed |

## Example (as JSON)

```json
{
  "clearing_id": "123456",
  "processing_date": "2015-02-12",
  "scheme_processing_date": "2015-02-12",
  "charges_amount": {
    "amount": "amount4",
    "currency": "currency2"
  },
  "compensation_amount": {
    "amount": "amount4",
    "currency": "currency2"
  },
  "return_amount": {
    "amount": "amount6",
    "currency": "currency4"
  }
}
```

