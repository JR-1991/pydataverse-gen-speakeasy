# Meta
(*meta*)

### Available Operations

* [~~get_datafile_meta~~](#get_datafile_meta) - Get metadata of a specific datafile by file id :warning: **Deprecated**
* [~~get_dataset_metadata_1~~](#get_dataset_metadata_1) - Retrieves the metadata of a specific dataset by its ID :warning: **Deprecated**

## ~~get_datafile_meta~~

Get metadata of a specific datafile by file id

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.meta.get_datafile_meta(file_id=708075)

if res.res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *int*              | :heavy_check_mark: | N/A                |
| `exclude`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `file_metadata_id` | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `include`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDatafileMetaResponse](../../models/operations/getdatafilemetaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~get_dataset_metadata_1~~

Retrieves the metadata of a specific dataset by its ID

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.meta.get_dataset_metadata_1(dataset_id=492183)

if res.res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dataset_id`       | *int*              | :heavy_check_mark: | N/A                |
| `exclude`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `include`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDatasetMetadata1Response](../../models/operations/getdatasetmetadata1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
