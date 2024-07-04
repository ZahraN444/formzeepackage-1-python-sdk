
# Query Reference

Arbitrary references for payment or case. Defined by a pair of reference type and reference value.

## Structure

`QueryReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Name of the reference type<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `45` |
| `value` | `str` | Required | Value of the provided reference type<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `45` |

## Example (as JSON)

```json
{
  "type": "UETR",
  "value": "value6"
}
```

