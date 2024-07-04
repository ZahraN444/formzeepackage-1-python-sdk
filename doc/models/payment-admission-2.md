
# Payment Admission 2

## Structure

`PaymentAdmission2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[PaymentAdmission]`](../../doc/models/payment-admission.md) | Optional | Array of Payment Admission resources related to the payment |

## Example (as JSON)

```json
{
  "data": [
    {
      "attributes": {
        "admission_datetime": "2016-03-13T12:52:32.123Z",
        "clearing_system": "clearing_system0",
        "route": "on_us",
        "scheme_status_code": "scheme_status_code6",
        "scheme_status_code_description": "scheme_status_code_description4"
      },
      "created_on": "2016-03-13T12:52:32.123Z",
      "id": "00001c2a-0000-0000-0000-000000000000",
      "modified_on": "2016-03-13T12:52:32.123Z",
      "organisation_id": "00000b24-0000-0000-0000-000000000000",
      "relationships": {
        "beneficiary_account": {
          "data": [
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            },
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            },
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            }
          ]
        },
        "payment": {
          "data": [
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            },
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            },
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            }
          ]
        },
        "payment_admission_task": {
          "data": [
            {
              "attributes": {
                "assignee": "customer",
                "name": "name4",
                "output": {
                  "key0": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key1": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key2": {
                    "key1": "val1",
                    "key2": "val2"
                  }
                },
                "status": "pending",
                "workflow": "000021d2-0000-0000-0000-000000000000"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000"
            },
            {
              "attributes": {
                "assignee": "customer",
                "name": "name4",
                "output": {
                  "key0": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key1": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key2": {
                    "key1": "val1",
                    "key2": "val2"
                  }
                },
                "status": "pending",
                "workflow": "000021d2-0000-0000-0000-000000000000"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000"
            }
          ]
        }
      },
      "type": "type0"
    },
    {
      "attributes": {
        "admission_datetime": "2016-03-13T12:52:32.123Z",
        "clearing_system": "clearing_system0",
        "route": "on_us",
        "scheme_status_code": "scheme_status_code6",
        "scheme_status_code_description": "scheme_status_code_description4"
      },
      "created_on": "2016-03-13T12:52:32.123Z",
      "id": "00001c2a-0000-0000-0000-000000000000",
      "modified_on": "2016-03-13T12:52:32.123Z",
      "organisation_id": "00000b24-0000-0000-0000-000000000000",
      "relationships": {
        "beneficiary_account": {
          "data": [
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            },
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            },
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            }
          ]
        },
        "payment": {
          "data": [
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            },
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            },
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            }
          ]
        },
        "payment_admission_task": {
          "data": [
            {
              "attributes": {
                "assignee": "customer",
                "name": "name4",
                "output": {
                  "key0": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key1": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key2": {
                    "key1": "val1",
                    "key2": "val2"
                  }
                },
                "status": "pending",
                "workflow": "000021d2-0000-0000-0000-000000000000"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000"
            },
            {
              "attributes": {
                "assignee": "customer",
                "name": "name4",
                "output": {
                  "key0": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key1": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key2": {
                    "key1": "val1",
                    "key2": "val2"
                  }
                },
                "status": "pending",
                "workflow": "000021d2-0000-0000-0000-000000000000"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000"
            }
          ]
        }
      },
      "type": "type0"
    },
    {
      "attributes": {
        "admission_datetime": "2016-03-13T12:52:32.123Z",
        "clearing_system": "clearing_system0",
        "route": "on_us",
        "scheme_status_code": "scheme_status_code6",
        "scheme_status_code_description": "scheme_status_code_description4"
      },
      "created_on": "2016-03-13T12:52:32.123Z",
      "id": "00001c2a-0000-0000-0000-000000000000",
      "modified_on": "2016-03-13T12:52:32.123Z",
      "organisation_id": "00000b24-0000-0000-0000-000000000000",
      "relationships": {
        "beneficiary_account": {
          "data": [
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            },
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            },
            {
              "attributes": {
                "user_defined_data": [
                  {
                    "key": "key6",
                    "value": "value8"
                  },
                  {
                    "key": "key6",
                    "value": "value8"
                  }
                ]
              },
              "id": "00001c2a-0000-0000-0000-000000000000",
              "type": "type0"
            }
          ]
        },
        "payment": {
          "data": [
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            },
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            },
            {
              "attributes": {
                "agents": [
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  },
                  {
                    "account_number": "account_number0",
                    "account_number_code": "IBAN",
                    "address": [
                      "address4",
                      "address5"
                    ],
                    "identification": {
                      "bank_id": "bank_id4",
                      "bank_id_code": "bank_id_code2",
                      "bank_ids": [
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        },
                        {
                          "bank_id": "bank_id4",
                          "bank_id_code": "bank_id_code8"
                        }
                      ]
                    },
                    "name": "name0"
                  }
                ],
                "amount": "amount6",
                "batch_booking_indicator": "batch_booking_indicator2",
                "batch_id": "batch_id6",
                "batch_type": "batch_type0"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000",
              "relationships": {
                "beneficiary": {
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
                "beneficiary_account": {
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
                "debtor": {
                  "data": [
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
                "debtor_account": {
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
                "forwarded_payment": {
                  "data": [
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    },
                    {
                      "id": "00001c2a-0000-0000-0000-000000000000",
                      "type": "type0"
                    }
                  ]
                }
              },
              "type": "type0",
              "version": 110
            }
          ]
        },
        "payment_admission_task": {
          "data": [
            {
              "attributes": {
                "assignee": "customer",
                "name": "name4",
                "output": {
                  "key0": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key1": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key2": {
                    "key1": "val1",
                    "key2": "val2"
                  }
                },
                "status": "pending",
                "workflow": "000021d2-0000-0000-0000-000000000000"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000"
            },
            {
              "attributes": {
                "assignee": "customer",
                "name": "name4",
                "output": {
                  "key0": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key1": {
                    "key1": "val1",
                    "key2": "val2"
                  },
                  "key2": {
                    "key1": "val1",
                    "key2": "val2"
                  }
                },
                "status": "pending",
                "workflow": "000021d2-0000-0000-0000-000000000000"
              },
              "created_on": "2016-03-13T12:52:32.123Z",
              "id": "00001c2a-0000-0000-0000-000000000000",
              "modified_on": "2016-03-13T12:52:32.123Z",
              "organisation_id": "00000b24-0000-0000-0000-000000000000"
            }
          ]
        }
      },
      "type": "type0"
    }
  ]
}
```
