
# Payment Type Information

Set of elements used to further specify the type of transaction.

## Structure

`PaymentTypeInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Optional | Amount of money to be moved between the debtor and creditor, before deduction of charges.<br>**Constraints**: *Pattern*: `^[0-9.]{0,14}$` |
| `category_purpose` | `str` | Optional | Specifies the high level purpose of the instruction based on a set of pre-defined categories.<br>**Constraints**: *Maximum Length*: `35` |
| `currency` | `str` | Optional | Currency of the transaction amount. Currency code as defined in [ISO 4217](https://www.iso.org/iso/home/standards/currency_codes.htm)<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `payment_purpose` | `str` | Optional | Underlying reason for the payment transaction. Defined in external code list (4 char) or proprietary code (35 char)<br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `35` |
| `processing_date` | `date` | Optional | Date on which the amount of money ceases to be available to the agent that owes it and when the amount of money becomes available to the agent to which it is due. |
| `remittance_information` | `str` | Optional | Unstructured information supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle.<br>**Constraints**: *Maximum Length*: `140` |
| `scheme_payment_sub_type` | `str` | Optional | Specifies a local instrument to further qualify the level of service.<br>**Constraints**: *Maximum Length*: `35` |
| `scheme_payment_type` | `str` | Optional | Specifies a pre-agreed level of service as published in an external code list (4 char) or a proprietary code (35 char).<br>**Constraints**: *Maximum Length*: `35` |

## Example (as JSON)

```json
{
  "processing_date": "2015-12-23",
  "amount": "amount2",
  "category_purpose": "category_purpose4",
  "currency": "currency0",
  "payment_purpose": "payment_purpose6"
}
```

