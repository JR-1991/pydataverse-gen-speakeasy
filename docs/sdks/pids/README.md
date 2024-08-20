# Pids
(*pids*)

### Available Operations

* [get_persistent_id](#get_persistent_id) - Retrieve a specific persistent identifier
* [get_unreserved_persistent_ids](#get_unreserved_persistent_ids) - Retrieves unreserved persistent identifiers
* [delete_pid](#delete_pid) - Delete a specific persistent identifier (PID)
* [reserve_pid](#reserve_pid) - Reserve a specific PID

## get_persistent_id

Retrieve a specific persistent identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.pids.get_persistent_id()

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `persistent_id`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetPersistentIDResponse](../../models/operations/getpersistentidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_unreserved_persistent_ids

Retrieves unreserved persistent identifiers

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.pids.get_unreserved_persistent_ids()

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `persistent_id`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetUnreservedPersistentIdsResponse](../../models/operations/getunreservedpersistentidsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_pid

Delete a specific persistent identifier (PID)

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.pids.delete_pid(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeletePidResponse](../../models/operations/deletepidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## reserve_pid

Reserve a specific PID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.pids.reserve_pid(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ReservePidResponse](../../models/operations/reservepidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
