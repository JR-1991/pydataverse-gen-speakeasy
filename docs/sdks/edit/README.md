# Edit
(*edit*)

### Available Operations

* [edit_file](#edit_file) - Edits the content of a specified file

## edit_file

Edits the content of a specified file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.edit.edit_file(file_id='<value>', request_body='<value>')

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

**[operations.EditFileResponse](../../models/operations/editfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |