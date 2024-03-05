# Batch
(*batch*)

### Available Operations

* [get_api_v1_batch_harvest](#get_api_v1_batch_harvest)
* [get_api_v1_batch_import](#get_api_v1_batch_import)
* [post_api_v1_batch_import](#post_api_v1_batch_import)
* [post_api_v1_batch_jobs_import_datasets_files_identifier_](#post_api_v1_batch_jobs_import_datasets_files_identifier_)

## get_api_v1_batch_harvest

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.batch.get_api_v1_batch_harvest(create_dv=False, dv='<value>', key='<value>', path='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `create_dv`        | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `dv`               | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `path`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1BatchHarvestResponse](../../models/operations/getapiv1batchharvestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_batch_import

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.batch.get_api_v1_batch_import(create_dv=False, dv='<value>', key='<value>', path='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `create_dv`        | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `dv`               | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `path`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1BatchImportResponse](../../models/operations/getapiv1batchimportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_batch_import

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.batch.post_api_v1_batch_import(dv='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dv`               | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1BatchImportResponse](../../models/operations/postapiv1batchimportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_batch_jobs_import_datasets_files_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.batch.post_api_v1_batch_jobs_import_datasets_files_identifier_(identifier='<value>', mode='MERGE', total_size=18653, upload_folder='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `mode`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `total_size`       | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `upload_folder`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1BatchJobsImportDatasetsFilesIdentifierResponse](../../models/operations/postapiv1batchjobsimportdatasetsfilesidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
