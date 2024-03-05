# Meta
(*meta*)

### Available Operations

* [~~get_api_v1_meta_datafile_file_id_~~](#get_api_v1_meta_datafile_file_id_) - :warning: **Deprecated**
* [~~get_api_v1_meta_dataset_dataset_id_~~](#get_api_v1_meta_dataset_dataset_id_) - :warning: **Deprecated**

## ~~get_api_v1_meta_datafile_file_id_~~

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.meta.get_api_v1_meta_datafile_file_id_(file_id=696407, exclude='<value>', file_metadata_id=880679, include='<value>')

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

**[operations.GetAPIV1MetaDatafileFileIDResponse](../../models/operations/getapiv1metadatafilefileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~get_api_v1_meta_dataset_dataset_id_~~

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.meta.get_api_v1_meta_dataset_dataset_id_(dataset_id=618154, exclude='<value>', include='<value>')

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

**[operations.GetAPIV1MetaDatasetDatasetIDResponse](../../models/operations/getapiv1metadatasetdatasetidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
