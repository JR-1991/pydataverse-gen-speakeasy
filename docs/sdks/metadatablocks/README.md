# Metadatablocks
(*metadatablocks*)

### Available Operations

* [get_metadatablocks](#get_metadatablocks) - Retrieve metadata blocks available in the system
* [get_metadatablock_1_1](#get_metadatablock_1_1) - Retrieve a specific Metadatablock by its identifier

## get_metadatablocks

Retrieve metadata blocks available in the system

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.metadatablocks.get_metadatablocks()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetMetadatablocksResponse](../../models/operations/getmetadatablocksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metadatablock_1_1

Retrieve a specific Metadatablock by its identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.metadatablocks.get_metadatablock_1_1(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetMetadatablock11Response](../../models/operations/getmetadatablock11response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |