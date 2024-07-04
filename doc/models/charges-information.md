
# Charges Information

## Structure

`ChargesInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bearer_code` | `str` | Optional | Specifies which party/parties will bear the charges associated with the processing of the payment transaction. Can be one of the following: `DEBT`, `CRED`, `SHAR` or `SLEV` |
| `receiver_charges_amount` | `str` | Optional | Transaction charges due to the receiver of the transaction. Requires 1 to 2 decimal places. Must be > 0. |
| `receiver_charges_currency` | `str` | Optional | Currency of `receiver_charges_amount`. Currency code as defined in [ISO 4217](http://www.iso.org/iso/home/standards/currency_codes.htm). |
| `sender_charges` | [`List[SenderCharge]`](../../doc/models/sender-charge.md) | Optional | - |

## Example (as JSON)

```json
{
  "bearer_code": "SLEV",
  "receiver_charges_amount": "1.20",
  "receiver_charges_currency": "EUR",
  "sender_charges": [
    {
      "amount": "amount6",
      "currency": "currency4"
    },
    {
      "amount": "amount6",
      "currency": "currency4"
    },
    {
      "amount": "amount6",
      "currency": "currency4"
    }
  ]
}
```

