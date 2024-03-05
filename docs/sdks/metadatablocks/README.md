# Metadatablocks
(*metadatablocks*)

### Available Operations

* [get_api_v1_metadatablocks](#get_api_v1_metadatablocks)
* [get_api_v1_metadatablocks_identifier_](#get_api_v1_metadatablocks_identifier_)

## get_api_v1_metadatablocks

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.metadatablocks.get_api_v1_metadatablocks()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1MetadatablocksResponse](../../models/operations/getapiv1metadatablocksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_metadatablocks_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.metadatablocks.get_api_v1_metadatablocks_identifier_(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1MetadatablocksIdentifierResponse](../../models/operations/getapiv1metadatablocksidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
