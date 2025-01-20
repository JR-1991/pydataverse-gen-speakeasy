# Datatags
(*datatags*)

## Overview

### Available Operations

* [post_receive_tags](#post_receive_tags) - Create a new datatag and associate it with the specified unique cache ID

## post_receive_tags

Create a new datatag and associate it with the specified unique cache ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datatags.post_receive_tags(unique_cache_id='<id>')

if res is not None:
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |