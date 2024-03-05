# Edit
(*edit*)

### Available Operations

* [put_api_v1_edit_file_id_](#put_api_v1_edit_file_id_)

## put_api_v1_edit_file_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.edit.put_api_v1_edit_file_id_(file_id='<value>', request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PutAPIV1EditFileIDResponse](../../models/operations/putapiv1editfileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
