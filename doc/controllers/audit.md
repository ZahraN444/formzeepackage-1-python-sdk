# Audit

```python
audit_controller = client.audit
```

## Class Name

`AuditController`

## Methods

* [List Audit Entries for This Record Type](../../doc/controllers/audit.md#list-audit-entries-for-this-record-type)
* [Fetch Audit Entry List for This Record Type Id](../../doc/controllers/audit.md#fetch-audit-entry-list-for-this-record-type-id)


# List Audit Entries for This Record Type

List audit entries for this record type

```python
def list_audit_entries_for_this_record_type(self,
                                           record_type,
                                           page_number=None,
                                           page_size=None,
                                           page_after=None,
                                           filter_organisation_id=None,
                                           filter_action_time_from=None,
                                           filter_action_time_to=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `record_type` | `str` | Template, Required | Record Type |
| `page_number` | `int` | Query, Optional | Which page to select |
| `page_size` | `int` | Query, Optional | Number of items to select |
| `page_after` | `str` | Query, Optional | Cursor for next page (this is a base64-encoded UUID continuation token returned from the application and should not be manually generated) |
| `filter_organisation_id` | `List[uuid\|str]` | Query, Optional | Filter by organisation id |
| `filter_action_time_from` | `datetime` | Query, Optional | - |
| `filter_action_time_to` | `datetime` | Query, Optional | - |

## Response Type

[`AuditEntryListResponse`](../../doc/models/audit-entry-list-response.md)

## Example Usage

```python
record_type = 'record_type6'

Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = audit_controller.list_audit_entries_for_this_record_type(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')record_type)
print(result)
```


# Fetch Audit Entry List for This Record Type Id

Fetch audit entry list for this record type/id

```python
def fetch_audit_entry_list_for_this_record_type_id(self,
                                                  record_type,
                                                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `record_type` | `str` | Template, Required | Record Type |
| `id` | `uuid\|str` | Template, Required | Record Id |

## Response Type

[`AuditEntryListResponse`](../../doc/models/audit-entry-list-response.md)

## Example Usage

```python
record_type = 'record_type6'

id = '00001770-0000-0000-0000-000000000000'

result = audit_controller.fetch_audit_entry_list_for_this_record_type_id(
    record_type,
    id
)
print(result)
```

