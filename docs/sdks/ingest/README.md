# Ingest
(*ingest*)

### Available Operations

* [get_ingest_test_file](#get_ingest_test_file) - Retrieve details of a specific test file in the ingest process by filename and filetype

## get_ingest_test_file

Retrieve details of a specific test file in the ingest process by filename and filetype

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.ingest.get_ingest_test_file(file_name='<value>', file_type='<value>')

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_name`        | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `file_type`        | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetIngestTestFileResponse](../../models/operations/getingesttestfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
