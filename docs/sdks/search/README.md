# Search
(*search*)

### Available Operations

* [get_api_v1_search](#get_api_v1_search)

## get_api_v1_search

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse()

req = operations.GetAPIV1SearchRequest()

res = s.search.get_api_v1_search(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAPIV1SearchRequest](../../models/operations/getapiv1searchrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetAPIV1SearchResponse](../../models/operations/getapiv1searchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
