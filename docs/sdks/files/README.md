# Files
(*files*)

## Overview

### Available Operations

* [get_fixity_algorithm](#get_fixity_algorithm) - Retrieve the fixity algorithm of a file
* [get_file](#get_file) - Retrieve a specific file by ID.
* [delete_file](#delete_file) - Delete a specific file by ID.
* [get_file_data_tables](#get_file_data_tables) - Retrieve the data tables of a given file
* [get_download_count](#get_download_count) - Retrieve the download count of a file
* [get_file_draft](#get_file_draft) - Retrieve a file in draft mode by its ID
* [extract_ncml_by_id](#extract_ncml_by_id) - Extract Ncml information of a file based on the provided id
* [check_file_deletion_status](#check_file_deletion_status) - Check if specified file has been deleted
* [get_file_metadata](#get_file_metadata) - Retrieves metadata for a specific file
* [update_file_metadata](#update_file_metadata) - Updates metadata for a specific file
* [post_file_metadata_categories](#post_file_metadata_categories) - Adds new metadata categories for a specific file.
* [get_draft_meta_data](#get_draft_meta_data) - Retrieve the metadata of a draft file
* [post_tabular_tags](#post_tabular_tags) - Add tabular tags to a file metadata
* [get_file_metadata_tool_params](#get_file_metadata_tool_params) - Retrieves tool parameters for a specific file metadata ID
* [get_file_prov_freeform](#get_file_prov_freeform) - Retrieves the freeform provenance data for a specific file
* [post_file_prov_freeform](#post_file_prov_freeform) - Posts freeform provenance data for a specific file
* [get_file_prov_json](#get_file_prov_json) - Retrieving the PROV JSON of a specific file
* [post_file_prov_json](#post_file_prov_json) - Submit a new PROV JSON for a specific file
* [delete_file_prov_json](#delete_file_prov_json) - Delete the PROV JSON of a specific file
* [redetect_file](#redetect_file) - Invoke redetection process for the specified file
* [reingest_file](#reingest_file) - Reingest a file using its ID
* [replace_file](#replace_file) - Replace an existing file with a new version
* [restrict_file_access](#restrict_file_access) - Restrict access to a specific file
* [post_file_uningest](#post_file_uningest) - Uningest a file with the specified ID

## get_fixity_algorithm

Retrieve the fixity algorithm of a file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_fixity_algorithm()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetFixityAlgorithmResponse](../../models/operations/getfixityalgorithmresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_file

Retrieve a specific file by ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_file(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetFileResponse](../../models/operations/getfileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_file

Delete a specific file by ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.delete_file(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteFileResponse](../../models/operations/deletefileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_file_data_tables

Retrieve the data tables of a given file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_file_data_tables(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetFileDataTablesResponse](../../models/operations/getfiledatatablesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_download_count

Retrieve the download count of a file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_download_count(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDownloadCountResponse](../../models/operations/getdownloadcountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_file_draft

Retrieve a file in draft mode by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_file_draft(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetFileDraftResponse](../../models/operations/getfiledraftresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## extract_ncml_by_id

Extract Ncml information of a file based on the provided id

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.extract_ncml_by_id(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.ExtractNcmlByIDResponse](../../models/operations/extractncmlbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## check_file_deletion_status

Check if specified file has been deleted

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.check_file_deletion_status(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.CheckFileDeletionStatusResponse](../../models/operations/checkfiledeletionstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_file_metadata

Retrieves metadata for a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_file_metadata(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetFileMetadataResponse](../../models/operations/getfilemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_file_metadata

Updates metadata for a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.update_file_metadata(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateFileMetadataResponse](../../models/operations/updatefilemetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_file_metadata_categories

Adds new metadata categories for a specific file.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.post_file_metadata_categories(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.PostFileMetadataCategoriesResponse](../../models/operations/postfilemetadatacategoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_draft_meta_data

Retrieve the metadata of a draft file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_draft_meta_data(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDraftMetaDataResponse](../../models/operations/getdraftmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_tabular_tags

Add tabular tags to a file metadata

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.post_tabular_tags(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.PostTabularTagsResponse](../../models/operations/posttabulartagsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_file_metadata_tool_params

Retrieves tool parameters for a specific file metadata ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_file_metadata_tool_params(fmid=27570, id='<id>', tid=57707)

if res is not None:
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

**[operations.GetFileMetadataToolParamsResponse](../../models/operations/getfilemetadatatoolparamsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_file_prov_freeform

Retrieves the freeform provenance data for a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_file_prov_freeform(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetFileProvFreeformResponse](../../models/operations/getfileprovfreeformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_file_prov_freeform

Posts freeform provenance data for a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.post_file_prov_freeform(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.PostFileProvFreeformResponse](../../models/operations/postfileprovfreeformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_file_prov_json

Retrieving the PROV JSON of a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.get_file_prov_json(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetFileProvJSONResponse](../../models/operations/getfileprovjsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_file_prov_json

Submit a new PROV JSON for a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.post_file_prov_json(id='<id>')

if res is not None:
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

**[operations.PostFileProvJSONResponse](../../models/operations/postfileprovjsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_file_prov_json

Delete the PROV JSON of a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.delete_file_prov_json(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteFileProvJSONResponse](../../models/operations/deletefileprovjsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## redetect_file

Invoke redetection process for the specified file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.redetect_file(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `dry_run`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |

### Response

**[operations.RedetectFileResponse](../../models/operations/redetectfileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## reingest_file

Reingest a file using its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.reingest_file(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.ReingestFileResponse](../../models/operations/reingestfileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## replace_file

Replace an existing file with a new version

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.replace_file(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `id`                                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `request_body`                                                                                   | [Optional[operations.ReplaceFileRequestBody]](../../models/operations/replacefilerequestbody.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |

### Response

**[operations.ReplaceFileResponse](../../models/operations/replacefileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## restrict_file_access

Restrict access to a specific file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.restrict_file_access(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.RestrictFileAccessResponse](../../models/operations/restrictfileaccessresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_file_uningest

Uningest a file with the specified ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.files.post_file_uningest(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.PostFileUningestResponse](../../models/operations/postfileuningestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |