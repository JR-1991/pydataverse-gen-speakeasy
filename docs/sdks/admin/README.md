# Admin
(*admin*)

### Available Operations

* [archive_all_unarchived_versions](#archive_all_unarchived_versions) - Archives all unarchived dataset versions. Allows options to limit the number of versions archived, archive only the latest versions, or simply list the versions that would be archived without actually doing it.
* [get_admin_assignee](#get_admin_assignee) - Retrieve a specific assignee detail by ID.
* [get_assignees_detail](#get_assignees_detail) - Retrieve details of a specific assignee by raIdtf
* [~~get_authenticated_users~~](#get_authenticated_users) - Retrieves a list of authenticated users. This endpoint is deprecated. :warning: **Deprecated**
* [create_authenticated_user](#create_authenticated_user) - Creates a new authenticated user.
* [convert_user_to_o_auth](#convert_user_to_o_auth) - Convert an authenticated user from built-in to OAuth
* [convert_auth_users](#convert_auth_users) - Convert Authenticated Users from Built-in system to Shibboleth
* [delete_authenticated_user](#delete_authenticated_user) - Delete an authenticated user by ID
* [convert_remote_to_built_in](#convert_remote_to_built_in) - Converts a remote user to a built-in user by their ID
* [~~convert_user_authentication_method~~](#convert_user_authentication_method) - Converts the authentication method of an authenticated user from Shibboleth to Built-In. :warning: **Deprecated**
* [deactivate_user](#deactivate_user) - Deactivates an authenticated user by ID
* [get_authenticated_user](#get_authenticated_user) - Retrieve details of a specified authenticated user
* [delete_authenticated_user_1](#delete_authenticated_user_1) - Delete a specified authenticated user
* [deactivate_user_1](#deactivate_user_1) - Deactivate an authenticated user by identifier
* [get_auth_provider_factories](#get_auth_provider_factories) - Retrieve all authentication provider factories
* [get_auth_providers](#get_auth_providers) - Retrieve list of authentication providers
* [add_auth_provider](#add_auth_provider) - Add a new authentication provider
* [get_auth_providers_by_id](#get_auth_providers_by_id) - Fetch specific authentication provider using ID
* [remove_auth_providers_by_id](#remove_auth_providers_by_id) - Delete specific authentication provider using ID
* [enable_auth_provider](#enable_auth_provider) - Enable a specific authentication provider by its ID
* [get_auth_provider_status](#get_auth_provider_status) - Retrieves the status of a specific authentication provider
* [update_auth_provider_status](#update_auth_provider_status) - Updates the status of a specific authentication provider
* [get_banner_message](#get_banner_message) - Retrieve a current banner message
* [post_banner_message](#post_banner_message) - Add a new banner message
* [delete_banner_message](#delete_banner_message) - Delete a specific banner message by ID
* [deactivate_banner_message](#deactivate_banner_message) - Deactivates a specific banner message
* [get_batch_jobs](#get_batch_jobs) - Retrieve all batch jobs
* [get_job_by_name](#get_job_by_name) - Retrieve details for a job given its name
* [get_admin_job_by_id](#get_admin_job_by_id) - Retrieve details of a specific admin batch job
* [delete_metrics_cache](#delete_metrics_cache) - Deletes the metrics cache for admin
* [delete_metrics_cache_1](#delete_metrics_cache_1) - Deletes a specific metric cache.
* [delete_thumbnail_failure_flag](#delete_thumbnail_failure_flag) - Deletes a thumbnail failure flag
* [admin_clear_thumbnail_failure_flag](#admin_clear_thumbnail_failure_flag) - Delete the thumbnail failure flag for a specified Dataverse id
* [compute_file_hash_value](#compute_file_hash_value) - Computes the hash value of the specified file using the given algorithm
* [get_user_id_conf_email](#get_user_id_conf_email) - Retrieve Confirmation Email Associated with User ID
* [post_user_id_conf_email](#post_user_id_conf_email) - Send Confirmation Email to User ID
* [admin_convert_user_encryption](#admin_convert_user_encryption) - Convert a user's encryption scheme from Bcrypt to Sha1
* [get_fix_missing_original_sizes](#get_fix_missing_original_sizes) - Retrieve a limited number of records with missing original sizes and fix them
* [fix_missing_original_types](#fix_missing_original_types) - Retrieve a report of datafiles with missing original types and apply fixes
* [get_admin_dataset_field](#get_admin_dataset_field) - Retrieve the dataset fields available to administrators
* [get_controlled_vocabulary](#get_controlled_vocabulary) - Retrieve a list of controlled vocabulary subjects
* [load_dataset_field_admin](#load_dataset_field_admin) - Load dataset field as an admin
* [get_na_controlled_vocab_value](#get_na_controlled_vocab_value) - Retrieve North American controlled vocabulary value
* [admin_load_property_files](#admin_load_property_files) - Load dataset field property files as a ZIP.
* [get_dataset_field_name](#get_dataset_field_name) - Retrieve information of the specified dataset field
* [post_fix_missing_unf](#post_fix_missing_unf) - Update or recalculate dataset integrity by fixing missing UNF in specified dataset version
* [get_thumbnail_metadata_by_id](#get_thumbnail_metadata_by_id) - Retrieves thumbnail metadata for a specific dataset using its ID
* [get_curation_label_sets](#get_curation_label_sets) - Retrieve all curation label sets
* [get_storage_drivers](#get_storage_drivers) - Retrieves all storage drivers
* [get_role_assignments](#get_role_assignments) - Retrieve role assignments associated with a dataverse
* [get_curation_label_set](#get_curation_label_set) - Retrieve the curation label set of the specified Dataverse
* [update_curation_label_set](#update_curation_label_set) - Update or create a curation label set for the specified Dataverse
* [delete_curation_label_set](#delete_curation_label_set) - Remove the curation label set from the specified Dataverse
* [get_storage_driver](#get_storage_driver) - Retrieve the storage driver of a specific dataverse
* [update_storage_driver](#update_storage_driver) - Update the storage driver of a specific dataverse
* [delete_storage_driver](#delete_storage_driver) - Remove the storage driver of a specific dataverse
* [get_tmp_file](#get_tmp_file) - Retrieve a temporary file via its fully qualified path
* [get_external_tools](#get_external_tools) - Retrieve a list of all external tools
* [create_external_tool](#create_external_tool) - Create a new external tool
* [get_external_tool](#get_external_tool) - Retrieve an external tool by its ID
* [delete_external_tool](#delete_external_tool) - Delete an external tool by its ID
* [post_admin_feedback](#post_admin_feedback) - Create or post feedback as an admin
* [get_admin_groups_domain](#get_admin_groups_domain) - Retrieve domain-related groups information from the admin endpoint
* [post_admin_groups_domain](#post_admin_groups_domain) - Submit new domain-related groups information to the admin endpoint
* [get_group_alias](#get_group_alias) - Retrieves information of the group alias specified in the path
* [update_group_alias](#update_group_alias) - Updates the group alias specified in the path
* [delete_group_alias](#delete_group_alias) - Deletes the group alias specified in the path
* [get_admin_groups_ip](#get_admin_groups_ip) - Retrieve IP-based groups information
* [post_admin_groups_ip](#post_admin_groups_ip) - Create a new IP-based group
* [get_group_by_group_idtf](#get_group_by_group_idtf) - Fetches a group by the groupIdtf provided in the path
* [delete_group_by_group_idtf](#delete_group_by_group_idtf) - Deletes a group by the groupIdtf provided in the path
* [get_shib_group_info](#get_shib_group_info) - Retrieve information about Shibboleth groups
* [create_shib_group](#create_shib_group) - Create a new Shibboleth group
* [delete_shib_group](#delete_shib_group) - Delete a Shibboleth Group by given Primary Key
* [get_admin_index](#get_admin_index) - Retrieve details of admin index with queried parameters
* [clear_admin_index](#clear_admin_index) - Clears the admin index
* [clear_orphans_index](#clear_orphans_index) - Retrieve and clear orphans from the admin index
* [continue_index_processing](#continue_index_processing) - Continues the process of indexing partitions based on given parameters.
* [get_dataset_index](#get_dataset_index) - Retrieve the index of a dataset given its persistentId
* [delete_dataset_by_id](#delete_dataset_by_id) - Delete a specific dataset by its ID
* [get_file_metadata1](#get_file_metadata1) - Retrieve file metadata for a specific dataset
* [file_search_index_get](#file_search_index_get) - This endpoint retrieves data about file search index by persistentId, q, and/or semanticVersion.
* [get_admin_index_mod](#get_admin_index_mod) - Retrieves modification of the admin index based on provided query parameters
* [get_admin_index_perms](#get_admin_index_perms) - Retrieve permissions for the admin index
* [get_admin_index_perms_1](#get_admin_index_perms_1) - Retrieve a specific admin index permissions by ID
* [get_perms_debug_info](#get_perms_debug_info) - Retrieves permission debug info for specified id and key
* [get_solr_schema](#get_solr_schema) - Retrieve the Solr schema configuration.
* [get_admin_index_status](#get_admin_index_status) - Retrieve status of the admin index
* [get_admin_test_index](#get_admin_test_index) - Obtain specific parameters from the Admin Test Index
* [delete_admin_index_timestamps](#delete_admin_index_timestamps) - Delete timestamps from the admin index
* [delete_index_timestamp](#delete_index_timestamp) - Delete index timestamp by dvObjectId
* [get_admin_index_type_by_id](#get_admin_index_type_by_id) - Retrieves specific type and ID details in admin index
* [get_orcid_status](#get_orcid_status) - Retrieve ORCID status for a specific admin
* [list_users](#list_users) - Retrieve a list of all users
* [add_metrics_from_report](#add_metrics_from_report) - Add usage metrics from a SUSHI report
* [admin_send_to_hub](#admin_send_to_hub) - Send data count to the admin hub.
* [add_usage_metrics_from_sushi_repo](#add_usage_metrics_from_sushi_repo) - Add usage metrics for a specific Dataverse file from a SUSHI Report
* [update_dataset_citations](#update_dataset_citations) - Updates the citation count for a specified dataset
* [get_export_timestamps](#get_export_timestamps) - Retrieve the export timestamps
* [get_metadata_export_all](#get_metadata_export_all) - Fetches all metadata for export by admin
* [admin_metadata_export_oai_spec](#admin_metadata_export_oai_spec) - Update the OAI export specification using provided 'specname'
* [re_export_all_metadata](#re_export_all_metadata) - Retrieves and exports all metadata
* [get_metadata_re_export](#get_metadata_re_export) - Retrieves and re-exports the specific metadata for the dataset using dataset ID
* [get_admin_permissions](#get_admin_permissions) - Retrieve specific admin permission details
* [publish_dataverse_as_creator](#publish_dataverse_as_creator) - Publish Dataverse as creator using the given ID
* [get_register_data_file_all](#get_register_data_file_all) - Retrieve all registered data files from the admin.
* [get_register_data_files_by_alias](#get_register_data_files_by_alias) - Retrieve data file registration details for a given alias
* [post_admin_signed_url](#post_admin_signed_url) - Admin sends a request to receive a signed URL.
* [get_admin_roles](#get_admin_roles) - Retrieve a list of all admin roles
* [create_admin_role](#create_admin_role) - Create a new admin role
* [delete_admin_role](#delete_admin_role) - Delete a specific admin role
* [get_saved_searches](#get_saved_searches) - Retrieves all saved searches in the system.
* [add_saved_search](#add_saved_search) - Adds a new saved search to the system.
* [get_saved_searches_list](#get_saved_searches_list) - Retrieve a list of all saved searches by the administrator
* [update_all_saved_search_links](#update_all_saved_search_links) - Updates all saved search links
* [make_links_for_saved_search](#make_links_for_saved_search) - Updates the link for a specific saved search by ID
* [get_saved_search](#get_saved_search) - Retrieves a saved search by ID
* [delete_saved_search](#delete_saved_search) - Deletes a saved search by ID
* [get_admin_settings](#get_admin_settings) - Retrieve administrator settings
* [get_admin_setting](#get_admin_setting) - Retrieve a specified admin setting
* [update_admin_setting](#update_admin_setting) - Update a specified admin setting
* [delete_admin_setting](#delete_admin_setting) - Delete a specified admin setting
* [update_admin_settings_lang](#update_admin_settings_lang) - Update a specific Admin setting for a given language
* [delete_admin_settings_lang](#delete_admin_settings_lang) - Delete a specific Admin setting for a given language
* [generate_sitemap](#generate_sitemap) - Generate a new sitemap for the application
* [get_storage_sites](#get_storage_sites) - Fetches all storage sites
* [create_storage_site](#create_storage_site) - Creates a new storage site
* [fetch_storage_site](#fetch_storage_site) - Retrieves details of a specific storage site by its unique identifier
* [delete_storage_site](#delete_storage_site) - Deletes a specific storage site by its unique identifier
* [update_primary_storage](#update_primary_storage) - Update the primary storage of a storage site by ID
* [submit_dataset_version_to_archive](#submit_dataset_version_to_archive) - Submit a specific dataset version to the archive by using provided dataset ID and version number
* [admin_create_super_user](#admin_create_super_user) - Creates a new superuser with the provided identifier
* [delete_admin_template](#delete_admin_template) - Delete an admin template by ID
* [get_admin_templates](#get_admin_templates) - Retrieve all admin templates
* [get_admin_template](#get_admin_template) - Retrieve a specific admin template using its alias.
* [get_external_tools_1](#get_external_tools_1) - Gets an external tool associated with a specific dataset identified by its id
* [get_external_tool_by_id](#get_external_tool_by_id) - Retrieve the details of a specific external tool by its ID for a given file
* [get_external_tools_1_1](#get_external_tools_1_1) - Retrieve the external tools of a specific test file.
* [get_hash_values](#get_hash_values) - Retrieve hash values based on specified algorithm
* [get_validate_dataset_files](#get_validate_dataset_files) - Retrieve and validate specified dataset files
* [validate_dataset](#validate_dataset) - Validate a dataset with a specified ID
* [admin_validate_datasets](#admin_validate_datasets) - Validate datasets in the system
* [validate_data_file_hash](#validate_data_file_hash) - Validate hash value of the specified data file
* [validate_admin_password](#validate_admin_password) - Validates the password of an admin user
* [get_admin_workflows](#get_admin_workflows) - Retrieve all workflows associated with the admin
* [create_admin_workflow](#create_admin_workflow) - Create a new workflow for the admin
* [get_default_workflow](#get_default_workflow) - Fetch default workflow configured for admin
* [get_trigger_type](#get_trigger_type) - Retrieve a specific trigger type from workflows
* [update_trigger_type](#update_trigger_type) - Update a specific trigger type in workflows
* [delete_trigger_type](#delete_trigger_type) - Delete a specific trigger type from workflows
* [get_ip_whitelist](#get_ip_whitelist) - Retrieve current IP Whitelist for admin workflows
* [update_ip_whitelist](#update_ip_whitelist) - Update the IP Whitelist for admin workflows
* [delete_ip_whitelist](#delete_ip_whitelist) - Remove the IP Whitelist for admin workflows
* [get_workflow_by_identifier](#get_workflow_by_identifier) - Retrieve a specific workflow using its identifier
* [get_admin_data_file](#get_admin_data_file) - Retrieve data file details registered by a specific admin
* [admin_reregister_hdl_to_pid](#admin_reregister_hdl_to_pid) - Admin reruns the HDL to PID registration for a specific admin ID.

## archive_all_unarchived_versions

Archives all unarchived dataset versions. Allows options to limit the number of versions archived, archive only the latest versions, or simply list the versions that would be archived without actually doing it.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.archive_all_unarchived_versions(latestonly=False, limit=452296, listonly=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `latestonly`       | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `listonly`         | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.ArchiveAllUnarchivedVersionsResponse](../../models/operations/archiveallunarchivedversionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_assignee

Retrieve a specific assignee detail by ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_assignee(idtf='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `idtf`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminAssigneeResponse](../../models/operations/getadminassigneeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_assignees_detail

Retrieve details of a specific assignee by raIdtf

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_assignees_detail(ra_idtf='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `ra_idtf`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAssigneesDetailResponse](../../models/operations/getassigneesdetailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~get_authenticated_users~~

Retrieves a list of authenticated users. This endpoint is deprecated.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_authenticated_users()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAuthenticatedUsersResponse](../../models/operations/getauthenticatedusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_authenticated_user

Creates a new authenticated user.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.create_authenticated_user()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.CreateAuthenticatedUserResponse](../../models/operations/createauthenticateduserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## convert_user_to_o_auth

Convert an authenticated user from built-in to OAuth

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.convert_user_to_o_auth()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.ConvertUserToOAuthResponse](../../models/operations/convertusertooauthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## convert_auth_users

Convert Authenticated Users from Built-in system to Shibboleth

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.convert_auth_users()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.ConvertAuthUsersResponse](../../models/operations/convertauthusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_authenticated_user

Delete an authenticated user by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_authenticated_user(id=972068)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAuthenticatedUserResponse](../../models/operations/deleteauthenticateduserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## convert_remote_to_built_in

Converts a remote user to a built-in user by their ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.convert_remote_to_built_in(id=306142)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ConvertRemoteToBuiltInResponse](../../models/operations/convertremotetobuiltinresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## ~~convert_user_authentication_method~~

Converts the authentication method of an authenticated user from Shibboleth to Built-In.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.convert_user_authentication_method(id=261670)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ConvertUserAuthenticationMethodResponse](../../models/operations/convertuserauthenticationmethodresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## deactivate_user

Deactivates an authenticated user by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.deactivate_user(id=143950)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeactivateUserResponse](../../models/operations/deactivateuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_authenticated_user

Retrieve details of a specified authenticated user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_authenticated_user(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAuthenticatedUserResponse](../../models/operations/getauthenticateduserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_authenticated_user_1

Delete a specified authenticated user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_authenticated_user_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAuthenticatedUser1Response](../../models/operations/deleteauthenticateduser1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## deactivate_user_1

Deactivate an authenticated user by identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.deactivate_user_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeactivateUser1Response](../../models/operations/deactivateuser1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_auth_provider_factories

Retrieve all authentication provider factories

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_auth_provider_factories()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAuthProviderFactoriesResponse](../../models/operations/getauthproviderfactoriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_auth_providers

Retrieve list of authentication providers

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_auth_providers()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAuthProvidersResponse](../../models/operations/getauthprovidersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_auth_provider

Add a new authentication provider

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.add_auth_provider()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.AddAuthProviderResponse](../../models/operations/addauthproviderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_auth_providers_by_id

Fetch specific authentication provider using ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_auth_providers_by_id(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAuthProvidersByIDResponse](../../models/operations/getauthprovidersbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## remove_auth_providers_by_id

Delete specific authentication provider using ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.remove_auth_providers_by_id(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RemoveAuthProvidersByIDResponse](../../models/operations/removeauthprovidersbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## enable_auth_provider

Enable a specific authentication provider by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.enable_auth_provider(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.EnableAuthProviderResponse](../../models/operations/enableauthproviderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_auth_provider_status

Retrieves the status of a specific authentication provider

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_auth_provider_status(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAuthProviderStatusResponse](../../models/operations/getauthproviderstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_auth_provider_status

Updates the status of a specific authentication provider

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_auth_provider_status(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateAuthProviderStatusResponse](../../models/operations/updateauthproviderstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_banner_message

Retrieve a current banner message

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_banner_message()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetBannerMessageResponse](../../models/operations/getbannermessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_banner_message

Add a new banner message

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_banner_message()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.PostBannerMessageResponse](../../models/operations/postbannermessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_banner_message

Delete a specific banner message by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_banner_message(id=314460)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteBannerMessageResponse](../../models/operations/deletebannermessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## deactivate_banner_message

Deactivates a specific banner message

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.deactivate_banner_message(id=723548)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeactivateBannerMessageResponse](../../models/operations/deactivatebannermessageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_batch_jobs

Retrieve all batch jobs

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_batch_jobs()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetBatchJobsResponse](../../models/operations/getbatchjobsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_job_by_name

Retrieve details for a job given its name

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_job_by_name(job_name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `job_name`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetJobByNameResponse](../../models/operations/getjobbynameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_job_by_id

Retrieve details of a specific admin batch job

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_job_by_id(job_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `job_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminJobByIDResponse](../../models/operations/getadminjobbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_metrics_cache

Deletes the metrics cache for admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_metrics_cache()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.DeleteMetricsCacheResponse](../../models/operations/deletemetricscacheresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_metrics_cache_1

Deletes a specific metric cache.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_metrics_cache_1(name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteMetricsCache1Response](../../models/operations/deletemetricscache1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_thumbnail_failure_flag

Deletes a thumbnail failure flag

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_thumbnail_failure_flag()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.DeleteThumbnailFailureFlagResponse](../../models/operations/deletethumbnailfailureflagresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_clear_thumbnail_failure_flag

Delete the thumbnail failure flag for a specified Dataverse id

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_clear_thumbnail_failure_flag(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.AdminClearThumbnailFailureFlagResponse](../../models/operations/adminclearthumbnailfailureflagresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## compute_file_hash_value

Computes the hash value of the specified file using the given algorithm

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.compute_file_hash_value(alg='<value>', file_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alg`              | *str*              | :heavy_check_mark: | N/A                |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ComputeFileHashValueResponse](../../models/operations/computefilehashvalueresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_user_id_conf_email

Retrieve Confirmation Email Associated with User ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_user_id_conf_email(user_id=47374)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetUserIDConfEmailResponse](../../models/operations/getuseridconfemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_user_id_conf_email

Send Confirmation Email to User ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_user_id_conf_email(user_id=163013)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostUserIDConfEmailResponse](../../models/operations/postuseridconfemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_convert_user_encryption

Convert a user's encryption scheme from Bcrypt to Sha1

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_convert_user_encryption()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.AdminConvertUserEncryptionResponse](../../models/operations/adminconvertuserencryptionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_fix_missing_original_sizes

Retrieve a limited number of records with missing original sizes and fix them

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_fix_missing_original_sizes(limit=413519)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFixMissingOriginalSizesResponse](../../models/operations/getfixmissingoriginalsizesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## fix_missing_original_types

Retrieve a report of datafiles with missing original types and apply fixes

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.fix_missing_original_types()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.FixMissingOriginalTypesResponse](../../models/operations/fixmissingoriginaltypesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_dataset_field

Retrieve the dataset fields available to administrators

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_dataset_field()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminDatasetFieldResponse](../../models/operations/getadmindatasetfieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_controlled_vocabulary

Retrieve a list of controlled vocabulary subjects

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_controlled_vocabulary()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetControlledVocabularyResponse](../../models/operations/getcontrolledvocabularyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## load_dataset_field_admin

Load dataset field as an admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.load_dataset_field_admin(request='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.LoadDatasetFieldAdminResponse](../../models/operations/loaddatasetfieldadminresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_na_controlled_vocab_value

Retrieve North American controlled vocabulary value

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_na_controlled_vocab_value()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetNAControlledVocabValueResponse](../../models/operations/getnacontrolledvocabvalueresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_load_property_files

Load dataset field property files as a ZIP.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_load_property_files(request='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AdminLoadPropertyFilesResponse](../../models/operations/adminloadpropertyfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_dataset_field_name

Retrieve information of the specified dataset field

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_dataset_field_name(name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDatasetFieldNameResponse](../../models/operations/getdatasetfieldnameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_fix_missing_unf

Update or recalculate dataset integrity by fixing missing UNF in specified dataset version

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_fix_missing_unf(dataset_version_id='<value>', force_recalculate=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter            | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `dataset_version_id` | *str*                | :heavy_check_mark:   | N/A                  |
| `force_recalculate`  | *Optional[bool]*     | :heavy_minus_sign:   | N/A                  |


### Response

**[operations.PostFixMissingUnfResponse](../../models/operations/postfixmissingunfresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_thumbnail_metadata_by_id

Retrieves thumbnail metadata for a specific dataset using its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_thumbnail_metadata_by_id(id=860637)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetThumbnailMetadataByIDResponse](../../models/operations/getthumbnailmetadatabyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_curation_label_sets

Retrieve all curation label sets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_curation_label_sets()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetCurationLabelSetsResponse](../../models/operations/getcurationlabelsetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_storage_drivers

Retrieves all storage drivers

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_storage_drivers()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetStorageDriversResponse](../../models/operations/getstoragedriversresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_role_assignments

Retrieve role assignments associated with a dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_role_assignments(alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetRoleAssignmentsResponse](../../models/operations/getroleassignmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_curation_label_set

Retrieve the curation label set of the specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_curation_label_set(alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetCurationLabelSetResponse](../../models/operations/getcurationlabelsetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_curation_label_set

Update or create a curation label set for the specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_curation_label_set(alias='<value>', name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |
| `name`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.UpdateCurationLabelSetResponse](../../models/operations/updatecurationlabelsetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_curation_label_set

Remove the curation label set from the specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_curation_label_set(alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteCurationLabelSetResponse](../../models/operations/deletecurationlabelsetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_storage_driver

Retrieve the storage driver of a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_storage_driver(alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetStorageDriverResponse](../../models/operations/getstoragedriverresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_storage_driver

Update the storage driver of a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_storage_driver(alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateStorageDriverResponse](../../models/operations/updatestoragedriverresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_storage_driver

Remove the storage driver of a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_storage_driver(alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteStorageDriverResponse](../../models/operations/deletestoragedriverresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_tmp_file

Retrieve a temporary file via its fully qualified path

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_tmp_file(fully_qualified_path_to_file='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `fully_qualified_path_to_file` | *Optional[str]*                | :heavy_minus_sign:             | N/A                            |


### Response

**[operations.GetTmpFileResponse](../../models/operations/gettmpfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_external_tools

Retrieve a list of all external tools

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_external_tools()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetExternalToolsResponse](../../models/operations/getexternaltoolsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_external_tool

Create a new external tool

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.create_external_tool()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.CreateExternalToolResponse](../../models/operations/createexternaltoolresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_external_tool

Retrieve an external tool by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_external_tool(id=835857)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetExternalToolResponse](../../models/operations/getexternaltoolresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_external_tool

Delete an external tool by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_external_tool(id=423055)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteExternalToolResponse](../../models/operations/deleteexternaltoolresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_admin_feedback

Create or post feedback as an admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_admin_feedback()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.PostAdminFeedbackResponse](../../models/operations/postadminfeedbackresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_groups_domain

Retrieve domain-related groups information from the admin endpoint

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_groups_domain()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminGroupsDomainResponse](../../models/operations/getadmingroupsdomainresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_admin_groups_domain

Submit new domain-related groups information to the admin endpoint

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_admin_groups_domain()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.PostAdminGroupsDomainResponse](../../models/operations/postadmingroupsdomainresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_group_alias

Retrieves information of the group alias specified in the path

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_group_alias(group_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_alias`      | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetGroupAliasResponse](../../models/operations/getgroupaliasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_group_alias

Updates the group alias specified in the path

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_group_alias(group_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_alias`      | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateGroupAliasResponse](../../models/operations/updategroupaliasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_group_alias

Deletes the group alias specified in the path

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_group_alias(group_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_alias`      | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteGroupAliasResponse](../../models/operations/deletegroupaliasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_groups_ip

Retrieve IP-based groups information

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_groups_ip()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminGroupsIPResponse](../../models/operations/getadmingroupsipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_admin_groups_ip

Create a new IP-based group

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_admin_groups_ip()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.PostAdminGroupsIPResponse](../../models/operations/postadmingroupsipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_group_by_group_idtf

Fetches a group by the groupIdtf provided in the path

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_group_by_group_idtf(group_idtf='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_idtf`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetGroupByGroupIdtfResponse](../../models/operations/getgroupbygroupidtfresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_group_by_group_idtf

Deletes a group by the groupIdtf provided in the path

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_group_by_group_idtf(group_idtf='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_idtf`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteGroupByGroupIdtfResponse](../../models/operations/deletegroupbygroupidtfresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_shib_group_info

Retrieve information about Shibboleth groups

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_shib_group_info()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetShibGroupInfoResponse](../../models/operations/getshibgroupinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_shib_group

Create a new Shibboleth group

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.create_shib_group()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.CreateShibGroupResponse](../../models/operations/createshibgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_shib_group

Delete a Shibboleth Group by given Primary Key

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_shib_group(primary_key='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `primary_key`      | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteShibGroupResponse](../../models/operations/deleteshibgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_index

Retrieve details of admin index with queried parameters

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_index(num_partitions=966288, partition_id_to_process=875880, preview_only=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `num_partitions`          | *Optional[int]*           | :heavy_minus_sign:        | N/A                       |
| `partition_id_to_process` | *Optional[int]*           | :heavy_minus_sign:        | N/A                       |
| `preview_only`            | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |


### Response

**[operations.GetAdminIndexResponse](../../models/operations/getadminindexresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## clear_admin_index

Clears the admin index

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.clear_admin_index()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.ClearAdminIndexResponse](../../models/operations/clearadminindexresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## clear_orphans_index

Retrieve and clear orphans from the admin index

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.clear_orphans_index(sync='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `sync`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.ClearOrphansIndexResponse](../../models/operations/clearorphansindexresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## continue_index_processing

Continues the process of indexing partitions based on given parameters.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.continue_index_processing(num_partitions=385791, partition_id_to_process=791191, preview_only=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `num_partitions`          | *Optional[int]*           | :heavy_minus_sign:        | N/A                       |
| `partition_id_to_process` | *Optional[int]*           | :heavy_minus_sign:        | N/A                       |
| `preview_only`            | *Optional[bool]*          | :heavy_minus_sign:        | N/A                       |


### Response

**[operations.ContinueIndexProcessingResponse](../../models/operations/continueindexprocessingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_dataset_index

Retrieve the index of a dataset given its persistentId

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_dataset_index(persistent_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `persistent_id`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDatasetIndexResponse](../../models/operations/getdatasetindexresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_dataset_by_id

Delete a specific dataset by its ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_dataset_by_id(id=57539)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteDatasetByIDResponse](../../models/operations/deletedatasetbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_file_metadata1

Retrieve file metadata for a specific dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_file_metadata1(dataset_id=442844, max_results=115835, order='<value>', sort='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dataset_id`       | *int*              | :heavy_check_mark: | N/A                |
| `max_results`      | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `order`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `sort`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFileMetadata1Response](../../models/operations/getfilemetadata1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## file_search_index_get

This endpoint retrieves data about file search index by persistentId, q, and/or semanticVersion.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.file_search_index_get(persistent_id='<value>', q='<value>', semantic_version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `persistent_id`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `q`                | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `semantic_version` | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.FileSearchIndexGETResponse](../../models/operations/filesearchindexgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_index_mod

Retrieves modification of the admin index based on provided query parameters

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_index_mod(partitions=500680, which=91223)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `partitions`       | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `which`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAdminIndexModResponse](../../models/operations/getadminindexmodresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_index_perms

Retrieve permissions for the admin index

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_index_perms()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminIndexPermsResponse](../../models/operations/getadminindexpermsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_index_perms_1

Retrieve a specific admin index permissions by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_index_perms_1(id=536096)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminIndexPerms1Response](../../models/operations/getadminindexperms1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_perms_debug_info

Retrieves permission debug info for specified id and key

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_perms_debug_info(id=680308, key='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetPermsDebugInfoResponse](../../models/operations/getpermsdebuginforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_solr_schema

Retrieve the Solr schema configuration.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_solr_schema()

if res.res is not None:
    # handle response
    pass

```


### Response

**[operations.GetSolrSchemaResponse](../../models/operations/getsolrschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_index_status

Retrieve status of the admin index

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_index_status(sync='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `sync`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAdminIndexStatusResponse](../../models/operations/getadminindexstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_test_index

Obtain specific parameters from the Admin Test Index

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_test_index(fq=[
    '<value>',
], key='<value>', q='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `fq`               | List[*str*]        | :heavy_minus_sign: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `q`                | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAdminTestIndexResponse](../../models/operations/getadmintestindexresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_admin_index_timestamps

Delete timestamps from the admin index

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_admin_index_timestamps()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.DeleteAdminIndexTimestampsResponse](../../models/operations/deleteadminindextimestampsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_index_timestamp

Delete index timestamp by dvObjectId

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_index_timestamp(dv_object_id=378575)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dv_object_id`     | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteIndexTimestampResponse](../../models/operations/deleteindextimestampresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_index_type_by_id

Retrieves specific type and ID details in admin index

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_index_type_by_id(id=292538, type='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |
| `type`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminIndexTypeByIDResponse](../../models/operations/getadminindextypebyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_orcid_status

Retrieve ORCID status for a specific admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_orcid_status()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetOrcidStatusResponse](../../models/operations/getorcidstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_users

Retrieve a list of all users

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.list_users(items_per_page=526212, search_term='<value>', selected_page=540061, sort_key='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `items_per_page`   | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `search_term`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `selected_page`    | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `sort_key`         | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.ListUsersResponse](../../models/operations/listusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_metrics_from_report

Add usage metrics from a SUSHI report

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.add_metrics_from_report(report_on_disk='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `report_on_disk`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.AddMetricsFromReportResponse](../../models/operations/addmetricsfromreportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_send_to_hub

Send data count to the admin hub.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_send_to_hub()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.AdminSendToHubResponse](../../models/operations/adminsendtohubresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_usage_metrics_from_sushi_repo

Add usage metrics for a specific Dataverse file from a SUSHI Report

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.add_usage_metrics_from_sushi_repo(id='<value>', report_on_disk='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `report_on_disk`   | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.AddUsageMetricsFromSushiRepoResponse](../../models/operations/addusagemetricsfromsushireporesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_dataset_citations

Updates the citation count for a specified dataset

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_dataset_citations(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateDatasetCitationsResponse](../../models/operations/updatedatasetcitationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_export_timestamps

Retrieve the export timestamps

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_export_timestamps()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetExportTimestampsResponse](../../models/operations/getexporttimestampsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_metadata_export_all

Fetches all metadata for export by admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_metadata_export_all()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetMetadataExportAllResponse](../../models/operations/getmetadataexportallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_metadata_export_oai_spec

Update the OAI export specification using provided 'specname'

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_metadata_export_oai_spec(specname='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `specname`         | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.AdminMetadataExportOAISpecResponse](../../models/operations/adminmetadataexportoaispecresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## re_export_all_metadata

Retrieves and exports all metadata

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.re_export_all_metadata()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.ReExportAllMetadataResponse](../../models/operations/reexportallmetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_metadata_re_export

Retrieves and re-exports the specific metadata for the dataset using dataset ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_metadata_re_export(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetMetadataReExportResponse](../../models/operations/getmetadatareexportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_permissions

Retrieve specific admin permission details

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_permissions(dvo='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `dvo`              | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminPermissionsResponse](../../models/operations/getadminpermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## publish_dataverse_as_creator

Publish Dataverse as creator using the given ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.publish_dataverse_as_creator(id=453435)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PublishDataverseAsCreatorResponse](../../models/operations/publishdataverseascreatorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_register_data_file_all

Retrieve all registered data files from the admin.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_register_data_file_all()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetRegisterDataFileAllResponse](../../models/operations/getregisterdatafileallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_register_data_files_by_alias

Retrieve data file registration details for a given alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_register_data_files_by_alias(alias='<value>', sleep=973941)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |
| `sleep`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetRegisterDataFilesByAliasResponse](../../models/operations/getregisterdatafilesbyaliasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_admin_signed_url

Admin sends a request to receive a signed URL.

### Example Usage

```python
import pydataverse
from pydataverse.models import operations

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_admin_signed_url(request=operations.PostAdminSignedURLRequestBody())

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PostAdminSignedURLRequestBody](../../models/operations/postadminsignedurlrequestbody.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PostAdminSignedURLResponse](../../models/operations/postadminsignedurlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_roles

Retrieve a list of all admin roles

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_roles()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminRolesResponse](../../models/operations/getadminrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_admin_role

Create a new admin role

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.create_admin_role()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.CreateAdminRoleResponse](../../models/operations/createadminroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_admin_role

Delete a specific admin role

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_admin_role(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAdminRoleResponse](../../models/operations/deleteadminroleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_saved_searches

Retrieves all saved searches in the system.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_saved_searches()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetSavedSearchesResponse](../../models/operations/getsavedsearchesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_saved_search

Adds a new saved search to the system.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.add_saved_search()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.AddSavedSearchResponse](../../models/operations/addsavedsearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_saved_searches_list

Retrieve a list of all saved searches by the administrator

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_saved_searches_list()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetSavedSearchesListResponse](../../models/operations/getsavedsearcheslistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_all_saved_search_links

Updates all saved search links

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_all_saved_search_links(debug=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `debug`            | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.UpdateAllSavedSearchLinksResponse](../../models/operations/updateallsavedsearchlinksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## make_links_for_saved_search

Updates the link for a specific saved search by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.make_links_for_saved_search(id=882350, debug=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |
| `debug`            | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.MakeLinksForSavedSearchResponse](../../models/operations/makelinksforsavedsearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_saved_search

Retrieves a saved search by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_saved_search(id=731650)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetSavedSearchResponse](../../models/operations/getsavedsearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_saved_search

Deletes a saved search by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_saved_search(id=364122)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteSavedSearchResponse](../../models/operations/deletesavedsearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_settings

Retrieve administrator settings

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_settings()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminSettingsResponse](../../models/operations/getadminsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_setting

Retrieve a specified admin setting

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_setting(name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminSettingResponse](../../models/operations/getadminsettingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_admin_setting

Update a specified admin setting

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_admin_setting(name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateAdminSettingResponse](../../models/operations/updateadminsettingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_admin_setting

Delete a specified admin setting

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_admin_setting(name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAdminSettingResponse](../../models/operations/deleteadminsettingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_admin_settings_lang

Update a specific Admin setting for a given language

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_admin_settings_lang(lang='<value>', name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `lang`             | *str*              | :heavy_check_mark: | N/A                |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateAdminSettingsLangResponse](../../models/operations/updateadminsettingslangresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_admin_settings_lang

Delete a specific Admin setting for a given language

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_admin_settings_lang(lang='<value>', name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `lang`             | *str*              | :heavy_check_mark: | N/A                |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAdminSettingsLangResponse](../../models/operations/deleteadminsettingslangresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## generate_sitemap

Generate a new sitemap for the application

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.generate_sitemap()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GenerateSitemapResponse](../../models/operations/generatesitemapresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_storage_sites

Fetches all storage sites

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_storage_sites()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetStorageSitesResponse](../../models/operations/getstoragesitesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_storage_site

Creates a new storage site

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.create_storage_site()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.CreateStorageSiteResponse](../../models/operations/createstoragesiteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## fetch_storage_site

Retrieves details of a specific storage site by its unique identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.fetch_storage_site(id=259428)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.FetchStorageSiteResponse](../../models/operations/fetchstoragesiteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_storage_site

Deletes a specific storage site by its unique identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_storage_site(id=969351)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteStorageSiteResponse](../../models/operations/deletestoragesiteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_primary_storage

Update the primary storage of a storage site by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_primary_storage(id=206518)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdatePrimaryStorageResponse](../../models/operations/updateprimarystorageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## submit_dataset_version_to_archive

Submit a specific dataset version to the archive by using provided dataset ID and version number

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.submit_dataset_version_to_archive(id='<value>', version='<value>')

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

**[operations.SubmitDatasetVersionToArchiveResponse](../../models/operations/submitdatasetversiontoarchiveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_create_super_user

Creates a new superuser with the provided identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_create_super_user(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.AdminCreateSuperUserResponse](../../models/operations/admincreatesuperuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_admin_template

Delete an admin template by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_admin_template(id=195565)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAdminTemplateResponse](../../models/operations/deleteadmintemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_templates

Retrieve all admin templates

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_templates()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminTemplatesResponse](../../models/operations/getadmintemplatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_template

Retrieve a specific admin template using its alias.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_template(alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias`            | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminTemplateResponse](../../models/operations/getadmintemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_external_tools_1

Gets an external tool associated with a specific dataset identified by its id

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_external_tools_1(id='<value>', type='<value>')

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

**[operations.GetExternalTools1Response](../../models/operations/getexternaltools1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_external_tool_by_id

Retrieve the details of a specific external tool by its ID for a given file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_external_tool_by_id(id='<value>', tool_id='<value>', type='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `tool_id`          | *str*              | :heavy_check_mark: | N/A                |
| `type`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetExternalToolByIDResponse](../../models/operations/getexternaltoolbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_external_tools_1_1

Retrieve the external tools of a specific test file.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_external_tools_1_1(id='<value>', type='<value>')

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

**[operations.GetExternalTools11Response](../../models/operations/getexternaltools11response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_hash_values

Retrieve hash values based on specified algorithm

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_hash_values(alg='<value>', num=972785)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alg`              | *str*              | :heavy_check_mark: | N/A                |
| `num`              | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetHashValuesResponse](../../models/operations/gethashvaluesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_validate_dataset_files

Retrieve and validate specified dataset files

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_validate_dataset_files(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetValidateDatasetFilesResponse](../../models/operations/getvalidatedatasetfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## validate_dataset

Validate a dataset with a specified ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.validate_dataset(id='<value>', variables=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |
| `variables`        | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.ValidateDatasetResponse](../../models/operations/validatedatasetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_validate_datasets

Validate datasets in the system

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_validate_datasets(variables=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `variables`        | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.AdminValidateDatasetsResponse](../../models/operations/adminvalidatedatasetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## validate_data_file_hash

Validate hash value of the specified data file

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.validate_data_file_hash(file_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `file_id`          | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.ValidateDataFileHashResponse](../../models/operations/validatedatafilehashresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## validate_admin_password

Validates the password of an admin user

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.validate_admin_password()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.ValidateAdminPasswordResponse](../../models/operations/validateadminpasswordresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_workflows

Retrieve all workflows associated with the admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_workflows()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAdminWorkflowsResponse](../../models/operations/getadminworkflowsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_admin_workflow

Create a new workflow for the admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.create_admin_workflow()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.CreateAdminWorkflowResponse](../../models/operations/createadminworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_default_workflow

Fetch default workflow configured for admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_default_workflow()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetDefaultWorkflowResponse](../../models/operations/getdefaultworkflowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_trigger_type

Retrieve a specific trigger type from workflows

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_trigger_type(trigger_type='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `trigger_type`     | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTriggerTypeResponse](../../models/operations/gettriggertyperesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_trigger_type

Update a specific trigger type in workflows

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_trigger_type(trigger_type='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `trigger_type`     | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UpdateTriggerTypeResponse](../../models/operations/updatetriggertyperesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_trigger_type

Delete a specific trigger type from workflows

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_trigger_type(trigger_type='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `trigger_type`     | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteTriggerTypeResponse](../../models/operations/deletetriggertyperesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_ip_whitelist

Retrieve current IP Whitelist for admin workflows

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_ip_whitelist()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetIPWhitelistResponse](../../models/operations/getipwhitelistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_ip_whitelist

Update the IP Whitelist for admin workflows

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.update_ip_whitelist()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.UpdateIPWhitelistResponse](../../models/operations/updateipwhitelistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_ip_whitelist

Remove the IP Whitelist for admin workflows

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.delete_ip_whitelist()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.DeleteIPWhitelistResponse](../../models/operations/deleteipwhitelistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_workflow_by_identifier

Retrieve a specific workflow using its identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_workflow_by_identifier(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetWorkflowByIdentifierResponse](../../models/operations/getworkflowbyidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_admin_data_file

Retrieve data file details registered by a specific admin

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.get_admin_data_file(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAdminDataFileResponse](../../models/operations/getadmindatafileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## admin_reregister_hdl_to_pid

Admin reruns the HDL to PID registration for a specific admin ID.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.admin_reregister_hdl_to_pid(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.AdminReregisterHDLToPIDResponse](../../models/operations/adminreregisterhdltopidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
