# Files
(*files*)

### Available Operations

* [get_api_v1_files_fixity_algorithm](#get_api_v1_files_fixity_algorithm)
* [get_api_v1_files_id_](#get_api_v1_files_id_)
* [delete_api_v1_files_id_](#delete_api_v1_files_id_)
* [get_api_v1_files_id_data_tables](#get_api_v1_files_id_data_tables)
* [get_api_v1_files_id_download_count](#get_api_v1_files_id_download_count)
* [get_api_v1_files_id_draft](#get_api_v1_files_id_draft)
* [post_api_v1_files_id_extract_ncml](#post_api_v1_files_id_extract_ncml)
* [get_api_v1_files_id_has_been_deleted](#get_api_v1_files_id_has_been_deleted)
* [get_api_v1_files_id_metadata](#get_api_v1_files_id_metadata)
* [post_api_v1_files_id_metadata](#post_api_v1_files_id_metadata)
* [post_api_v1_files_id_metadata_categories](#post_api_v1_files_id_metadata_categories)
* [get_api_v1_files_id_metadata_draft](#get_api_v1_files_id_metadata_draft)
* [post_api_v1_files_id_metadata_tabular_tags](#post_api_v1_files_id_metadata_tabular_tags)
* [get_api_v1_files_id_metadata_fmid_toolparams_tid_](#get_api_v1_files_id_metadata_fmid_toolparams_tid_)
* [get_api_v1_files_id_prov_freeform](#get_api_v1_files_id_prov_freeform)
* [post_api_v1_files_id_prov_freeform](#post_api_v1_files_id_prov_freeform)
* [get_api_v1_files_id_prov_json](#get_api_v1_files_id_prov_json)
* [post_api_v1_files_id_prov_json](#post_api_v1_files_id_prov_json)
* [delete_api_v1_files_id_prov_json](#delete_api_v1_files_id_prov_json)
* [post_api_v1_files_id_redetect](#post_api_v1_files_id_redetect)
* [post_api_v1_files_id_reingest](#post_api_v1_files_id_reingest)
* [post_api_v1_files_id_replace](#post_api_v1_files_id_replace)
* [put_api_v1_files_id_restrict](#put_api_v1_files_id_restrict)
* [post_api_v1_files_id_uningest](#post_api_v1_files_id_uningest)

## get_api_v1_files_fixity_algorithm

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_fixity_algorithm()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1FilesFixityAlgorithmResponse](../../models/operations/getapiv1filesfixityalgorithmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDResponse](../../models/operations/getapiv1filesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_files_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.delete_api_v1_files_id_(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1FilesIDResponse](../../models/operations/deleteapiv1filesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_data_tables

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_data_tables(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDDataTablesResponse](../../models/operations/getapiv1filesiddatatablesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_download_count

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_download_count(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDDownloadCountResponse](../../models/operations/getapiv1filesiddownloadcountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_draft

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_draft(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDDraftResponse](../../models/operations/getapiv1filesiddraftresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_extract_ncml

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_extract_ncml(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1FilesIDExtractNcmlResponse](../../models/operations/postapiv1filesidextractncmlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_has_been_deleted

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_has_been_deleted(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDHasBeenDeletedResponse](../../models/operations/getapiv1filesidhasbeendeletedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_metadata

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_metadata(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDMetadataResponse](../../models/operations/getapiv1filesidmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_metadata

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_metadata(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1FilesIDMetadataResponse](../../models/operations/postapiv1filesidmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_metadata_categories

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_metadata_categories(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1FilesIDMetadataCategoriesResponse](../../models/operations/postapiv1filesidmetadatacategoriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_metadata_draft

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_metadata_draft(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDMetadataDraftResponse](../../models/operations/getapiv1filesidmetadatadraftresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_metadata_tabular_tags

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_metadata_tabular_tags(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1FilesIDMetadataTabularTagsResponse](../../models/operations/postapiv1filesidmetadatatabulartagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_metadata_fmid_toolparams_tid_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_metadata_fmid_toolparams_tid_(fmid=505910, id='<value>', tid=735941, locale='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `fmid`             | *int*              | :heavy_check_mark: | N/A                |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `tid`              | *int*              | :heavy_check_mark: | N/A                |
| `locale`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1FilesIDMetadataFmidToolparamsTidResponse](../../models/operations/getapiv1filesidmetadatafmidtoolparamstidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_prov_freeform

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_prov_freeform(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDProvFreeformResponse](../../models/operations/getapiv1filesidprovfreeformresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_prov_freeform

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_prov_freeform(id='<value>', request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1FilesIDProvFreeformResponse](../../models/operations/postapiv1filesidprovfreeformresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_files_id_prov_json

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.get_api_v1_files_id_prov_json(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1FilesIDProvJSONResponse](../../models/operations/getapiv1filesidprovjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_prov_json

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_prov_json(id='<value>', entity_name='<value>', request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `entity_name`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1FilesIDProvJSONResponse](../../models/operations/postapiv1filesidprovjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_files_id_prov_json

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.delete_api_v1_files_id_prov_json(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1FilesIDProvJSONResponse](../../models/operations/deleteapiv1filesidprovjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_redetect

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_redetect(id='<value>', dry_run=False)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `dry_run`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1FilesIDRedetectResponse](../../models/operations/postapiv1filesidredetectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_reingest

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_reingest(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1FilesIDReingestResponse](../../models/operations/postapiv1filesidreingestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_replace

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_replace(id='<value>', request_body=operations.PostAPIV1FilesIDReplaceRequestBody())

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `request_body`                                                                                                           | [Optional[operations.PostAPIV1FilesIDReplaceRequestBody]](../../models/operations/postapiv1filesidreplacerequestbody.md) | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |


### Response

**[operations.PostAPIV1FilesIDReplaceResponse](../../models/operations/postapiv1filesidreplaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_files_id_restrict

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.put_api_v1_files_id_restrict(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1FilesIDRestrictResponse](../../models/operations/putapiv1filesidrestrictresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_files_id_uningest

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.files.post_api_v1_files_id_uningest(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1FilesIDUningestResponse](../../models/operations/postapiv1filesiduningestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
