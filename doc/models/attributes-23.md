
# Attributes 23

## Structure

`Attributes23`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Optional | Amount of money moved between the instructing agent and instructed agent<br>**Constraints**: *Pattern*: `^[0-9.]{0,20}$` |
| `beneficiary_party` | [`BeneficiaryParty3`](../../doc/models/beneficiary-party-3.md) | Optional | - |
| `category_purpose` | `str` | Optional | Category purpose in proprietary form. Specifies the high level purpose of the instruction. Cannot be used at the same time as `category_purpose_coded`. |
| `category_purpose_coded` | `str` | Optional | Category purpose in a coded form. Specifies the high level purpose of the instruction. Cannot be used at the same time as `category_purpose`. |
| `clearing_id` | `str` | Optional | Unique identifier for organisations collecting payments |
| `currency` | `str` | Optional | Currency of the transaction amount. Currency code as defined in [ISO 4217](http://www.iso.org/iso/home/standards/currency_codes.htm) |
| `debtor_party` | [`DebtorParty2`](../../doc/models/debtor-party-2.md) | Optional | - |
| `end_to_end_reference` | `str` | Optional | Unique identification, as assigned by the initiating party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain. |
| `instruction_id` | `str` | Optional | Unique identification, as assigned by the initiating party to unambiguously identify the transaction. This identification is an point-to-point reference and is passed on, unchanged, throughout the entire chain. Cannot include leading, trailing or internal spaces. |
| `mandate_amendment_indicator` | `bool` | Optional | Indicator notifying whether the underlying mandate is amended or not |
| `mandate_id` | `str` | Optional | Original mandate id. |
| `mandate_signature_date` | `date` | Optional | Date on which the direct debit mandate has been signed by the debtor. |
| `numeric_reference` | `str` | Optional | Numeric reference field, see scheme specific descriptions for usage |
| `payment_purpose_coded` | `str` | Optional | Purpose of the direct debit in a coded form |
| `payment_scheme` | `str` | Optional | Clearing infrastructure through which the operation instruction is to be processed. Default for given organisation ID is used if left empty. Has to be a valid [scheme identifier](http://draft-api-docs.form3.tech/api.html#enumerations-schemes). |
| `processing_date` | `date` | Optional | Date on which the operation is to be debited from the debtor account. Formatted according to ISO 8601 format: YYYY-MM-DD. |
| `reference` | `str` | Optional | Payment reference for beneficiary use |
| `remittance_information` | `str` | Optional | Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts receivable system provided by the debtor for the beneficiary. |
| `scheme_payment_type` | `str` | Optional | The [scheme-specific payment type](#enumerations-scheme-payment-types) |
| `scheme_processing_date` | `date` | Optional | Date on which the operation is processed by the scheme. Formatted according to ISO 8601 format: YYYY-MM-DD. Only used if different from `processing_date`. |
| `scheme_status` | [`SchemeStatusEnum`](../../doc/models/scheme-status-enum.md) | Optional | This reference is used by the receiving party to identify whether the related DDI would have been electronic (AUDDIS) or paper‐based. |
| `scheme_transaction_id` | `str` | Optional | Unique identification, as assigned by the first instructing agent, to unambiguously identify the transaction that is passed on, unchanged, throughout the entire interbank chain. |
| `settlement` | [`Settlement`](../../doc/models/settlement.md) | Optional | Specifies the details on how the settlement of the transaction between the instructing agent and the instructed agent is completed |
| `structured_reference` | [`StructuredReference`](../../doc/models/structured-reference.md) | Optional | - |
| `ultimate_beneficiary` | [`UltimateEntity`](../../doc/models/ultimate-entity.md) | Optional | - |
| `ultimate_debtor` | [`UltimateEntity`](../../doc/models/ultimate-entity.md) | Optional | - |
| `unique_scheme_id` | `str` | Optional | The scheme-specific unique transaction ID. Populated by the scheme. |

## Example (as JSON)

```json
{
  "amount": "10.00",
  "clearing_id": "123456",
  "currency": "EUR",
  "end_to_end_reference": "PAYMENT REF: 20094",
  "instruction_id": "ID1245799",
  "mandate_signature_date": "2017-07-23",
  "payment_scheme": "BACS",
  "processing_date": "2015-02-12",
  "reference": "rent for oct",
  "remittance_information": "Additional remittance information over and above reference information",
  "scheme_payment_type": "DirectDebitFirst",
  "scheme_processing_date": "2015-02-12",
  "scheme_status": "AUDDIS",
  "scheme_transaction_id": "123456789012345678",
  "unique_scheme_id": "L5W48NDWYW7JV9MRO71020180301826040011",
  "beneficiary_party": {
    "account_name": "account_name0",
    "account_number": "account_number8",
    "account_number_code": "IBAN",
    "account_type": 6,
    "account_with": {
      "bank_address": [
        "bank_address4",
        "bank_address3",
        "bank_address2"
      ],
      "bank_id": "bank_id2",
      "bank_id_code": "PLKNR",
      "bank_ids": [
        {
          "bank_id": "bank_id4",
          "bank_id_code": "bank_id_code8"
        },
        {
          "bank_id": "bank_id4",
          "bank_id_code": "bank_id_code8"
        }
      ],
      "bank_name": "bank_name4",
      "bank_party_id": "bank_party_id6"
    }
  },
  "category_purpose": "category_purpose6",
  "category_purpose_coded": "category_purpose_coded2"
}
```

