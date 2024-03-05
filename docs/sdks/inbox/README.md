# Inbox
(*inbox*)

### Available Operations

* [post_api_v1_inbox](#post_api_v1_inbox)

## post_api_v1_inbox

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()

req = '<value>'

res = s.inbox.post_api_v1_inbox(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PostAPIV1InboxResponse](../../models/operations/postapiv1inboxresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
