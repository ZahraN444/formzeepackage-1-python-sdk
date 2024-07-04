
# Links

## Structure

`Links`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | `str` | Optional | Link to the first resource in the list |
| `last` | `str` | Optional | Link to the last resource in the list |
| `next` | `str` | Optional | Link to the next resource in the list |
| `prev` | `str` | Optional | Link to the previous resource in the list |
| `mself` | `str` | Required | Link to this resource type |

## Example (as JSON)

```json
{
  "first": "https://api.test.form3.tech/v1/api_name/resource_type",
  "last": "https://api.test.form3.tech/v1/api_name/resource_type",
  "next": "https://api.test.form3.tech/v1/api_name/resource_type",
  "prev": "https://api.test.form3.tech/v1/api_name/resource_type",
  "self": "https://api.test.form3.tech/v1/api_name/resource_type"
}
```

