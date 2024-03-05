# Roles
(*roles*)

### Available Operations

* [post_api_v1_roles](#post_api_v1_roles)
* [get_api_v1_roles_id_](#get_api_v1_roles_id_)
* [delete_api_v1_roles_id_](#delete_api_v1_roles_id_)

## post_api_v1_roles

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.roles.post_api_v1_roles(dvo='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dvo`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1RolesResponse](../../models/operations/postapiv1rolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_roles_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.roles.get_api_v1_roles_id_(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1RolesIDResponse](../../models/operations/getapiv1rolesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_roles_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.roles.delete_api_v1_roles_id_(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1RolesIDResponse](../../models/operations/deleteapiv1rolesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
