# Licenses
(*licenses*)

### Available Operations

* [get_licenses](#get_licenses) - Retrieve all the licenses
* [add_license](#add_license) - Add a new license
* [get_default_license](#get_default_license) - Fetch the current default license
* [update_default_license](#update_default_license) - Update a default license by ID
* [get_license](#get_license) - Retrieve a specific license by its ID
* [delete_license](#delete_license) - Delete a specific license by its ID
* [update_license_active_state](#update_license_active_state) - Updates the activity state of a specific license
* [update_license_sort_order](#update_license_sort_order) - Update the sort order of a given license

## get_licenses

Retrieve all the licenses

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.get_licenses()

if res is not None:
    # handle response
    pass

```




### Response

**[operations.GetLicensesResponse](../../models/operations/getlicensesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_license

Add a new license

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.add_license()

if res is not None:
    # handle response
    pass

```




### Response

**[operations.AddLicenseResponse](../../models/operations/addlicenseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_default_license

Fetch the current default license

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.get_default_license()

if res is not None:
    # handle response
    pass

```




### Response

**[operations.GetDefaultLicenseResponse](../../models/operations/getdefaultlicenseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_default_license

Update a default license by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.update_default_license(id=34621)

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateDefaultLicenseResponse](../../models/operations/updatedefaultlicenseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_license

Retrieve a specific license by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.get_license(id=179853)

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetLicenseResponse](../../models/operations/getlicenseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_license

Delete a specific license by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.delete_license(id=738361)

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteLicenseResponse](../../models/operations/deletelicenseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_license_active_state

Updates the activity state of a specific license

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.update_license_active_state(active_state=False, id=744481)

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `active_state`     | *bool*             | :heavy_check_mark: | N/A                |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateLicenseActiveStateResponse](../../models/operations/updatelicenseactivestateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_license_sort_order

Update the sort order of a given license

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.licenses.update_license_sort_order(id=430322, sort_order=505916)

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |
| `sort_order`       | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateLicenseSortOrderResponse](../../models/operations/updatelicensesortorderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
