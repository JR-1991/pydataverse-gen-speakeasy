# Search
(*search*)

### Available Operations

* [search_query](#search_query) - Executes a search query with various parameters and returns the matching records.

## search_query

Executes a search query with various parameters and returns the matching records.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.search.search_query()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.SearchQueryRequest](../../models/operations/searchqueryrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.SearchQueryResponse](../../models/operations/searchqueryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
