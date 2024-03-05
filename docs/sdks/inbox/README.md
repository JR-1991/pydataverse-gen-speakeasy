# Inbox
(*inbox*)

### Available Operations

* [post_inbox](#post_inbox) - Create a new inbox message

## post_inbox

Create a new inbox message

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()

req = '<value>'

res = s.inbox.post_inbox(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PostInboxResponse](../../models/operations/postinboxresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
