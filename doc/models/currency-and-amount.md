
# Currency and Amount

## Structure

`CurrencyAndAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Optional | **Constraints**: *Pattern*: `^[0-9.]{0,20}$` |
| `currency` | `str` | Optional | ISO currency code for `amount` |

## Example (as JSON)

```json
{
  "amount": "10.00",
  "currency": "currency0"
}
```

