# Datasets
(*datasets*)

## Overview

### Available Operations

* [get_datasets_export](#get_datasets_export) - Retrieves export information of a dataset given its exporter and persistent ID
* [get_curation_states](#get_curation_states) - Retrieve a list of curation states for datasets
* [get_dataset_locks](#get_dataset_locks) - Retrieve information about locks on datasets
* [modify_all_registrations](#modify_all_registrations) - Modifies registration details for all datasets
* [get_registration_pid_metadata](#get_registration_pid_metadata) - Retrieve registration PID metadata of all datasets
* [update_dataset_upload](#update_dataset_upload) - Update a multi-part upload for a dataset using the provided global ID, storage identifier, and upload ID
* [delete_dataset_upload](#delete_dataset_upload) - Delete a multi-part upload for a dataset using the provided global ID, storage identifier, and upload ID
* [get_private_url_dataset_version](#get_private_url_dataset_version) - Retrieves a dataset version using a private URL token
* [get_citation_by_private_url](#get_citation_by_private_url) - Retrieve citation information for a dataset version via a private URL token
* [get_summary_field_names](#get_summary_field_names) - Retrieve names of summary fields in the dataset
* [delete_dataset_link](#delete_dataset_link) - Delete a link between a dataset and a dataverse
* [get_allowed_curation_labels](#get_allowed_curation_labels) - Retrieve a list of allowed curation labels for a specific dataset
* [get_dataset_assignments](#get_dataset_assignments) - Retrieves assignments for a specific dataset
* [create_dataset_assignment](#create_dataset_assignment) - Creates an assignment for a specific dataset
* [delete_assignment](#delete_assignment) - Delete a specific assignment for a dataset
* [get_curation_label_set_1](#get_curation_label_set_1) - Retrieves the curation label set of the specified dataset
* [update_curation_label_set_1](#update_curation_label_set_1) - Updates the curation label set of the specified dataset
* [delete_curation_label_set_1](#delete_curation_label_set_1) - Deletes the curation label set for the specified dataset
* [validate_checksum](#validate_checksum) - Validate checksum for specified dataset
* [get_rsync_data_module](#get_rsync_data_module) - Retrieve the Rsync data capture module for a specific dataset
* [get_guestbook_entry](#get_guestbook_entry) - Retrieves a guestbook entry for a specific dataset
* [update_guestbook_entry](#update_guestbook_entry) - Updates a guestbook entry for a specific dataset
* [delete_guestbook_entry](#delete_guestbook_entry) - Deletes a guestbook entry for a specific dataset
* [lock_dataset](#lock_dataset) - Lock a specific dataset identified by the given identifier and type
* [get_dataset_locks_1](#get_dataset_locks_1) - Retrieves specific dataset locks
* [delete_dataset_locks](#delete_dataset_locks) - Deletes specific dataset locks
* [get_storage_driver_1](#get_storage_driver_1) - Retrieve the details of a specific storage driver based on the provided identifier
* [update_storage_driver_1](#update_storage_driver_1) - Update the details of a specific storage driver based on the provided identifier
* [delete_storage_driver_1](#delete_storage_driver_1) - Delete a specific storage driver based on the provided identifier
* [get_dataset_storage_size](#get_dataset_storage_size) - Retrieves the storage size of a dataset based on its identifier. An optional query parameter can be used to include cached files.
* [get_dataset_timestamps](#get_dataset_timestamps) - Retrieves the timestamps for a given dataset identified by the path parameter 'identifier'
* [get_download_size](#get_download_size) - Retrieve the download size of a specific version of a dataset
* [get_dataset](#get_dataset) - Retrieve the specified dataset
* [delete_dataset](#delete_dataset) - Delete the specified dataset
* [~~get_publish_dataset~~](#get_publish_dataset) - Retrieve publishing details of a designated dataset :warning: **Deprecated**
* [initiate_publishing](#initiate_publishing) - Publish a designated dataset with optional assurances
* [release_migrated_dataset](#release_migrated_dataset) - Release a migrated dataset with a specified ID
* [add_dataset](#add_dataset) - Add a new dataset to the existing record
* [add_files_to_dataset](#add_files_to_dataset) - Adds files to a specified dataset
* [add_globus_files_to_dataset](#add_globus_files_to_dataset) - Add globus files to a specific dataset
* [update_citation_date](#update_citation_date) - Update the citation date of a dataset based on dataset ID
* [delete_citation_date](#delete_citation_date) - Delete citation date of a dataset based on dataset ID
* [get_clean_storage_status](#get_clean_storage_status) - Get the status of the clean storage task for the specified dataset
* [get_curation_status](#get_curation_status) - Fetches the curation status of the specified dataset
* [update_curation_status](#update_curation_status) - Updates the curation status of the specified dataset
* [delete_curation_status](#delete_curation_status) - Deletes the curation status of the specified dataset
* [update_dataset_metadata](#update_dataset_metadata) - Update the metadata of a specific dataset
* [delete_dataset_1](#delete_dataset_1) - Delete a specific dataset by its ID.
* [get_dataset_directory_index](#get_dataset_directory_index) - Retrieve directory index of a dataset
* [edit_dataset_metadata](#edit_dataset_metadata) - Updates the metadata of a specific dataset represented by its ID
* [set_dataset_embargo](#set_dataset_embargo) - Set an embargo on a specific dataset's files
* [unset_embargo_on_dataset_files](#unset_embargo_on_dataset_files) - Unset embargo on files for a specific dataset
* [get_globus_download_parameters](#get_globus_download_parameters) - Retrieve the parameters for Globus download for a specified dataset
* [get_globus_upload_parameters](#get_globus_upload_parameters) - Retrieves Globus upload parameters for a specific dataset
* [get_dataset_links](#get_dataset_links) - Retrieves the links of a specified dataset
* [get_dataset_logo](#get_dataset_logo) - Retrieve the logo of a specific dataset
* [dataset_citation_count_get](#dataset_citation_count_get) - Retrieves the citation count for a specific dataset
* [get_dataset_metrics](#get_dataset_metrics) - Retrieve specific metrics for a specified dataset
* [get_dataset_metric](#get_dataset_metric) - Fetches a specific metric for a specific dataset
* [get_dataset_metadata](#get_dataset_metadata) - Retrieves the metadata of a dataset by its ID
* [update_dataset_metadata_1](#update_dataset_metadata_1) - Updates the metadata of a dataset by its ID, with an option to replace the existing metadata
* [update_metadata_deletion](#update_metadata_deletion) - Update the deletion status of the metadata of a specific dataset
* [get_registration_modification](#get_registration_modification) - Retrieve the modification details of a specific dataset registration
* [modify_dataset_registration_metadata](#modify_dataset_registration_metadata) - Modify the registration metadata of a specific dataset
* [monitor_globus_download](#monitor_globus_download) - Initiate the process to monitor a Globus download operation for a specific dataset
* [move_dataset_to_target](#move_dataset_to_target) - Moves a specific dataset to a target dataverse
* [get_private_url](#get_private_url) - Retrieve a specific dataset's private URL
* [create_private_url](#create_private_url) - Create a private URL for a specific dataset
* [delete_private_url](#delete_private_url) - Delete a specific dataset's private URL
* [replace_dataset_files](#replace_dataset_files) - Replace files in a specified dataset
* [submit_globus_download_request](#submit_globus_download_request) - Submit a request for Globus download for a specific dataset
* [post_globus_upload_paths_request](#post_globus_upload_paths_request) - Submit a request to get the paths for Globus file upload for a specified dataset
* [return_dataset_to_author](#return_dataset_to_author) - Returns the specified dataset back to its author
* [submit_dataset_for_review](#submit_dataset_for_review) - Submits a specified dataset for review
* [get_dataset_thumbnail](#get_dataset_thumbnail) - Retrieves a thumbnail from a specific dataset
* [post_dataset_thumbnail](#post_dataset_thumbnail) - Adds a thumbnail to a specific dataset
* [delete_dataset_thumbnail](#delete_dataset_thumbnail) - Deletes a thumbnail from a specific dataset
* [get_thumbnail_candidates](#get_thumbnail_candidates) - Retrieve the list of thumbnail candidates for a specific dataset
* [post_thumbnail_data](#post_thumbnail_data) - Upload a new thumbnail for a specific dataset
* [~~get_upload_id~~](#get_upload_id) - Retrieve the upload ID for the specified dataset :warning: **Deprecated**
* [get_upload_ur_ls](#get_upload_ur_ls) - Retrieve upload URLs for a specific dataset
* [get_user_permissions](#get_user_permissions) - Retrieve user permissions for a specific dataset
* [get_dataset_versions](#get_dataset_versions) - Retrieve versions of a specific dataset
* [get_dataset_version](#get_dataset_version) - Fetches the dataset version details, with options to exclude files or include deaccessioned ones
* [update_dataset_version](#update_dataset_version) - Updates the dataset version with the given ID
* [delete_dataset_version](#delete_dataset_version) - Deletes the specified version of a dataset
* [check_dataset_file_download_permission](#check_dataset_file_download_permission) - Checks if a user has permission to download at least one file from a specific dataset version
* [get_citation](#get_citation) - Retrieve the citation of a specific dataset version
* [get_custom_license](#get_custom_license) - Retrieve a specific dataset version's custom license
* [post_deaccession_dataset_by_version_id](#post_deaccession_dataset_by_version_id) - Remove access to a specific version of a dataset
* [get_dataset_version_files](#get_dataset_version_files) - Fetches files within a specific version of a dataset
* [get_dataset_files_count](#get_dataset_files_count) - Retrieve counts of various types of files in a specified dataset version
* [get_dataset_version_linkset](#get_dataset_version_linkset) - Retrieve linkset of a specific dataset version
* [get_dataset_version_metadata](#get_dataset_version_metadata) - Retrieve the metadata of a specific version of a dataset
* [get_dataset_version_metadata_1](#get_dataset_version_metadata_1) - Retrieve metadata of a specified version of a dataset
* [get_dataset_version_tool_param](#get_dataset_version_tool_param) - Retrieve tool parameters of a specific version of a dataset
* [get_dataset_archival_status](#get_dataset_archival_status) - Retrieve the archival status of a specific version of a dataset
* [update_dataset_archival_status](#update_dataset_archival_status) - Update the archival status of a specific version of a dataset
* [delete_dataset_archival_status](#delete_dataset_archival_status) - Remove the archival status of a specific version of a dataset
* [update_dataset_link](#update_dataset_link) - Updates the link between a dataset and a Dataverse alias

## get_datasets_export

Retrieves export information of a dataset given its exporter and persistent ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_datasets_export()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `exporter`         | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `persistent_id`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetsExportResponse](../../models/operations/getdatasetsexportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_curation_states

Retrieve a list of curation states for datasets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_curation_states()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetCurationStatesResponse](../../models/operations/getcurationstatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_locks

Retrieve information about locks on datasets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_locks()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `user_identifier`  | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetLocksResponse](../../models/operations/getdatasetlocksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## modify_all_registrations

Modifies registration details for all datasets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.modify_all_registrations()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.ModifyAllRegistrationsResponse](../../models/operations/modifyallregistrationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_registration_pid_metadata

Retrieve registration PID metadata of all datasets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_registration_pid_metadata()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetRegistrationPIDMetadataResponse](../../models/operations/getregistrationpidmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dataset_upload

Update a multi-part upload for a dataset using the provided global ID, storage identifier, and upload ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_dataset_upload()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `globalid`          | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |
| `storageidentifier` | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |
| `uploadid`          | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |

### Response

**[operations.UpdateDatasetUploadResponse](../../models/operations/updatedatasetuploadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset_upload

Delete a multi-part upload for a dataset using the provided global ID, storage identifier, and upload ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset_upload()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `globalid`          | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |
| `storageidentifier` | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |
| `uploadid`          | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |

### Response

**[operations.DeleteDatasetUploadResponse](../../models/operations/deletedatasetuploadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_private_url_dataset_version

Retrieves a dataset version using a private URL token

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_private_url_dataset_version(private_url_token='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `private_url_token` | *str*               | :heavy_check_mark:  | N/A                 |

### Response

**[operations.GetPrivateURLDatasetVersionResponse](../../models/operations/getprivateurldatasetversionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_citation_by_private_url

Retrieve citation information for a dataset version via a private URL token

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_citation_by_private_url(private_url_token='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `private_url_token` | *str*               | :heavy_check_mark:  | N/A                 |

### Response

**[operations.GetCitationByPrivateURLResponse](../../models/operations/getcitationbyprivateurlresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_summary_field_names

Retrieve names of summary fields in the dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_summary_field_names()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetSummaryFieldNamesResponse](../../models/operations/getsummaryfieldnamesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset_link

Delete a link between a dataset and a dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset_link(dataset_id='<value>', linked_dataverse_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `dataset_id`          | *str*                 | :heavy_check_mark:    | N/A                   |
| `linked_dataverse_id` | *str*                 | :heavy_check_mark:    | N/A                   |

### Response

**[operations.DeleteDatasetLinkResponse](../../models/operations/deletedatasetlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_allowed_curation_labels

Retrieve a list of allowed curation labels for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_allowed_curation_labels(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetAllowedCurationLabelsResponse](../../models/operations/getallowedcurationlabelsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_assignments

Retrieves assignments for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_assignments(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetAssignmentsResponse](../../models/operations/getdatasetassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dataset_assignment

Creates an assignment for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.create_dataset_assignment(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.CreateDatasetAssignmentResponse](../../models/operations/createdatasetassignmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_assignment

Delete a specific assignment for a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_assignment(id=246530, identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteAssignmentResponse](../../models/operations/deleteassignmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_curation_label_set_1

Retrieves the curation label set of the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_curation_label_set_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetCurationLabelSet1Response](../../models/operations/getcurationlabelset1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_curation_label_set_1

Updates the curation label set of the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_curation_label_set_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `name`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.UpdateCurationLabelSet1Response](../../models/operations/updatecurationlabelset1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_curation_label_set_1

Deletes the curation label set for the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_curation_label_set_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteCurationLabelSet1Response](../../models/operations/deletecurationlabelset1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## validate_checksum

Validate checksum for specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.validate_checksum(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.ValidateChecksumResponse](../../models/operations/validatechecksumresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_rsync_data_module

Retrieve the Rsync data capture module for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_rsync_data_module(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetRsyncDataModuleResponse](../../models/operations/getrsyncdatamoduleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_guestbook_entry

Retrieves a guestbook entry for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_guestbook_entry(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetGuestbookEntryResponse](../../models/operations/getguestbookentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_guestbook_entry

Updates a guestbook entry for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_guestbook_entry(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateGuestbookEntryResponse](../../models/operations/updateguestbookentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_guestbook_entry

Deletes a guestbook entry for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_guestbook_entry(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteGuestbookEntryResponse](../../models/operations/deleteguestbookentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## lock_dataset

Lock a specific dataset identified by the given identifier and type

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.lock_dataset(identifier='<value>', type='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `type`             | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.LockDatasetResponse](../../models/operations/lockdatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_locks_1

Retrieves specific dataset locks

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_locks_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `type`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetLocks1Response](../../models/operations/getdatasetlocks1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset_locks

Deletes specific dataset locks

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset_locks(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `type`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.DeleteDatasetLocksResponse](../../models/operations/deletedatasetlocksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_storage_driver_1

Retrieve the details of a specific storage driver based on the provided identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_storage_driver_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetStorageDriver1Response](../../models/operations/getstoragedriver1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_storage_driver_1

Update the details of a specific storage driver based on the provided identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_storage_driver_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateStorageDriver1Response](../../models/operations/updatestoragedriver1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_storage_driver_1

Delete a specific storage driver based on the provided identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_storage_driver_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteStorageDriver1Response](../../models/operations/deletestoragedriver1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_storage_size

Retrieves the storage size of a dataset based on its identifier. An optional query parameter can be used to include cached files.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_storage_size(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `include_cached`   | *Optional[bool]*   | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetStorageSizeResponse](../../models/operations/getdatasetstoragesizeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_timestamps

Retrieves the timestamps for a given dataset identified by the path parameter 'identifier'

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_timestamps(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetTimestampsResponse](../../models/operations/getdatasettimestampsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_download_size

Retrieve the download size of a specific version of a dataset

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_download_size(request=operations.GetDownloadSizeRequest(
    identifier='<value>',
    version_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetDownloadSizeRequest](../../models/operations/getdownloadsizerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |

### Response

**[operations.GetDownloadSizeResponse](../../models/operations/getdownloadsizeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset

Retrieve the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetResponse](../../models/operations/getdatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset

Delete the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteDatasetResponse](../../models/operations/deletedatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## ~~get_publish_dataset~~

Retrieve publishing details of a designated dataset

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_publish_dataset(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `type`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetPublishDatasetResponse](../../models/operations/getpublishdatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## initiate_publishing

Publish a designated dataset with optional assurances

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.initiate_publishing(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `id`                | *str*               | :heavy_check_mark:  | N/A                 |
| `assure_is_indexed` | *Optional[bool]*    | :heavy_minus_sign:  | N/A                 |
| `type`              | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |

### Response

**[operations.InitiatePublishingResponse](../../models/operations/initiatepublishingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## release_migrated_dataset

Release a migrated dataset with a specified ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.release_migrated_dataset(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `id`                  | *str*                 | :heavy_check_mark:    | N/A                   |
| `updatepidatprovider` | *Optional[bool]*      | :heavy_minus_sign:    | N/A                   |
| `request_body`        | *Optional[str]*       | :heavy_minus_sign:    | N/A                   |

### Response

**[operations.ReleaseMigratedDatasetResponse](../../models/operations/releasemigrateddatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_dataset

Add a new dataset to the existing record

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.add_dataset(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `request_body`                                                                                 | [Optional[operations.AddDatasetRequestBody]](../../models/operations/adddatasetrequestbody.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |

### Response

**[operations.AddDatasetResponse](../../models/operations/adddatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_files_to_dataset

Adds files to a specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.add_files_to_dataset(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                         | *str*                                                                                                        | :heavy_check_mark:                                                                                           | N/A                                                                                                          |
| `request_body`                                                                                               | [Optional[operations.AddFilesToDatasetRequestBody]](../../models/operations/addfilestodatasetrequestbody.md) | :heavy_minus_sign:                                                                                           | N/A                                                                                                          |

### Response

**[operations.AddFilesToDatasetResponse](../../models/operations/addfilestodatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_globus_files_to_dataset

Add globus files to a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.add_globus_files_to_dataset(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `request_body`                                                                                                           | [Optional[operations.AddGlobusFilesToDatasetRequestBody]](../../models/operations/addglobusfilestodatasetrequestbody.md) | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |

### Response

**[operations.AddGlobusFilesToDatasetResponse](../../models/operations/addglobusfilestodatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_citation_date

Update the citation date of a dataset based on dataset ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_citation_date(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateCitationDateResponse](../../models/operations/updatecitationdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_citation_date

Delete citation date of a dataset based on dataset ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_citation_date(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteCitationDateResponse](../../models/operations/deletecitationdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_clean_storage_status

Get the status of the clean storage task for the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_clean_storage_status(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `dryrun`           | *Optional[bool]*   | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetCleanStorageStatusResponse](../../models/operations/getcleanstoragestatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_curation_status

Fetches the curation status of the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_curation_status(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetCurationStatusResponse](../../models/operations/getcurationstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_curation_status

Updates the curation status of the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_curation_status(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `label`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.UpdateCurationStatusResponse](../../models/operations/updatecurationstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_curation_status

Deletes the curation status of the specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_curation_status(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteCurationStatusResponse](../../models/operations/deletecurationstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dataset_metadata

Update the metadata of a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_dataset_metadata(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateDatasetMetadataResponse](../../models/operations/updatedatasetmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset_1

Delete a specific dataset by its ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset_1(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteDataset1Response](../../models/operations/deletedataset1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_directory_index

Retrieve directory index of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_directory_index(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `folder`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `original`         | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `version`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetDirectoryIndexResponse](../../models/operations/getdatasetdirectoryindexresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## edit_dataset_metadata

Updates the metadata of a specific dataset represented by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.edit_dataset_metadata(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `replace`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |

### Response

**[operations.EditDatasetMetadataResponse](../../models/operations/editdatasetmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set_dataset_embargo

Set an embargo on a specific dataset's files

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.set_dataset_embargo(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.SetDatasetEmbargoResponse](../../models/operations/setdatasetembargoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## unset_embargo_on_dataset_files

Unset embargo on files for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.unset_embargo_on_dataset_files(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UnsetEmbargoOnDatasetFilesResponse](../../models/operations/unsetembargoondatasetfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_globus_download_parameters

Retrieve the parameters for Globus download for a specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_globus_download_parameters(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `download_id`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `locale`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetGlobusDownloadParametersResponse](../../models/operations/getglobusdownloadparametersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_globus_upload_parameters

Retrieves Globus upload parameters for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_globus_upload_parameters(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `locale`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetGlobusUploadParametersResponse](../../models/operations/getglobusuploadparametersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_links

Retrieves the links of a specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_links(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetLinksResponse](../../models/operations/getdatasetlinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_logo

Retrieve the logo of a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_logo(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetLogoResponse](../../models/operations/getdatasetlogoresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## dataset_citation_count_get

Retrieves the citation count for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.dataset_citation_count_get(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DatasetCitationCountGetResponse](../../models/operations/datasetcitationcountgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_metrics

Retrieve specific metrics for a specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_metrics(id='<id>', metric='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetMetricsResponse](../../models/operations/getdatasetmetricsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_metric

Fetches a specific metric for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_metric(id='<id>', metric='<value>', yyyymm='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetMetricResponse](../../models/operations/getdatasetmetricresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_metadata

Retrieves the metadata of a dataset by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_metadata(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetMetadataResponse](../../models/operations/getdatasetmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dataset_metadata_1

Updates the metadata of a dataset by its ID, with an option to replace the existing metadata

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_dataset_metadata_1(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `replace`          | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.UpdateDatasetMetadata1Response](../../models/operations/updatedatasetmetadata1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_metadata_deletion

Update the deletion status of the metadata of a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_metadata_deletion(id='<id>')

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

**[operations.UpdateMetadataDeletionResponse](../../models/operations/updatemetadatadeletionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_registration_modification

Retrieve the modification details of a specific dataset registration

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_registration_modification(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetRegistrationModificationResponse](../../models/operations/getregistrationmodificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## modify_dataset_registration_metadata

Modify the registration metadata of a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.modify_dataset_registration_metadata(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.ModifyDatasetRegistrationMetadataResponse](../../models/operations/modifydatasetregistrationmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## monitor_globus_download

Initiate the process to monitor a Globus download operation for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.monitor_globus_download(id='<id>')

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

**[operations.MonitorGlobusDownloadResponse](../../models/operations/monitorglobusdownloadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## move_dataset_to_target

Moves a specific dataset to a target dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.move_dataset_to_target(id='<id>', target_dataverse_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `id`                     | *str*                    | :heavy_check_mark:       | N/A                      |
| `target_dataverse_alias` | *str*                    | :heavy_check_mark:       | N/A                      |
| `force_move`             | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      |

### Response

**[operations.MoveDatasetToTargetResponse](../../models/operations/movedatasettotargetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_private_url

Retrieve a specific dataset's private URL

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_private_url(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetPrivateURLResponse](../../models/operations/getprivateurlresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_private_url

Create a private URL for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.create_private_url(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `id`                | *str*               | :heavy_check_mark:  | N/A                 |
| `anonymized_access` | *Optional[bool]*    | :heavy_minus_sign:  | N/A                 |

### Response

**[operations.CreatePrivateURLResponse](../../models/operations/createprivateurlresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_private_url

Delete a specific dataset's private URL

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_private_url(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeletePrivateURLResponse](../../models/operations/deleteprivateurlresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## replace_dataset_files

Replace files in a specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.replace_dataset_files(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                             | *str*                                                                                                            | :heavy_check_mark:                                                                                               | N/A                                                                                                              |
| `request_body`                                                                                                   | [Optional[operations.ReplaceDatasetFilesRequestBody]](../../models/operations/replacedatasetfilesrequestbody.md) | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |

### Response

**[operations.ReplaceDatasetFilesResponse](../../models/operations/replacedatasetfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## submit_globus_download_request

Submit a request for Globus download for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.submit_globus_download_request(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `download_id`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.SubmitGlobusDownloadRequestResponse](../../models/operations/submitglobusdownloadrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_globus_upload_paths_request

Submit a request to get the paths for Globus file upload for a specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.post_globus_upload_paths_request(id='<id>')

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

**[operations.PostGlobusUploadPathsRequestResponse](../../models/operations/postglobusuploadpathsrequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## return_dataset_to_author

Returns the specified dataset back to its author

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.return_dataset_to_author(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.ReturnDatasetToAuthorResponse](../../models/operations/returndatasettoauthorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## submit_dataset_for_review

Submits a specified dataset for review

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.submit_dataset_for_review(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.SubmitDatasetForReviewResponse](../../models/operations/submitdatasetforreviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_thumbnail

Retrieves a thumbnail from a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_thumbnail(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetThumbnailResponse](../../models/operations/getdatasetthumbnailresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_dataset_thumbnail

Adds a thumbnail to a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.post_dataset_thumbnail(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                               | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | N/A                                                                                                                |
| `request_body`                                                                                                     | [Optional[operations.PostDatasetThumbnailRequestBody]](../../models/operations/postdatasetthumbnailrequestbody.md) | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |

### Response

**[operations.PostDatasetThumbnailResponse](../../models/operations/postdatasetthumbnailresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset_thumbnail

Deletes a thumbnail from a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset_thumbnail(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteDatasetThumbnailResponse](../../models/operations/deletedatasetthumbnailresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_thumbnail_candidates

Retrieve the list of thumbnail candidates for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_thumbnail_candidates(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetThumbnailCandidatesResponse](../../models/operations/getthumbnailcandidatesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_thumbnail_data

Upload a new thumbnail for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.post_thumbnail_data(data_file_id=907375, id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_file_id`     | *int*              | :heavy_check_mark: | N/A                |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.PostThumbnailDataResponse](../../models/operations/postthumbnaildataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## ~~get_upload_id~~

Retrieve the upload ID for the specified dataset

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_upload_id(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetUploadIDResponse](../../models/operations/getuploadidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_upload_ur_ls

Retrieve upload URLs for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_upload_ur_ls(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `size`             | *Optional[int]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetUploadURLsResponse](../../models/operations/getuploadurlsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_user_permissions

Retrieve user permissions for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_user_permissions(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetUserPermissionsResponse](../../models/operations/getuserpermissionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_versions

Retrieve versions of a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_versions(id='<id>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `exclude_files`    | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `offset`           | *Optional[int]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetVersionsResponse](../../models/operations/getdatasetversionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_version

Fetches the dataset version details, with options to exclude files or include deaccessioned ones

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_version(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter               | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `id`                    | *str*                   | :heavy_check_mark:      | N/A                     |
| `version_id`            | *str*                   | :heavy_check_mark:      | N/A                     |
| `exclude_files`         | *Optional[bool]*        | :heavy_minus_sign:      | N/A                     |
| `include_deaccessioned` | *Optional[bool]*        | :heavy_minus_sign:      | N/A                     |

### Response

**[operations.GetDatasetVersionResponse](../../models/operations/getdatasetversionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dataset_version

Updates the dataset version with the given ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_dataset_version(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_id`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.UpdateDatasetVersionResponse](../../models/operations/updatedatasetversionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset_version

Deletes the specified version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset_version(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_id`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteDatasetVersionResponse](../../models/operations/deletedatasetversionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## check_dataset_file_download_permission

Checks if a user has permission to download at least one file from a specific dataset version

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.check_dataset_file_download_permission(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter               | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `id`                    | *str*                   | :heavy_check_mark:      | N/A                     |
| `version_id`            | *str*                   | :heavy_check_mark:      | N/A                     |
| `include_deaccessioned` | *Optional[bool]*        | :heavy_minus_sign:      | N/A                     |

### Response

**[operations.CheckDatasetFileDownloadPermissionResponse](../../models/operations/checkdatasetfiledownloadpermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_citation

Retrieve the citation of a specific dataset version

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_citation(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter               | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `id`                    | *str*                   | :heavy_check_mark:      | N/A                     |
| `version_id`            | *str*                   | :heavy_check_mark:      | N/A                     |
| `include_deaccessioned` | *Optional[bool]*        | :heavy_minus_sign:      | N/A                     |

### Response

**[operations.GetCitationResponse](../../models/operations/getcitationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_custom_license

Retrieve a specific dataset version's custom license

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_custom_license(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_id`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetCustomLicenseResponse](../../models/operations/getcustomlicenseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_deaccession_dataset_by_version_id

Remove access to a specific version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.post_deaccession_dataset_by_version_id(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_id`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.PostDeaccessionDatasetByVersionIDResponse](../../models/operations/postdeaccessiondatasetbyversionidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_version_files

Fetches files within a specific version of a dataset

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_version_files(request=operations.GetDatasetVersionFilesRequest(
    id='<id>',
    version_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetDatasetVersionFilesRequest](../../models/operations/getdatasetversionfilesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |

### Response

**[operations.GetDatasetVersionFilesResponse](../../models/operations/getdatasetversionfilesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_files_count

Retrieve counts of various types of files in a specified dataset version

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_files_count(request=operations.GetDatasetFilesCountRequest(
    id='<id>',
    version_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetDatasetFilesCountRequest](../../models/operations/getdatasetfilescountrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |

### Response

**[operations.GetDatasetFilesCountResponse](../../models/operations/getdatasetfilescountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_version_linkset

Retrieve linkset of a specific dataset version

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_version_linkset(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_id`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetVersionLinksetResponse](../../models/operations/getdatasetversionlinksetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_version_metadata

Retrieve the metadata of a specific version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_version_metadata(id='<id>', version_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_id`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetVersionMetadataResponse](../../models/operations/getdatasetversionmetadataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_version_metadata_1

Retrieve metadata of a specified version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_version_metadata_1(block='<value>', id='<id>', version_number='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `block`            | *str*              | :heavy_check_mark: | N/A                |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version_number`   | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetVersionMetadata1Response](../../models/operations/getdatasetversionmetadata1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_version_tool_param

Retrieve tool parameters of a specific version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_version_tool_param(id='<id>', tid=660939, version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `tid`              | *int*              | :heavy_check_mark: | N/A                |
| `version`          | *str*              | :heavy_check_mark: | N/A                |
| `locale`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetDatasetVersionToolParamResponse](../../models/operations/getdatasetversiontoolparamresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_archival_status

Retrieve the archival status of a specific version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.get_dataset_archival_status(id='<id>', version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version`          | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetArchivalStatusResponse](../../models/operations/getdatasetarchivalstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dataset_archival_status

Update the archival status of a specific version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_dataset_archival_status(id='<id>', version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version`          | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.UpdateDatasetArchivalStatusResponse](../../models/operations/updatedatasetarchivalstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataset_archival_status

Remove the archival status of a specific version of a dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.delete_dataset_archival_status(id='<id>', version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `version`          | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteDatasetArchivalStatusResponse](../../models/operations/deletedatasetarchivalstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dataset_link

Updates the link between a dataset and a Dataverse alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.datasets.update_dataset_link(linked_dataset_id='<value>', linking_dataverse_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `linked_dataset_id`       | *str*                     | :heavy_check_mark:        | N/A                       |
| `linking_dataverse_alias` | *str*                     | :heavy_check_mark:        | N/A                       |

### Response

**[operations.UpdateDatasetLinkResponse](../../models/operations/updatedatasetlinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |