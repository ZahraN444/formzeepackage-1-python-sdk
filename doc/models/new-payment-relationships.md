
# New Payment Relationships

## Structure

`NewPaymentRelationships`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `beneficiary` | [`Beneficiary`](../../doc/models/beneficiary.md) | Optional | - |
| `beneficiary_account` | [`BeneficiaryAccount`](../../doc/models/beneficiary-account.md) | Optional | - |
| `debtor` | [`Debtor`](../../doc/models/debtor.md) | Optional | - |
| `debtor_account` | [`DebtorAccount`](../../doc/models/debtor-account.md) | Optional | - |
| `forwarded_payment` | [`ForwardedPayment`](../../doc/models/forwarded-payment.md) | Optional | - |
| `fx_deal` | [`FxDeal`](../../doc/models/fx-deal.md) | Optional | - |
| `payment_admission` | [`PaymentAdmission2`](../../doc/models/payment-admission-2.md) | Optional | - |
| `payment_advice` | [`PaymentAdvice1`](../../doc/models/payment-advice-1.md) | Optional | - |
| `payment_recall` | [`PaymentRecall`](../../doc/models/payment-recall.md) | Optional | - |
| `payment_return` | [`PaymentReturn`](../../doc/models/payment-return.md) | Optional | - |
| `payment_reversal` | [`PaymentReversal`](../../doc/models/payment-reversal.md) | Optional | - |
| `payment_submission` | [`PaymentSubmission2`](../../doc/models/payment-submission-2.md) | Optional | - |

## Example (as JSON)

```json
{
  "beneficiary": {
    "data": [
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      }
    ]
  },
  "beneficiary_account": {
    "data": [
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      }
    ]
  },
  "debtor": {
    "data": [
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      }
    ]
  },
  "debtor_account": {
    "data": [
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      }
    ]
  },
  "forwarded_payment": {
    "data": [
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      },
      {
        "id": "00001c2a-0000-0000-0000-000000000000",
        "type": "type0"
      }
    ]
  }
}
```

