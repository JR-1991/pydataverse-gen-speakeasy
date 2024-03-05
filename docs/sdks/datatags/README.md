# Datatags
(*datatags*)

### Available Operations

* [post_api_v1_datatags_receive_tags_unique_cache_id_](#post_api_v1_datatags_receive_tags_unique_cache_id_)

## post_api_v1_datatags_receive_tags_unique_cache_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.datatags.post_api_v1_datatags_receive_tags_unique_cache_id_(unique_cache_id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `unique_cache_id`  | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DatatagsReceiveTagsUniqueCacheIDResponse](../../models/operations/postapiv1datatagsreceivetagsuniquecacheidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
