# Subscriptions

```python
subscriptions_controller = client.subscriptions
```

## Class Name

`SubscriptionsController`

## Methods

* [List Subscriptions](../../doc/controllers/subscriptions.md#list-subscriptions)
* [Create Subscription](../../doc/controllers/subscriptions.md#create-subscription)
* [Delete Subscription](../../doc/controllers/subscriptions.md#delete-subscription)
* [Fetch Subscription](../../doc/controllers/subscriptions.md#fetch-subscription)
* [Patch Subscription](../../doc/controllers/subscriptions.md#patch-subscription)


# List Subscriptions

List all subscriptions

```python
def list_subscriptions(self,
                      page_number=None,
                      page_size=None,
                      filter_event_type=None,
                      filter_record_type=None,
                      filter_organisation_id=None,
                      filter_deactivated=None,
                      filter_callback_transport=None,
                      filter_callback_uri_search_term=None,
                      filter_notification_filter=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_number` | `str` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `filter_event_type` | `List[str]` | Query, Optional | Filter by event type |
| `filter_record_type` | `List[str]` | Query, Optional | Filter by record type |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_deactivated` | `bool` | Query, Optional | Filter by deactivated |
| `filter_callback_transport` | `str` | Query, Optional | Filter by callback_transport |
| `filter_callback_uri_search_term` | `str` | Query, Optional | Filter on callback_uri containing a search term |
| `filter_notification_filter` | `bool` | Query, Optional | Filter by existence of notification filters |

## Response Type

[`SubscriptionDetailsListResponse`](../../doc/models/subscription-details-list-response.md)

## Example Usage

```python
Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = subscriptions_controller.list_subscriptions(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key'))
print(result)
```


# Create Subscription

Create subscription

```python
def create_subscription(self,
                       subscription_creation_request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_creation_request` | [`SubscriptionCreation`](../../doc/models/subscription-creation.md) | Body, Required | - |

## Response Type

[`SubscriptionCreationResponse`](../../doc/models/subscription-creation-response.md)

## Example Usage

```python
subscription_creation_request = SubscriptionCreation(
    data=Subscription(
        attributes=SubscriptionAttributes(
            event_type='event_type4',
            record_type='record_type8'
        ),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='subscriptions',
        version=0
    )
)

result = subscriptions_controller.create_subscription(subscription_creation_request)
print(result)
```


# Delete Subscription

Deletes a subscription

```python
def delete_subscription(self,
                       id,
                       version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Subscription Id |
| `version` | `int` | Query, Required | Version |

## Response Type

`void`

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

version = 172

result = subscriptions_controller.delete_subscription(
    id,
    version
)
print(result)
```


# Fetch Subscription

Fetch subscription

```python
def fetch_subscription(self,
                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Subscription Id |

## Response Type

[`SubscriptionDetailsResponse`](../../doc/models/subscription-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = subscriptions_controller.fetch_subscription(id)
print(result)
```


# Patch Subscription

Update subscription details

```python
def patch_subscription(self,
                      id,
                      subscription_update_request=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Template, Required | Subscription Id |
| `subscription_update_request` | [`SubscriptionAmendment`](../../doc/models/subscription-amendment.md) | Body, Optional | - |

## Response Type

[`SubscriptionDetailsResponse`](../../doc/models/subscription-details-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

subscription_update_request = SubscriptionAmendment(
    data=SubscriptionUpdate(
        attributes=SubscriptionUpdateAttributes(),
        id='7826c3cb-d6fd-41d0-b187-dc23ba928772',
        organisation_id='ee2fb143-6dfe-4787-b183-ca8ddd4164d2',
        mtype='subscriptions',
        version=0
    )
)

result = subscriptions_controller.patch_subscription(
    id,
    subscription_update_request=subscription_update_request
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 404 | Not Found | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 409 | Conflict | [`ApiErrorException`](../../doc/models/api-error-exception.md) |
| 500 | Internal Error | [`ApiErrorException`](../../doc/models/api-error-exception.md) |

