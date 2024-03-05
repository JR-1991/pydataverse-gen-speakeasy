# Pids
(*pids*)

### Available Operations

* [get_api_v1_pids](#get_api_v1_pids)
* [get_api_v1_pids_unreserved](#get_api_v1_pids_unreserved)
* [delete_api_v1_pids_id_delete](#delete_api_v1_pids_id_delete)
* [post_api_v1_pids_id_reserve](#post_api_v1_pids_id_reserve)

## get_api_v1_pids

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.pids.get_api_v1_pids(persistent_id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `persistent_id`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1PidsResponse](../../models/operations/getapiv1pidsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_pids_unreserved

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.pids.get_api_v1_pids_unreserved(persistent_id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `persistent_id`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1PidsUnreservedResponse](../../models/operations/getapiv1pidsunreservedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_pids_id_delete

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.pids.delete_api_v1_pids_id_delete(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1PidsIDDeleteResponse](../../models/operations/deleteapiv1pidsiddeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_pids_id_reserve

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.pids.post_api_v1_pids_id_reserve(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1PidsIDReserveResponse](../../models/operations/postapiv1pidsidreserveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
