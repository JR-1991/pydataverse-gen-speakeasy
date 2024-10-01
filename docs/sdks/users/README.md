# Users
(*users*)

## Overview

### Available Operations

* [get_user_details](#get_user_details) - Retrieve the details of the logged-in user
* [get_user_token](#get_user_token) - Retrieves a user's authentication token
* [delete_user_token](#delete_user_token) - Deletes a user's authentication token
* [recreate_user_token](#recreate_user_token) - Recreates the authentication token for a given user
* [merge_users](#merge_users) - Merge the user with consumedIdentifier into the user with baseIdentifier
* [change_user_identifier](#change_user_identifier) - Change the identifier of a given user
* [remove_user_roles](#remove_user_roles) - Remove roles from a specific user
* [get_user_traces](#get_user_traces) - Retrieve a user's traces
* [get_user_trace_element](#get_user_trace_element) - Retrieve a specific trace element for a given user

## get_user_details

Retrieve the details of the logged-in user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.get_user_details()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetUserDetailsResponse](../../models/operations/getuserdetailsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_user_token

Retrieves a user's authentication token

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.get_user_token()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetUserTokenResponse](../../models/operations/getusertokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_user_token

Deletes a user's authentication token

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.delete_user_token()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.DeleteUserTokenResponse](../../models/operations/deleteusertokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## recreate_user_token

Recreates the authentication token for a given user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.recreate_user_token()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.RecreateUserTokenResponse](../../models/operations/recreateusertokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## merge_users

Merge the user with consumedIdentifier into the user with baseIdentifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.merge_users(base_identifier='<value>', consumed_identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `base_identifier`     | *str*                 | :heavy_check_mark:    | N/A                   |
| `consumed_identifier` | *str*                 | :heavy_check_mark:    | N/A                   |

### Response

**[operations.MergeUsersResponse](../../models/operations/mergeusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## change_user_identifier

Change the identifier of a given user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.change_user_identifier(identifier='<value>', new_identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `new_identifier`   | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.ChangeUserIdentifierResponse](../../models/operations/changeuseridentifierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_user_roles

Remove roles from a specific user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.remove_user_roles(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.RemoveUserRolesResponse](../../models/operations/removeuserrolesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_user_traces

Retrieve a user's traces

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.get_user_traces(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetUserTracesResponse](../../models/operations/getusertracesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_user_trace_element

Retrieve a specific trace element for a given user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.users.get_user_trace_element(element='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `element`          | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetUserTraceElementResponse](../../models/operations/getusertraceelementresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |