
# Transaction File Submission

## Structure

`TransactionFileSubmission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attributes` | [`Attributes44`](../../doc/models/attributes-44.md) | Optional | - |
| `created_on` | `datetime` | Optional | - |
| `id` | `uuid\|str` | Required | - |
| `modified_on` | `datetime` | Optional | - |
| `organisation_id` | `uuid\|str` | Required | Unique ID of the organisation this resource is created by |
| `relationships` | [`TransactionFileSubmissionRelationships`](../../doc/models/transaction-file-submission-relationships.md) | Optional | - |
| `mtype` | [`Type4Enum`](../../doc/models/type-4-enum.md) | Optional | - |
| `version` | `int` | Optional | Version number<br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "created_on": "09/26/2017 15:26:57",
  "id": "000003de-0000-0000-0000-000000000000",
  "modified_on": "09/26/2017 15:26:57",
  "organisation_id": "ee2fb143-6dfe-4787-b183-ca8ddd4164d2",
  "version": 0,
  "attributes": {
    "scheme_references": [
      {
        "clearing_id": "clearing_id4",
        "file_identifier": "file_identifier4",
        "file_number": "file_number8",
        "transaction_count": 98,
        "transaction_sum": "transaction_sum0"
      }
    ],
    "status": "delivery_failed",
    "status_reason": "status_reason6",
    "submission_datetime": "2016-03-13T12:52:32.123Z",
    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
  },
  "relationships": {
    "transaction_files": {
      "data": [
        {
          "attributes": {
            "file_format": "ndjson",
            "file_hash": "file_hash0",
            "file_size": 44,
            "hashing_algorithm": "hashing_algorithm2",
            "number_of_parts": 8,
            "payment_scheme": "payment_scheme4",
            "transaction_count": 254,
            "transaction_data": {
              "key1": "val1",
              "key2": "val2"
            },
            "transaction_sum": "transaction_sum2"
          },
          "created_on": "2016-03-13T12:52:32.123Z",
          "id": "00001c2a-0000-0000-0000-000000000000",
          "modified_on": "2016-03-13T12:52:32.123Z",
          "organisation_id": "00000b24-0000-0000-0000-000000000000",
          "relationships": {
            "reports": {
              "data": [
                {
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "type": "type0"
                },
                {
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "type": "type0"
                },
                {
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "type": "type0"
                }
              ]
            },
            "transaction_file_admissions": {
              "data": [
                {
                  "attributes": {
                    "admission_datetime": "2016-03-13T12:52:32.123Z",
                    "status": "failed",
                    "status_reason": "status_reason6",
                    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
                  },
                  "created_on": "2016-03-13T12:52:32.123Z",
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "modified_on": "2016-03-13T12:52:32.123Z",
                  "organisation_id": "00000b24-0000-0000-0000-000000000000",
                  "relationships": {
                    "transaction_files": {}
                  },
                  "type": "transaction_file_admissions"
                }
              ]
            },
            "transaction_file_submissions": {
              "data": [
                {
                  "attributes": {
                    "scheme_references": [
                      {
                        "clearing_id": "clearing_id4",
                        "file_identifier": "file_identifier4",
                        "file_number": "file_number8",
                        "transaction_count": 98,
                        "transaction_sum": "transaction_sum0"
                      }
                    ],
                    "status": "delivery_failed",
                    "status_reason": "status_reason6",
                    "submission_datetime": "2016-03-13T12:52:32.123Z",
                    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
                  },
                  "created_on": "2016-03-13T12:52:32.123Z",
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "modified_on": "2016-03-13T12:52:32.123Z",
                  "organisation_id": "00000b24-0000-0000-0000-000000000000",
                  "relationships": {},
                  "type": "transaction_file_submissions"
                },
                {
                  "attributes": {
                    "scheme_references": [
                      {
                        "clearing_id": "clearing_id4",
                        "file_identifier": "file_identifier4",
                        "file_number": "file_number8",
                        "transaction_count": 98,
                        "transaction_sum": "transaction_sum0"
                      }
                    ],
                    "status": "delivery_failed",
                    "status_reason": "status_reason6",
                    "submission_datetime": "2016-03-13T12:52:32.123Z",
                    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
                  },
                  "created_on": "2016-03-13T12:52:32.123Z",
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "modified_on": "2016-03-13T12:52:32.123Z",
                  "organisation_id": "00000b24-0000-0000-0000-000000000000",
                  "relationships": {},
                  "type": "transaction_file_submissions"
                }
              ]
            }
          },
          "type": "transaction_files",
          "version": 110
        },
        {
          "attributes": {
            "file_format": "ndjson",
            "file_hash": "file_hash0",
            "file_size": 44,
            "hashing_algorithm": "hashing_algorithm2",
            "number_of_parts": 8,
            "payment_scheme": "payment_scheme4",
            "transaction_count": 254,
            "transaction_data": {
              "key1": "val1",
              "key2": "val2"
            },
            "transaction_sum": "transaction_sum2"
          },
          "created_on": "2016-03-13T12:52:32.123Z",
          "id": "00001c2a-0000-0000-0000-000000000000",
          "modified_on": "2016-03-13T12:52:32.123Z",
          "organisation_id": "00000b24-0000-0000-0000-000000000000",
          "relationships": {
            "reports": {
              "data": [
                {
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "type": "type0"
                },
                {
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "type": "type0"
                },
                {
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "type": "type0"
                }
              ]
            },
            "transaction_file_admissions": {
              "data": [
                {
                  "attributes": {
                    "admission_datetime": "2016-03-13T12:52:32.123Z",
                    "status": "failed",
                    "status_reason": "status_reason6",
                    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
                  },
                  "created_on": "2016-03-13T12:52:32.123Z",
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "modified_on": "2016-03-13T12:52:32.123Z",
                  "organisation_id": "00000b24-0000-0000-0000-000000000000",
                  "relationships": {
                    "transaction_files": {}
                  },
                  "type": "transaction_file_admissions"
                }
              ]
            },
            "transaction_file_submissions": {
              "data": [
                {
                  "attributes": {
                    "scheme_references": [
                      {
                        "clearing_id": "clearing_id4",
                        "file_identifier": "file_identifier4",
                        "file_number": "file_number8",
                        "transaction_count": 98,
                        "transaction_sum": "transaction_sum0"
                      }
                    ],
                    "status": "delivery_failed",
                    "status_reason": "status_reason6",
                    "submission_datetime": "2016-03-13T12:52:32.123Z",
                    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
                  },
                  "created_on": "2016-03-13T12:52:32.123Z",
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "modified_on": "2016-03-13T12:52:32.123Z",
                  "organisation_id": "00000b24-0000-0000-0000-000000000000",
                  "relationships": {},
                  "type": "transaction_file_submissions"
                },
                {
                  "attributes": {
                    "scheme_references": [
                      {
                        "clearing_id": "clearing_id4",
                        "file_identifier": "file_identifier4",
                        "file_number": "file_number8",
                        "transaction_count": 98,
                        "transaction_sum": "transaction_sum0"
                      }
                    ],
                    "status": "delivery_failed",
                    "status_reason": "status_reason6",
                    "submission_datetime": "2016-03-13T12:52:32.123Z",
                    "transaction_start_datetime": "2016-03-13T12:52:32.123Z"
                  },
                  "created_on": "2016-03-13T12:52:32.123Z",
                  "id": "00001c2a-0000-0000-0000-000000000000",
                  "modified_on": "2016-03-13T12:52:32.123Z",
                  "organisation_id": "00000b24-0000-0000-0000-000000000000",
                  "relationships": {},
                  "type": "transaction_file_submissions"
                }
              ]
            }
          },
          "type": "transaction_files",
          "version": 110
        }
      ]
    }
  },
  "type": "transaction_file_submissions"
}
```
