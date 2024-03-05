# BuiltinUsers
(*builtin_users*)

### Available Operations

* [post_api_v1_builtin_users](#post_api_v1_builtin_users)
* [post_api_v1_builtin_users_password_key_](#post_api_v1_builtin_users_password_key_)
* [post_api_v1_builtin_users_password_key_send_email_notification_](#post_api_v1_builtin_users_password_key_send_email_notification_)
* [get_api_v1_builtin_users_username_api_token](#get_api_v1_builtin_users_username_api_token)

## post_api_v1_builtin_users

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.builtin_users.post_api_v1_builtin_users(key='<value>', password='<value>', send_email_notification=False)

if res.status_code == 200:
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

**[operations.PostAPIV1BuiltinUsersResponse](../../models/operations/postapiv1builtinusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_builtin_users_password_key_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.builtin_users.post_api_v1_builtin_users_password_key_(key='<value>', password='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *str*              | :heavy_check_mark: | N/A                |
| `password`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1BuiltinUsersPasswordKeyResponse](../../models/operations/postapiv1builtinuserspasswordkeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_builtin_users_password_key_send_email_notification_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.builtin_users.post_api_v1_builtin_users_password_key_send_email_notification_(key='<value>', password='<value>', send_email_notification=False)

if res.status_code == 200:
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

**[operations.PostAPIV1BuiltinUsersPasswordKeySendEmailNotificationResponse](../../models/operations/postapiv1builtinuserspasswordkeysendemailnotificationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_builtin_users_username_api_token

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.builtin_users.get_api_v1_builtin_users_username_api_token(username='<value>', password='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `username`         | *str*              | :heavy_check_mark: | N/A                |
| `password`         | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1BuiltinUsersUsernameAPITokenResponse](../../models/operations/getapiv1builtinusersusernameapitokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
