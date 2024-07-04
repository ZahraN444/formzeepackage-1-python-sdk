
# Correction Transaction Information

References a transaction initiated to fix the case under investigation.

## Structure

`CorrectionTransactionInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Optional | Amount of money moved between the instructing agent and the instructed agent.<br>**Constraints**: *Pattern*: `^[0-9.]{0,14}$` |
| `currency` | `str` | Optional | Currency of the transaction amount. Currency code as defined in [ISO 4217](https://www.iso.org/iso/home/standards/currency_codes.htm)<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `end_to_end_reference` | `str` | Optional | Unique identification, as assigned by the initiating party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.<br>**Constraints**: *Maximum Length*: `35` |
| `instruction_id` | `str` | Optional | Unique identification, as assigned by an instructing party for an instructed party, to unambiguously identify the instruction.<br>**Constraints**: *Maximum Length*: `35` |
| `processing_date` | `date` | Optional | Date on which the amount of money ceases to be available to the agent that owes it and when the amount of money becomes available to the agent to which it is due. |
| `references` | [`List[QueryReference]`](../../doc/models/query-reference.md) | Optional | Reference for the corrective payment for this query case. |
| `scheme_transaction_id` | `str` | Optional | Unique identification, as assigned by the first instructing agent, to unambiguously identify the transaction that is passed on, unchanged, throughout the entire interbank chain.<br>**Constraints**: *Maximum Length*: `35` |
| `unique_scheme_id` | `str` | Optional | The scheme-specific unique transaction ID to unambiguously identify the message. Populated by the scheme.<br>**Constraints**: *Maximum Length*: `35` |

## Example (as JSON)

```json
{
  "processing_date": "2015-12-23",
  "amount": "amount6",
  "currency": "currency4",
  "end_to_end_reference": "end_to_end_reference0",
  "instruction_id": "instruction_id8"
}
```

