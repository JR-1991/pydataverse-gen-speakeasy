# Logout
(*logout*)

### Available Operations

* [logout_user](#logout_user) - Log out the current user

## logout_user

Log out the current user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.logout.logout_user()

if res is not None:
    # handle response
    pass

```




### Response

**[operations.LogoutUserResponse](../../models/operations/logoutuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
