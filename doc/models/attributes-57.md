
# Attributes 57

## Structure

`Attributes57`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agents` | [`List[Agent]`](../../doc/models/agent.md) | Optional | Block to represent a Financial Institution/agent in the payment chain |
| `answer` | [`RecallDecisionAnswerEnum`](../../doc/models/recall-decision-answer-enum.md) | Optional | Answer to the recall request. Can either be `accepted` or `rejected`. |
| `charges_amount` | [`CurrencyAndAmount`](../../doc/models/currency-and-amount.md) | Optional | - |
| `reason` | `str` | Optional | Optional free text reason in addition to `reason_code` |
| `reason_code` | `str` | Optional | Reason for a rejected decision. Required when answer is rejected, ignored otherwise. Has to be a valid [rejected recall decision reason code](http://api-docs.form3.tech/api.html#enumerations-rejected-recall-decision-reason-codes) |
| `recall_amount` | [`CurrencyAndAmount`](../../doc/models/currency-and-amount.md) | Optional | - |
| `resolution_related_information` | [`ResolutionRelatedInformation`](../../doc/models/resolution-related-information.md) | Optional | - |

## Example (as JSON)

```json
{
  "answer": "accepted",
  "reason": "Closed account number",
  "reason_code": "AC04",
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
  "charges_amount": {
    "amount": "amount4",
    "currency": "currency2"
  }
}
```

