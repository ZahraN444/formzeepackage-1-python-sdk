
# Subscription Update Attributes

## Structure

`SubscriptionUpdateAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `callback_transport` | [`CallbackTransportEnum`](../../doc/models/callback-transport-enum.md) | Optional | - |
| `callback_uri` | `str` | Optional | Deprecated. Please use callback_uris instead<br>**Constraints**: *Pattern*: `^[A-Za-z0-9 .,@:\&\?=\/\-_]*$` |
| `callback_uris` | [`List[CallbackURI]`](../../doc/models/callback-uri.md) | Optional | - |
| `deactivated` | `bool` | Optional | - |
| `event_type` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Za-z_-]*$` |
| `filter` | `str` | Optional | - |
| `record_type` | `str` | Optional | **Constraints**: *Pattern*: `^[A-Za-z_-]*$` |
| `user_defined_data` | [`List[SubscriptionUserDefinedData]`](../../doc/models/subscription-user-defined-data.md) | Optional | All purpose list of key-value pairs to store specific data for the associated subscription.<br>**Constraints**: *Maximum Items*: `5` |
| `user_id` | `uuid\|str` | Optional | - |

## Example (as JSON)

```json
{
  "callback_transport": "http_aws_private",
  "callback_uri": "callback_uri6",
  "callback_uris": [
    {
      "callback_transport": "queue",
      "callback_uri": "callback_uri4"
    },
    {
      "callback_transport": "queue",
      "callback_uri": "callback_uri4"
    },
    {
      "callback_transport": "queue",
      "callback_uri": "callback_uri4"
    }
  ],
  "deactivated": false,
  "event_type": "event_type2"
}
```

