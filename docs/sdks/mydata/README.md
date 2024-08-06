# Mydata
(*mydata*)

### Available Operations

* [my_data_retrieve](#my_data_retrieve) - Retrieve specific set of my data based on the provided filters

## my_data_retrieve

Retrieve specific set of my data based on the provided filters

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.mydata.my_data_retrieve()

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.MyDataRetrieveRequest](../../models/operations/mydataretrieverequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.MyDataRetrieveResponse](../../models/operations/mydataretrieveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
