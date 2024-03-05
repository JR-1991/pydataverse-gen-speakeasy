# Logout
(*logout*)

### Available Operations

* [logout_user](#logout_user) - Log out the current user

## logout_user

Log out the current user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.logout.logout_user()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.LogoutUserResponse](../../models/operations/logoutuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |