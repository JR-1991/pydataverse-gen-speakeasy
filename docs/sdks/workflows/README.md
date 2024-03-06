# Workflows
(*workflows*)

### Available Operations

* [start_workflow](#start_workflow) - Initiate a workflow using the given invocation id

## start_workflow

Initiate a workflow using the given invocation id

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.workflows.start_workflow(invocation_id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `invocation_id`    | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.StartWorkflowResponse](../../models/operations/startworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
