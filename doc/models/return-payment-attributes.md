
# Return Payment Attributes

## Structure

`ReturnPaymentAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agents` | [`List[Agent]`](../../doc/models/agent.md) | Optional | Block to represent a Financial Institution/agent in the payment chain |
| `amount` | `str` | Optional | The amount to return which should correspond to the amount of the original payment<br>**Constraints**: *Pattern*: `^[0-9.]{0,20}$` |
| `clearing_id` | `str` | Optional | Unique identifier for organisations collecting payments |
| `currency` | `str` | Optional | ISO currency code for transaction amount |
| `limit_breach_end_datetime` | `datetime` | Optional | Time a payment was released from being held due to a limit breach |
| `limit_breach_start_datetime` | `datetime` | Optional | Start time a payment was held due to a limit breach |
| `reason` | `str` | Optional | - |
| `return_code` | `str` | Optional | The return [reason code](http://draft-api-docs.form3.tech/api.html#enumerations-payment-return-codes) |
| `scheme_transaction_id` | `str` | Optional | A unique reference to the return payment instruction. If not supplied, the value is generated by Form3. |
| `settlement` | [`Settlement`](../../doc/models/settlement.md) | Optional | Specifies the details on how the settlement of the transaction between the instructing agent and the instructed agent is completed |
| `unique_scheme_id` | `str` | Optional | The scheme-specific unique transaction ID. Populated by the scheme.<br>**Constraints**: *Maximum Length*: `42` |
| `user_defined_data` | [`List[UserDefinedData]`](../../doc/models/user-defined-data.md) | Optional | All purpose list of key-value pairs specific data stored on the return.<br>**Constraints**: *Maximum Items*: `5` |

## Example (as JSON)

```json
{
  "amount": "200.00",
  "currency": "GBP",
  "limit_breach_end_datetime": "03/12/2018 14:11:55",
  "limit_breach_start_datetime": "03/12/2018 14:11:50",
  "return_code": "00000002",
  "scheme_transaction_id": "e368ab2d",
  "unique_scheme_id": "L5W48NDWYW7JV9MRO71020180301826040011",
  "agents": [
    {
      "account_number": "account_number0",
      "account_number_code": "IBAN",
      "address": [
        "address4",
        "address5"
      ],
      "identification": {
        "bank_id": "bank_id4",
        "bank_id_code": "bank_id_code2",
        "bank_ids": [
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          }
        ]
      },
      "name": "name0"
    },
    {
      "account_number": "account_number0",
      "account_number_code": "IBAN",
      "address": [
        "address4",
        "address5"
      ],
      "identification": {
        "bank_id": "bank_id4",
        "bank_id_code": "bank_id_code2",
        "bank_ids": [
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          }
        ]
      },
      "name": "name0"
    },
    {
      "account_number": "account_number0",
      "account_number_code": "IBAN",
      "address": [
        "address4",
        "address5"
      ],
      "identification": {
        "bank_id": "bank_id4",
        "bank_id_code": "bank_id_code2",
        "bank_ids": [
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          },
          {
            "bank_id": "bank_id4",
            "bank_id_code": "bank_id_code8"
          }
        ]
      },
      "name": "name0"
    }
  ],
  "clearing_id": "clearing_id0"
}
```

