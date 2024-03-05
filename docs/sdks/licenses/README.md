# Licenses
(*licenses*)

### Available Operations

* [get_api_v1_licenses](#get_api_v1_licenses)
* [post_api_v1_licenses](#post_api_v1_licenses)
* [get_api_v1_licenses_default](#get_api_v1_licenses_default)
* [put_api_v1_licenses_default_id_](#put_api_v1_licenses_default_id_)
* [get_api_v1_licenses_id_](#get_api_v1_licenses_id_)
* [delete_api_v1_licenses_id_](#delete_api_v1_licenses_id_)
* [put_api_v1_licenses_id_active_active_state_](#put_api_v1_licenses_id_active_active_state_)
* [put_api_v1_licenses_id_sort_order_sort_order_](#put_api_v1_licenses_id_sort_order_sort_order_)

## get_api_v1_licenses

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.get_api_v1_licenses()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1LicensesResponse](../../models/operations/getapiv1licensesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_licenses

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.post_api_v1_licenses()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostAPIV1LicensesResponse](../../models/operations/postapiv1licensesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_licenses_default

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.get_api_v1_licenses_default()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1LicensesDefaultResponse](../../models/operations/getapiv1licensesdefaultresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_licenses_default_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.put_api_v1_licenses_default_id_(id=702036)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1LicensesDefaultIDResponse](../../models/operations/putapiv1licensesdefaultidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_licenses_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.get_api_v1_licenses_id_(id=185769)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1LicensesIDResponse](../../models/operations/getapiv1licensesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_licenses_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.delete_api_v1_licenses_id_(id=307281)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1LicensesIDResponse](../../models/operations/deleteapiv1licensesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_licenses_id_active_active_state_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.put_api_v1_licenses_id_active_active_state_(active_state=False, id=262386)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `active_state`     | *bool*             | :heavy_check_mark: | N/A                |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1LicensesIDActiveActiveStateResponse](../../models/operations/putapiv1licensesidactiveactivestateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_licenses_id_sort_order_sort_order_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.licenses.put_api_v1_licenses_id_sort_order_sort_order_(id=754761, sort_order=445396)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |
| `sort_order`       | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1LicensesIDSortOrderSortOrderResponse](../../models/operations/putapiv1licensesidsortordersortorderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
