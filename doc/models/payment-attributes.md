
# Payment Attributes

## Structure

`PaymentAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agents` | [`List[Agent]`](../../doc/models/agent.md) | Optional | Block to represent a Financial Institution/agent in the payment chain |
| `amount` | `str` | Optional | Amount of money moved between the instructing agent and instructed agent<br>**Constraints**: *Pattern*: `^[0-9.]{0,20}$` |
| `batch_booking_indicator` | `str` | Optional | - |
| `batch_id` | `str` | Optional | - |
| `batch_type` | `str` | Optional | - |
| `beneficiary_party` | [`BeneficiaryParty1`](../../doc/models/beneficiary-party-1.md) | Optional | - |
| `category_purpose` | `str` | Optional | Category purpose in proprietary form. Specifies the high level purpose of the instruction. Cannot be used at the same time as `category_purpose_coded`. |
| `category_purpose_coded` | `str` | Optional | Category purpose in a coded form. Specifies the high level purpose of the instruction. Cannot be used at the same time as `category_purpose`. |
| `charges_information` | [`ChargesInformation`](../../doc/models/charges-information.md) | Optional | - |
| `clearing_id` | `str` | Optional | Unique identifier for organisations collecting payments |
| `currency` | `str` | Optional | Currency of the transaction amount. Currency code as defined in [ISO 4217](http://www.iso.org/iso/home/standards/currency_codes.htm) |
| `debtor_party` | [`DebtorParty`](../../doc/models/debtor-party.md) | Optional | - |
| `end_to_end_reference` | `str` | Optional | Unique identification, as assigned by the initiating party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain. |
| `file_number` | `str` | Optional | - |
| `fx` | [`Fx`](../../doc/models/fx.md) | Optional | - |
| `instruction_id` | `str` | Optional | Unique identification, as assigned by the initiating party to unambiguously identify the transaction. This identification is an point-to-point reference and is passed on, unchanged, throughout the entire chain. Cannot include leading, trailing or internal spaces. |
| `intermediary_bank` | [`IntermediaryBankAccountHoldingEntity`](../../doc/models/intermediary-bank-account-holding-entity.md) | Optional | - |
| `numeric_reference` | `str` | Optional | Numeric reference field, see scheme specific descriptions for usage |
| `payment_acceptance_datetime` | `datetime` | Optional | Timestamp of when the payment instruction meets the set processing conditions. Format: YYYY-MM-DDThh:mm:ss:mmm+hh:mm |
| `payment_purpose` | `str` | Optional | Purpose of the payment in a proprietary form |
| `payment_purpose_coded` | `str` | Optional | Purpose of the payment in a coded form |
| `payment_scheme` | `str` | Optional | Clearing infrastructure through which the payment instruction is to be processed. Default for given organisation ID is used if left empty. Has to be a valid [scheme identifier](http://draft-api-docs.form3.tech/api.html#enumerations-schemes).<br>**Constraints**: *Pattern*: `^[A-Za-z_]*$` |
| `payment_type` | `str` | Optional | - |
| `processing_date` | `date` | Optional | Date on which the payment is to be debited from the debtor account. Formatted according to ISO 8601 format: YYYY-MM-DD. |
| `receivers_correspondent` | [`ReceiversCorrespondentAccountHoldingEntity`](../../doc/models/receivers-correspondent-account-holding-entity.md) | Optional | - |
| `reference` | `str` | Optional | Payment reference for beneficiary use |
| `references` | [`List[Reference]`](../../doc/models/reference.md) | Optional | Block to represent a list of references |
| `regulatory_reporting` | `str` | Optional | Regulatory reporting information |
| `reimbursement` | [`ReimbursementAccountHoldingEntity`](../../doc/models/reimbursement-account-holding-entity.md) | Optional | - |
| `remittance_information` | `str` | Optional | Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts receivable system provided by the debtor for the beneficiary. |
| `scheme_payment_sub_type` | `str` | Optional | The scheme specific payment [sub type](http://api-docs.form3.tech/api.html#enumerations-scheme-specific-payment-sub-types) |
| `scheme_payment_type` | `str` | Optional | The [scheme-specific payment type](#enumerations-scheme-payment-types) |
| `scheme_processing_date` | `date` | Optional | Date on which the payment is processed by the scheme. Only used if different from `processing_date`. |
| `scheme_transaction_id` | `str` | Optional | Unique identification, as assigned by the first instructing agent, to unambiguously identify the transaction that is passed on, unchanged, throughout the entire interbank chain. |
| `senders_correspondent` | [`SendersCorrespondentAccountHoldingEntity`](../../doc/models/senders-correspondent-account-holding-entity.md) | Optional | - |
| `settlement` | [`Settlement`](../../doc/models/settlement.md) | Optional | Specifies the details on how the settlement of the transaction between the instructing agent and the instructed agent is completed |
| `structured_reference` | [`StructuredReference`](../../doc/models/structured-reference.md) | Optional | - |
| `swift` | [`Swift`](../../doc/models/swift.md) | Optional | - |
| `ultimate_beneficiary` | [`UltimateEntity`](../../doc/models/ultimate-entity.md) | Optional | - |
| `ultimate_debtor` | [`UltimateEntity`](../../doc/models/ultimate-entity.md) | Optional | - |
| `unique_scheme_id` | `str` | Optional | The scheme-specific unique transaction ID. Populated by the scheme. |
| `user_defined_data` | [`List[UserDefinedData]`](../../doc/models/user-defined-data.md) | Optional | All purpose list of key-value pairs specific data stored on the payment.<br>**Constraints**: *Maximum Items*: `5` |

## Example (as JSON)

```json
{
  "amount": "10.00",
  "currency": "EUR",
  "end_to_end_reference": "PAYMENT REF: 20094",
  "instruction_id": "ID1245799",
  "payment_acceptance_datetime": "09/30/2017 12:36:02",
  "payment_purpose": "X",
  "payment_scheme": "FPS",
  "processing_date": "2015-02-12",
  "reference": "rent for oct",
  "regulatory_reporting": "May be required for some foreign originated payments",
  "remittance_information": "Additional remittance information over and above reference information",
  "scheme_payment_sub_type": "TelephoneBanking",
  "scheme_payment_type": "ImmediatePayment",
  "scheme_processing_date": "2015-02-12",
  "scheme_transaction_id": "123456789012345678",
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
    }
  ],
  "batch_booking_indicator": "batch_booking_indicator8",
  "batch_id": "batch_id2",
  "batch_type": "batch_type4"
}
```

