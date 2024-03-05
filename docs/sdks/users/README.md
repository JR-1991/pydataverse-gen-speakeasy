# Users
(*users*)

### Available Operations

* [get_api_v1_users_me](#get_api_v1_users_me)
* [get_api_v1_users_token](#get_api_v1_users_token)
* [delete_api_v1_users_token](#delete_api_v1_users_token)
* [post_api_v1_users_token_recreate](#post_api_v1_users_token_recreate)
* [post_api_v1_users_consumed_identifier_merge_into_user_base_identifier_](#post_api_v1_users_consumed_identifier_merge_into_user_base_identifier_)
* [post_api_v1_users_identifier_change_identifier_new_identifier_](#post_api_v1_users_identifier_change_identifier_new_identifier_)
* [post_api_v1_users_identifier_remove_roles](#post_api_v1_users_identifier_remove_roles)
* [get_api_v1_users_identifier_traces](#get_api_v1_users_identifier_traces)
* [get_api_v1_users_identifier_traces_element_](#get_api_v1_users_identifier_traces_element_)

## get_api_v1_users_me

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.get_api_v1_users_me()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1UsersMeResponse](../../models/operations/getapiv1usersmeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_users_token

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.get_api_v1_users_token()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1UsersTokenResponse](../../models/operations/getapiv1userstokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_users_token

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.delete_api_v1_users_token()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.DeleteAPIV1UsersTokenResponse](../../models/operations/deleteapiv1userstokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_users_token_recreate

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.post_api_v1_users_token_recreate()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostAPIV1UsersTokenRecreateResponse](../../models/operations/postapiv1userstokenrecreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_users_consumed_identifier_merge_into_user_base_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.post_api_v1_users_consumed_identifier_merge_into_user_base_identifier_(base_identifier='<value>', consumed_identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `base_identifier`     | *str*                 | :heavy_check_mark:    | N/A                   |
| `consumed_identifier` | *str*                 | :heavy_check_mark:    | N/A                   |


### Response

**[operations.PostAPIV1UsersConsumedIdentifierMergeIntoUserBaseIdentifierResponse](../../models/operations/postapiv1usersconsumedidentifiermergeintouserbaseidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_users_identifier_change_identifier_new_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.post_api_v1_users_identifier_change_identifier_new_identifier_(identifier='<value>', new_identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `new_identifier`   | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1UsersIdentifierChangeIdentifierNewIdentifierResponse](../../models/operations/postapiv1usersidentifierchangeidentifiernewidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_users_identifier_remove_roles

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.post_api_v1_users_identifier_remove_roles(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1UsersIdentifierRemoveRolesResponse](../../models/operations/postapiv1usersidentifierremoverolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_users_identifier_traces

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.get_api_v1_users_identifier_traces(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1UsersIdentifierTracesResponse](../../models/operations/getapiv1usersidentifiertracesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_users_identifier_traces_element_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.users.get_api_v1_users_identifier_traces_element_(element='<value>', identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `element`          | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1UsersIdentifierTracesElementResponse](../../models/operations/getapiv1usersidentifiertraceselementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
