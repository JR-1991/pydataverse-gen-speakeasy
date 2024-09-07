# Batch
(*batch*)

## Overview

### Available Operations

* [get_batch_harvest](#get_batch_harvest) - Retrieves information about a batch harvest based on provided parameters
* [get_batch_import_status](#get_batch_import_status) - Retrieve status of a batch import request
* [create_batch_import](#create_batch_import) - Initiate a new batch import request
* [post_batch_job_import_datasets](#post_batch_job_import_datasets) - Initiate a batch job for importing datasets using the provided identifier

## get_batch_harvest

Retrieves information about a batch harvest based on provided parameters

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.batch.get_batch_harvest()

if res is not None:
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

**[operations.GetBatchHarvestResponse](../../models/operations/getbatchharvestresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get_batch_import_status

Retrieve status of a batch import request

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.batch.get_batch_import_status()

if res is not None:
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

**[operations.GetBatchImportStatusResponse](../../models/operations/getbatchimportstatusresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## create_batch_import

Initiate a new batch import request

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.batch.create_batch_import()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dv`               | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.CreateBatchImportResponse](../../models/operations/createbatchimportresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## post_batch_job_import_datasets

Initiate a batch job for importing datasets using the provided identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.batch.post_batch_job_import_datasets(identifier='<value>')

if res is not None:
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

**[operations.PostBatchJobImportDatasetsResponse](../../models/operations/postbatchjobimportdatasetsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
