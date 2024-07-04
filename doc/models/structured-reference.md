
# Structured Reference

## Structure

`StructuredReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `issuer` | `str` | Optional | Issuer of remittance reference |
| `reference` | `str` | Optional | Unique reference to unambiguously refer to the payment originated by the creditor, this reference enables reconciliation by the creditor upon receipt of the amount of money. |

## Example (as JSON)

```json
{
  "issuer": "issuer8",
  "reference": "reference4"
}
```
