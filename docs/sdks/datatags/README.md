# Datatags
(*datatags*)

### Available Operations

* [post_receive_tags](#post_receive_tags) - Create a new datatag and associate it with the specified unique cache ID

## post_receive_tags

Create a new datatag and associate it with the specified unique cache ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.datatags.post_receive_tags(unique_cache_id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `unique_cache_id`  | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostReceiveTagsResponse](../../models/operations/postreceivetagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
