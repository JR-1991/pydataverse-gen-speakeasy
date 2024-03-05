# Roles
(*roles*)

### Available Operations

* [create_role](#create_role) - Create a new role in the system
* [get_role](#get_role) - Retrieve details of a specific role by id
* [delete_role](#delete_role) - Delete a specific role by id

## create_role

Create a new role in the system

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.roles.create_role(dvo='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dvo`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.CreateRoleResponse](../../models/operations/createroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_role

Retrieve details of a specific role by id

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.roles.get_role(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetRoleResponse](../../models/operations/getroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_role

Delete a specific role by id

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.roles.delete_role(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteRoleResponse](../../models/operations/deleteroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
