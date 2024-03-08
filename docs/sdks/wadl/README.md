# Wadl
(*application.wadl*)

### Available Operations

* [get_application_wadl](#get_application_wadl) - Retrieves the application WADL
* [get_application_wadl_1](#get_application_wadl_1) - Retrieve the application WADL

## get_application_wadl

Retrieves the application WADL

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.application.wadl.get_application_wadl()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetApplicationWadlResponse](../../models/operations/getapplicationwadlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_application_wadl_1

Retrieve the application WADL

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.application.wadl.get_application_wadl_1(path='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `path`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetApplicationWadl1Response](../../models/operations/getapplicationwadl1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
