# Access
(*access*)

### Available Operations

* [get_datafile_bundle](#get_datafile_bundle) - Retrieve a zip of the datafile bundle identified by the file ID.
* [get_datafile](#get_datafile) - Retrieves datafile details based on given fileId
* [get_datafile_auxiliary](#get_datafile_auxiliary) - Retrieve auxiliary data for a specific datafile.
* [access_datafile_auxiliary_get](#access_datafile_auxiliary_get) - Retrieve details of a specific auxiliary data file
* [access_datafile_auxiliary_create](#access_datafile_auxiliary_create) - Create a new auxiliary data file for a particular data file
* [access_datafile_auxiliary_delete](#access_datafile_auxiliary_delete) - Delete a specific auxiliary data file
* [get_datafile_auxiliary_info](#get_datafile_auxiliary_info) - Retrieve auxiliary information of specific datafile
* [get_datafile_metadata](#get_datafile_metadata) - Retrieve metadata for a specific datafile
* [get_datafile_meta_ddi](#get_datafile_meta_ddi) - Retrieve DDI metadata for a specific datafile.
* [grant_datafile_access](#grant_datafile_access) - Grants access to a specific datafile using its ID and the identifier of the user
* [get_datafile_requests](#get_datafile_requests) - Retrieves a list of all requests relevant to a specified datafile
* [reject_data_access](#reject_data_access) - Reject access to specified datafile using ids
* [request_file_access](#request_file_access) - Requests access to a specific datafile by ID.
* [delete_file_access](#delete_file_access) - Revoke access to a specific file using its ID and an identifier
* [get_user_file_access_requested](#get_user_file_access_requested) - Retrieve the status of a user file access request
* [get_user_file_permissions](#get_user_file_permissions) - Retrieve user permissions for a specific datafile.
* [post_data_file_access](#post_data_file_access) - Uploads access details of a data file
* [get_access_data_files](#get_access_data_files) - Retrieve access data for specified files
* [get_dataset_access](#get_dataset_access) - Retrieve access information for a specific dataset
* [get_dataset_version_access](#get_dataset_version_access) - Retrieve specific version of an accessible dataset by ID
* [get_ds_card_image](#get_ds_card_image) - Retrieves the version-specific Data Card image
* [get_dataverse_card_image](#get_dataverse_card_image) - Fetch the Dataverse card image
* [get_file_card_image](#get_file_card_image) - Retrieves the card image for the specified file ID.
* [allow_access_request](#allow_access_request) - Update permission to allow access request based on the provided ID

## get_datafile_bundle

Retrieve a zip of the datafile bundle identified by the file ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_bundle(file_id='<value>')

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

**[operations.GetDatafileBundleResponse](../../models/operations/getdatafilebundleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_datafile

Retrieves datafile details based on given fileId

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile(file_id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDatafileResponse](../../models/operations/getdatafileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_datafile_auxiliary

Retrieve auxiliary data for a specific datafile.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_auxiliary(file_id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDatafileAuxiliaryResponse](../../models/operations/getdatafileauxiliaryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## access_datafile_auxiliary_get

Retrieve details of a specific auxiliary data file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.access_datafile_auxiliary_get(file_id='<value>', format_tag='<value>', format_version='<value>')

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

**[operations.AccessDatafileAuxiliaryGetResponse](../../models/operations/accessdatafileauxiliarygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## access_datafile_auxiliary_create

Create a new auxiliary data file for a particular data file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.access_datafile_auxiliary_create(file_id=7002, format_tag='<value>', format_version='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `file_id`                                                                                                                            | *int*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |
| `format_tag`                                                                                                                         | *str*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |
| `format_version`                                                                                                                     | *str*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |
| `request_body`                                                                                                                       | [Optional[operations.AccessDatafileAuxiliaryCreateRequestBody]](../../models/operations/accessdatafileauxiliarycreaterequestbody.md) | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |


### Response

**[operations.AccessDatafileAuxiliaryCreateResponse](../../models/operations/accessdatafileauxiliarycreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## access_datafile_auxiliary_delete

Delete a specific auxiliary data file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.access_datafile_auxiliary_delete(file_id=458810, format_tag='<value>', format_version='<value>')

if res is not None:
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

**[operations.AccessDatafileAuxiliaryDeleteResponse](../../models/operations/accessdatafileauxiliarydeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_datafile_auxiliary_info

Retrieve auxiliary information of specific datafile

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_auxiliary_info(file_id='<value>', origin='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |
| `origin`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDatafileAuxiliaryInfoResponse](../../models/operations/getdatafileauxiliaryinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_datafile_metadata

Retrieve metadata for a specific datafile

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_metadata(file_id='<value>')

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

**[operations.GetDatafileMetadataResponse](../../models/operations/getdatafilemetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_datafile_meta_ddi

Retrieve DDI metadata for a specific datafile.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_meta_ddi(file_id='<value>')

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

**[operations.GetDatafileMetaDDIResponse](../../models/operations/getdatafilemetaddiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## grant_datafile_access

Grants access to a specific datafile using its ID and the identifier of the user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.grant_datafile_access(id='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GrantDatafileAccessResponse](../../models/operations/grantdatafileaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_datafile_requests

Retrieves a list of all requests relevant to a specified datafile

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_requests(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDatafileRequestsResponse](../../models/operations/getdatafilerequestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## reject_data_access

Reject access to specified datafile using ids

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.reject_data_access(id='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RejectDataAccessResponse](../../models/operations/rejectdataaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## request_file_access

Requests access to a specific datafile by ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.request_file_access(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RequestFileAccessResponse](../../models/operations/requestfileaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_file_access

Revoke access to a specific file using its ID and an identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.delete_file_access(id='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteFileAccessResponse](../../models/operations/deletefileaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_user_file_access_requested

Retrieve the status of a user file access request

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_user_file_access_requested(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetUserFileAccessRequestedResponse](../../models/operations/getuserfileaccessrequestedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_user_file_permissions

Retrieve user permissions for a specific datafile.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_user_file_permissions(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetUserFilePermissionsResponse](../../models/operations/getuserfilepermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_data_file_access

Uploads access details of a data file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.post_data_file_access()

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostDataFileAccessResponse](../../models/operations/postdatafileaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_access_data_files

Retrieve access data for specified files

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_access_data_files(file_ids='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_ids`         | *str*              | :heavy_check_mark: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAccessDataFilesResponse](../../models/operations/getaccessdatafilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_dataset_access

Retrieve access information for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_dataset_access(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `gbrecs`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDatasetAccessResponse](../../models/operations/getdatasetaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_dataset_version_access

Retrieve specific version of an accessible dataset by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_dataset_version_access(id='<value>', version_id='<value>')

if res is not None:
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

**[operations.GetDatasetVersionAccessResponse](../../models/operations/getdatasetversionaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ds_card_image

Retrieves the version-specific Data Card image

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_ds_card_image(version_id=856190)

if res.res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `version_id`       | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDsCardImageResponse](../../models/operations/getdscardimageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_dataverse_card_image

Fetch the Dataverse card image

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_dataverse_card_image(dataverse_id=305707)

if res.res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dataverse_id`     | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDataverseCardImageResponse](../../models/operations/getdataversecardimageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_file_card_image

Retrieves the card image for the specified file ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_file_card_image(file_id=259222)

if res.res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFileCardImageResponse](../../models/operations/getfilecardimageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## allow_access_request

Update permission to allow access request based on the provided ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.allow_access_request(id='<value>')

if res is not None:
    # handle response
    pass

```



### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.AllowAccessRequestResponse](../../models/operations/allowaccessrequestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
