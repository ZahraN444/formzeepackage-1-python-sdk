
# Sender Charge

List of transaction charges due to the sender of the transaction

## Structure

`SenderCharge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Optional | Amount of each transaction charge due to the sender of the transaction. Requires 1 to 2 decimal places. Must be > 0. |
| `currency` | `str` | Optional | Currency of `amount`. Currency code as defined in [ISO 4217](http://www.iso.org/iso/home/standards/currency_codes.htm). |

## Example (as JSON)

```json
{
  "amount": "2.00",
  "currency": "EUR"
}
```

