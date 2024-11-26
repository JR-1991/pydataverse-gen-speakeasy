# BuiltinUsers
(*builtin_users*)

## Overview

### Available Operations

* [post_builtin_users](#post_builtin_users) - Create a new builtin user
* [create_builtin_user](#create_builtin_user) - Create a new built-in user using a password and key
* [create_builtin_user_1](#create_builtin_user_1) - Create a new builtin-user with a specific key, password and email notification preference.
* [get_api_token_by_username](#get_api_token_by_username) - Gets the API token for the specified built-in user

## post_builtin_users

Create a new builtin user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.builtin_users.post_builtin_users()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `key`                     | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `password`                | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |
| `send_email_notification` | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |

### Response

**[operations.PostBuiltinUsersResponse](../../models/operations/postbuiltinusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_builtin_user

Create a new built-in user using a password and key

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.builtin_users.create_builtin_user(key='<key>', password='bT1J7kLnkhyBrOW')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *str*              | :heavy_check_mark: | N/A                |
| `password`         | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.CreateBuiltinUserResponse](../../models/operations/createbuiltinuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_builtin_user_1

Create a new builtin-user with a specific key, password and email notification preference.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.builtin_users.create_builtin_user_1(key='<key>', password='XGntXDnk7mNelX8', send_email_notification=True)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `key`                     | *str*                     | :heavy_check_mark:        | N/A                       |
| `password`                | *str*                     | :heavy_check_mark:        | N/A                       |
| `send_email_notification` | *bool*                    | :heavy_check_mark:        | N/A                       |

### Response

**[operations.CreateBuiltinUser1Response](../../models/operations/createbuiltinuser1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_api_token_by_username

Gets the API token for the specified built-in user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.builtin_users.get_api_token_by_username(username='Lou48')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `username`         | *str*              | :heavy_check_mark: | N/A                |
| `password`         | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetAPITokenByUsernameResponse](../../models/operations/getapitokenbyusernameresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |