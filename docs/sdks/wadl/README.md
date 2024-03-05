# Wadl
(*application.wadl*)

### Available Operations

* [get_api_v1_application_wadl](#get_api_v1_application_wadl)
* [get_api_v1_application_wadl_path_](#get_api_v1_application_wadl_path_)

## get_api_v1_application_wadl

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.application.wadl.get_api_v1_application_wadl()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1ApplicationWadlResponse](../../models/operations/getapiv1applicationwadlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_application_wadl_path_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.application.wadl.get_api_v1_application_wadl_path_(path='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `path`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1ApplicationWadlPathResponse](../../models/operations/getapiv1applicationwadlpathresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
