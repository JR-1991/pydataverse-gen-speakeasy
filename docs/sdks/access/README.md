# Access
(*access*)

### Available Operations

* [get_api_v1_access_datafile_bundle_file_id_](#get_api_v1_access_datafile_bundle_file_id_)
* [get_api_v1_access_datafile_file_id_](#get_api_v1_access_datafile_file_id_)
* [get_api_v1_access_datafile_file_id_auxiliary](#get_api_v1_access_datafile_file_id_auxiliary)
* [get_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_](#get_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_)
* [post_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_](#post_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_)
* [delete_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_](#delete_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_)
* [get_api_v1_access_datafile_file_id_auxiliary_origin_](#get_api_v1_access_datafile_file_id_auxiliary_origin_)
* [get_api_v1_access_datafile_file_id_metadata](#get_api_v1_access_datafile_file_id_metadata)
* [get_api_v1_access_datafile_file_id_metadata_ddi](#get_api_v1_access_datafile_file_id_metadata_ddi)
* [put_api_v1_access_datafile_id_grant_access_identifier_](#put_api_v1_access_datafile_id_grant_access_identifier_)
* [get_api_v1_access_datafile_id_list_requests](#get_api_v1_access_datafile_id_list_requests)
* [put_api_v1_access_datafile_id_reject_access_identifier_](#put_api_v1_access_datafile_id_reject_access_identifier_)
* [put_api_v1_access_datafile_id_request_access](#put_api_v1_access_datafile_id_request_access)
* [delete_api_v1_access_datafile_id_revoke_access_identifier_](#delete_api_v1_access_datafile_id_revoke_access_identifier_)
* [get_api_v1_access_datafile_id_user_file_access_requested](#get_api_v1_access_datafile_id_user_file_access_requested)
* [get_api_v1_access_datafile_id_user_permissions](#get_api_v1_access_datafile_id_user_permissions)
* [post_api_v1_access_datafiles](#post_api_v1_access_datafiles)
* [get_api_v1_access_datafiles_file_ids_](#get_api_v1_access_datafiles_file_ids_)
* [get_api_v1_access_dataset_id_](#get_api_v1_access_dataset_id_)
* [get_api_v1_access_dataset_id_versions_version_id_](#get_api_v1_access_dataset_id_versions_version_id_)
* [get_api_v1_access_ds_card_image_version_id_](#get_api_v1_access_ds_card_image_version_id_)
* [get_api_v1_access_dv_card_image_dataverse_id_](#get_api_v1_access_dv_card_image_dataverse_id_)
* [get_api_v1_access_file_card_image_file_id_](#get_api_v1_access_file_card_image_file_id_)
* [put_api_v1_access_id_allow_access_request](#put_api_v1_access_id_allow_access_request)

## get_api_v1_access_datafile_bundle_file_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_bundle_file_id_(file_id='<value>', file_metadata_id=793125, gbrecs=False)

if res.body is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `file_metadata_id` | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileBundleFileIDResponse](../../models/operations/getapiv1accessdatafilebundlefileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_file_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_file_id_(file_id='<value>', gbrecs=False)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileFileIDResponse](../../models/operations/getapiv1accessdatafilefileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_file_id_auxiliary

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_file_id_auxiliary(file_id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileFileIDAuxiliaryResponse](../../models/operations/getapiv1accessdatafilefileidauxiliaryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_(file_id='<value>', format_tag='<value>', format_version='<value>')

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `format_tag`       | *str*              | :heavy_check_mark: | N/A                |
| `format_version`   | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileFileIDAuxiliaryFormatTagFormatVersionResponse](../../models/operations/getapiv1accessdatafilefileidauxiliaryformattagformatversionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse()


res = s.access.post_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_(file_id=398096, format_tag='<value>', format_version='<value>', request_body=operations.PostAPIV1AccessDatafileFileIDAuxiliaryFormatTagFormatVersionRequestBody())

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file_id`                                                                                                                                                                                          | *int*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `format_tag`                                                                                                                                                                                       | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `format_version`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `request_body`                                                                                                                                                                                     | [Optional[operations.PostAPIV1AccessDatafileFileIDAuxiliaryFormatTagFormatVersionRequestBody]](../../models/operations/postapiv1accessdatafilefileidauxiliaryformattagformatversionrequestbody.md) | :heavy_minus_sign:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |


### Response

**[operations.PostAPIV1AccessDatafileFileIDAuxiliaryFormatTagFormatVersionResponse](../../models/operations/postapiv1accessdatafilefileidauxiliaryformattagformatversionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.delete_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_(file_id=417724, format_tag='<value>', format_version='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *int*              | :heavy_check_mark: | N/A                |
| `format_tag`       | *str*              | :heavy_check_mark: | N/A                |
| `format_version`   | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1AccessDatafileFileIDAuxiliaryFormatTagFormatVersionResponse](../../models/operations/deleteapiv1accessdatafilefileidauxiliaryformattagformatversionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_file_id_auxiliary_origin_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_file_id_auxiliary_origin_(file_id='<value>', origin='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `origin`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileFileIDAuxiliaryOriginResponse](../../models/operations/getapiv1accessdatafilefileidauxiliaryoriginresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_file_id_metadata

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_file_id_metadata(file_id='<value>', exclude='<value>', file_metadata_id=700338, include='<value>')

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `exclude`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `file_metadata_id` | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `include`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileFileIDMetadataResponse](../../models/operations/getapiv1accessdatafilefileidmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_file_id_metadata_ddi

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_file_id_metadata_ddi(file_id='<value>', exclude='<value>', file_metadata_id=709213, include='<value>')

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `exclude`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `file_metadata_id` | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `include`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileFileIDMetadataDdiResponse](../../models/operations/getapiv1accessdatafilefileidmetadataddiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_access_datafile_id_grant_access_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.put_api_v1_access_datafile_id_grant_access_identifier_(id='<value>', identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1AccessDatafileIDGrantAccessIdentifierResponse](../../models/operations/putapiv1accessdatafileidgrantaccessidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_id_list_requests

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_id_list_requests(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileIDListRequestsResponse](../../models/operations/getapiv1accessdatafileidlistrequestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_access_datafile_id_reject_access_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.put_api_v1_access_datafile_id_reject_access_identifier_(id='<value>', identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1AccessDatafileIDRejectAccessIdentifierResponse](../../models/operations/putapiv1accessdatafileidrejectaccessidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_access_datafile_id_request_access

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.put_api_v1_access_datafile_id_request_access(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1AccessDatafileIDRequestAccessResponse](../../models/operations/putapiv1accessdatafileidrequestaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_access_datafile_id_revoke_access_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.delete_api_v1_access_datafile_id_revoke_access_identifier_(id='<value>', identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1AccessDatafileIDRevokeAccessIdentifierResponse](../../models/operations/deleteapiv1accessdatafileidrevokeaccessidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_id_user_file_access_requested

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_id_user_file_access_requested(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileIDUserFileAccessRequestedResponse](../../models/operations/getapiv1accessdatafileiduserfileaccessrequestedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafile_id_user_permissions

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_id_user_permissions(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafileIDUserPermissionsResponse](../../models/operations/getapiv1accessdatafileiduserpermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_access_datafiles

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.post_api_v1_access_datafiles(gbrecs=False, request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1AccessDatafilesResponse](../../models/operations/postapiv1accessdatafilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_datafiles_file_ids_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafiles_file_ids_(file_ids='<value>', gbrecs=False)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_ids`         | *str*              | :heavy_check_mark: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1AccessDatafilesFileIdsResponse](../../models/operations/getapiv1accessdatafilesfileidsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_dataset_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_dataset_id_(id='<value>', gbrecs=False)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1AccessDatasetIDResponse](../../models/operations/getapiv1accessdatasetidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_dataset_id_versions_version_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_dataset_id_versions_version_id_(id='<value>', version_id='<value>', gbrecs=False, key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_id`       | *str*              | :heavy_check_mark: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1AccessDatasetIDVersionsVersionIDResponse](../../models/operations/getapiv1accessdatasetidversionsversionidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_ds_card_image_version_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_ds_card_image_version_id_(version_id=597512)

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `version_id`       | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDsCardImageVersionIDResponse](../../models/operations/getapiv1accessdscardimageversionidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_dv_card_image_dataverse_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_dv_card_image_dataverse_id_(dataverse_id=799966)

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dataverse_id`     | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessDvCardImageDataverseIDResponse](../../models/operations/getapiv1accessdvcardimagedataverseidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_access_file_card_image_file_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_file_card_image_file_id_(file_id=203069)

if res.res is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1AccessFileCardImageFileIDResponse](../../models/operations/getapiv1accessfilecardimagefileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_access_id_allow_access_request

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.put_api_v1_access_id_allow_access_request(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1AccessIDAllowAccessRequestResponse](../../models/operations/putapiv1accessidallowaccessrequestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
