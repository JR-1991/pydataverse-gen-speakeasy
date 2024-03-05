# Mydata
(*mydata*)

### Available Operations

* [get_api_v1_mydata_retrieve](#get_api_v1_mydata_retrieve)

## get_api_v1_mydata_retrieve

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse()

req = operations.GetAPIV1MydataRetrieveRequest()

res = s.mydata.get_api_v1_mydata_retrieve(req)

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAPIV1MydataRetrieveRequest](../../models/operations/getapiv1mydataretrieverequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetAPIV1MydataRetrieveResponse](../../models/operations/getapiv1mydataretrieveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
