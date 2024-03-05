# Logout
(*logout*)

### Available Operations

* [post_api_v1_logout](#post_api_v1_logout)

## post_api_v1_logout

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.logout.post_api_v1_logout()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostAPIV1LogoutResponse](../../models/operations/postapiv1logoutresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
