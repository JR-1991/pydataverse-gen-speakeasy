# pydataverse

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

## ReadMe Documentation

[Go to the documentation](https://test-dv.readme.io/reference/)

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/JR-1991/pydataverse-gen-speakeasy.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [access](docs/sdks/access/README.md)

* [get_datafile_bundle](docs/sdks/access/README.md#get_datafile_bundle) - Retrieve a zip of the datafile bundle identified by the file ID.
* [get_datafile](docs/sdks/access/README.md#get_datafile) - Retrieves datafile details based on given fileId
* [get_datafile_auxiliary](docs/sdks/access/README.md#get_datafile_auxiliary) - Retrieve auxiliary data for a specific datafile.
* [access_datafile_auxiliary_get](docs/sdks/access/README.md#access_datafile_auxiliary_get) - Retrieve details of a specific auxiliary data file
* [access_datafile_auxiliary_create](docs/sdks/access/README.md#access_datafile_auxiliary_create) - Create a new auxiliary data file for a particular data file
* [access_datafile_auxiliary_delete](docs/sdks/access/README.md#access_datafile_auxiliary_delete) - Delete a specific auxiliary data file
* [get_datafile_auxiliary_info](docs/sdks/access/README.md#get_datafile_auxiliary_info) - Retrieve auxiliary information of specific datafile
* [get_datafile_metadata](docs/sdks/access/README.md#get_datafile_metadata) - Retrieve metadata for a specific datafile
* [get_datafile_meta_ddi](docs/sdks/access/README.md#get_datafile_meta_ddi) - Retrieve DDI metadata for a specific datafile.
* [grant_datafile_access](docs/sdks/access/README.md#grant_datafile_access) - Grants access to a specific datafile using its ID and the identifier of the user
* [get_datafile_requests](docs/sdks/access/README.md#get_datafile_requests) - Retrieves a list of all requests relevant to a specified datafile
* [reject_data_access](docs/sdks/access/README.md#reject_data_access) - Reject access to specified datafile using ids
* [request_file_access](docs/sdks/access/README.md#request_file_access) - Requests access to a specific datafile by ID.
* [delete_file_access](docs/sdks/access/README.md#delete_file_access) - Revoke access to a specific file using its ID and an identifier
* [get_user_file_access_requested](docs/sdks/access/README.md#get_user_file_access_requested) - Retrieve the status of a user file access request
* [get_user_file_permissions](docs/sdks/access/README.md#get_user_file_permissions) - Retrieve user permissions for a specific datafile.
* [post_data_file_access](docs/sdks/access/README.md#post_data_file_access) - Uploads access details of a data file
* [get_access_data_files](docs/sdks/access/README.md#get_access_data_files) - Retrieve access data for specified files
* [get_dataset_access](docs/sdks/access/README.md#get_dataset_access) - Retrieve access information for a specific dataset
* [get_dataset_version_access](docs/sdks/access/README.md#get_dataset_version_access) - Retrieve specific version of an accessible dataset by ID
* [get_ds_card_image](docs/sdks/access/README.md#get_ds_card_image) - Retrieves the version-specific Data Card image
* [get_dataverse_card_image](docs/sdks/access/README.md#get_dataverse_card_image) - Fetch the Dataverse card image
* [get_file_card_image](docs/sdks/access/README.md#get_file_card_image) - Retrieves the card image for the specified file ID.
* [allow_access_request](docs/sdks/access/README.md#allow_access_request) - Update permission to allow access request based on the provided ID

### [admin](docs/sdks/admin/README.md)

* [archive_all_unarchived_versions](docs/sdks/admin/README.md#archive_all_unarchived_versions) - Archives all unarchived dataset versions. Allows options to limit the number of versions archived, archive only the latest versions, or simply list the versions that would be archived without actually doing it.
* [get_admin_assignee](docs/sdks/admin/README.md#get_admin_assignee) - Retrieve a specific assignee detail by ID.
* [get_assignees_detail](docs/sdks/admin/README.md#get_assignees_detail) - Retrieve details of a specific assignee by raIdtf
* [~~get_authenticated_users~~](docs/sdks/admin/README.md#get_authenticated_users) - Retrieves a list of authenticated users. This endpoint is deprecated. :warning: **Deprecated**
* [create_authenticated_user](docs/sdks/admin/README.md#create_authenticated_user) - Creates a new authenticated user.
* [convert_user_to_o_auth](docs/sdks/admin/README.md#convert_user_to_o_auth) - Convert an authenticated user from built-in to OAuth
* [convert_auth_users](docs/sdks/admin/README.md#convert_auth_users) - Convert Authenticated Users from Built-in system to Shibboleth
* [delete_authenticated_user](docs/sdks/admin/README.md#delete_authenticated_user) - Delete an authenticated user by ID
* [convert_remote_to_built_in](docs/sdks/admin/README.md#convert_remote_to_built_in) - Converts a remote user to a built-in user by their ID
* [~~convert_user_authentication_method~~](docs/sdks/admin/README.md#convert_user_authentication_method) - Converts the authentication method of an authenticated user from Shibboleth to Built-In. :warning: **Deprecated**
* [deactivate_user](docs/sdks/admin/README.md#deactivate_user) - Deactivates an authenticated user by ID
* [get_authenticated_user](docs/sdks/admin/README.md#get_authenticated_user) - Retrieve details of a specified authenticated user
* [delete_authenticated_user_1](docs/sdks/admin/README.md#delete_authenticated_user_1) - Delete a specified authenticated user
* [deactivate_user_1](docs/sdks/admin/README.md#deactivate_user_1) - Deactivate an authenticated user by identifier
* [get_auth_provider_factories](docs/sdks/admin/README.md#get_auth_provider_factories) - Retrieve all authentication provider factories
* [get_auth_providers](docs/sdks/admin/README.md#get_auth_providers) - Retrieve list of authentication providers
* [add_auth_provider](docs/sdks/admin/README.md#add_auth_provider) - Add a new authentication provider
* [get_auth_providers_by_id](docs/sdks/admin/README.md#get_auth_providers_by_id) - Fetch specific authentication provider using ID
* [remove_auth_providers_by_id](docs/sdks/admin/README.md#remove_auth_providers_by_id) - Delete specific authentication provider using ID
* [enable_auth_provider](docs/sdks/admin/README.md#enable_auth_provider) - Enable a specific authentication provider by its ID
* [get_auth_provider_status](docs/sdks/admin/README.md#get_auth_provider_status) - Retrieves the status of a specific authentication provider
* [update_auth_provider_status](docs/sdks/admin/README.md#update_auth_provider_status) - Updates the status of a specific authentication provider
* [get_banner_message](docs/sdks/admin/README.md#get_banner_message) - Retrieve a current banner message
* [post_banner_message](docs/sdks/admin/README.md#post_banner_message) - Add a new banner message
* [delete_banner_message](docs/sdks/admin/README.md#delete_banner_message) - Delete a specific banner message by ID
* [deactivate_banner_message](docs/sdks/admin/README.md#deactivate_banner_message) - Deactivates a specific banner message
* [get_batch_jobs](docs/sdks/admin/README.md#get_batch_jobs) - Retrieve all batch jobs
* [get_job_by_name](docs/sdks/admin/README.md#get_job_by_name) - Retrieve details for a job given its name
* [get_admin_job_by_id](docs/sdks/admin/README.md#get_admin_job_by_id) - Retrieve details of a specific admin batch job
* [delete_metrics_cache](docs/sdks/admin/README.md#delete_metrics_cache) - Deletes the metrics cache for admin
* [delete_metrics_cache_1](docs/sdks/admin/README.md#delete_metrics_cache_1) - Deletes a specific metric cache.
* [delete_thumbnail_failure_flag](docs/sdks/admin/README.md#delete_thumbnail_failure_flag) - Deletes a thumbnail failure flag
* [admin_clear_thumbnail_failure_flag](docs/sdks/admin/README.md#admin_clear_thumbnail_failure_flag) - Delete the thumbnail failure flag for a specified Dataverse id
* [compute_file_hash_value](docs/sdks/admin/README.md#compute_file_hash_value) - Computes the hash value of the specified file using the given algorithm
* [get_user_id_conf_email](docs/sdks/admin/README.md#get_user_id_conf_email) - Retrieve Confirmation Email Associated with User ID
* [post_user_id_conf_email](docs/sdks/admin/README.md#post_user_id_conf_email) - Send Confirmation Email to User ID
* [admin_convert_user_encryption](docs/sdks/admin/README.md#admin_convert_user_encryption) - Convert a user's encryption scheme from Bcrypt to Sha1
* [get_fix_missing_original_sizes](docs/sdks/admin/README.md#get_fix_missing_original_sizes) - Retrieve a limited number of records with missing original sizes and fix them
* [fix_missing_original_types](docs/sdks/admin/README.md#fix_missing_original_types) - Retrieve a report of datafiles with missing original types and apply fixes
* [get_admin_dataset_field](docs/sdks/admin/README.md#get_admin_dataset_field) - Retrieve the dataset fields available to administrators
* [get_controlled_vocabulary](docs/sdks/admin/README.md#get_controlled_vocabulary) - Retrieve a list of controlled vocabulary subjects
* [load_dataset_field_admin](docs/sdks/admin/README.md#load_dataset_field_admin) - Load dataset field as an admin
* [get_na_controlled_vocab_value](docs/sdks/admin/README.md#get_na_controlled_vocab_value) - Retrieve North American controlled vocabulary value
* [admin_load_property_files](docs/sdks/admin/README.md#admin_load_property_files) - Load dataset field property files as a ZIP.
* [get_dataset_field_name](docs/sdks/admin/README.md#get_dataset_field_name) - Retrieve information of the specified dataset field
* [post_fix_missing_unf](docs/sdks/admin/README.md#post_fix_missing_unf) - Update or recalculate dataset integrity by fixing missing UNF in specified dataset version
* [get_thumbnail_metadata_by_id](docs/sdks/admin/README.md#get_thumbnail_metadata_by_id) - Retrieves thumbnail metadata for a specific dataset using its ID
* [get_curation_label_sets](docs/sdks/admin/README.md#get_curation_label_sets) - Retrieve all curation label sets
* [get_storage_drivers](docs/sdks/admin/README.md#get_storage_drivers) - Retrieves all storage drivers
* [get_role_assignments](docs/sdks/admin/README.md#get_role_assignments) - Retrieve role assignments associated with a dataverse
* [get_curation_label_set](docs/sdks/admin/README.md#get_curation_label_set) - Retrieve the curation label set of the specified Dataverse
* [update_curation_label_set](docs/sdks/admin/README.md#update_curation_label_set) - Update or create a curation label set for the specified Dataverse
* [delete_curation_label_set](docs/sdks/admin/README.md#delete_curation_label_set) - Remove the curation label set from the specified Dataverse
* [get_storage_driver](docs/sdks/admin/README.md#get_storage_driver) - Retrieve the storage driver of a specific dataverse
* [update_storage_driver](docs/sdks/admin/README.md#update_storage_driver) - Update the storage driver of a specific dataverse
* [delete_storage_driver](docs/sdks/admin/README.md#delete_storage_driver) - Remove the storage driver of a specific dataverse
* [get_tmp_file](docs/sdks/admin/README.md#get_tmp_file) - Retrieve a temporary file via its fully qualified path
* [get_external_tools](docs/sdks/admin/README.md#get_external_tools) - Retrieve a list of all external tools
* [create_external_tool](docs/sdks/admin/README.md#create_external_tool) - Create a new external tool
* [get_external_tool](docs/sdks/admin/README.md#get_external_tool) - Retrieve an external tool by its ID
* [delete_external_tool](docs/sdks/admin/README.md#delete_external_tool) - Delete an external tool by its ID
* [post_admin_feedback](docs/sdks/admin/README.md#post_admin_feedback) - Create or post feedback as an admin
* [get_admin_groups_domain](docs/sdks/admin/README.md#get_admin_groups_domain) - Retrieve domain-related groups information from the admin endpoint
* [post_admin_groups_domain](docs/sdks/admin/README.md#post_admin_groups_domain) - Submit new domain-related groups information to the admin endpoint
* [get_group_alias](docs/sdks/admin/README.md#get_group_alias) - Retrieves information of the group alias specified in the path
* [update_group_alias](docs/sdks/admin/README.md#update_group_alias) - Updates the group alias specified in the path
* [delete_group_alias](docs/sdks/admin/README.md#delete_group_alias) - Deletes the group alias specified in the path
* [get_admin_groups_ip](docs/sdks/admin/README.md#get_admin_groups_ip) - Retrieve IP-based groups information
* [post_admin_groups_ip](docs/sdks/admin/README.md#post_admin_groups_ip) - Create a new IP-based group
* [get_group_by_group_idtf](docs/sdks/admin/README.md#get_group_by_group_idtf) - Fetches a group by the groupIdtf provided in the path
* [delete_group_by_group_idtf](docs/sdks/admin/README.md#delete_group_by_group_idtf) - Deletes a group by the groupIdtf provided in the path
* [get_shib_group_info](docs/sdks/admin/README.md#get_shib_group_info) - Retrieve information about Shibboleth groups
* [create_shib_group](docs/sdks/admin/README.md#create_shib_group) - Create a new Shibboleth group
* [delete_shib_group](docs/sdks/admin/README.md#delete_shib_group) - Delete a Shibboleth Group by given Primary Key
* [get_admin_index](docs/sdks/admin/README.md#get_admin_index) - Retrieve details of admin index with queried parameters
* [clear_admin_index](docs/sdks/admin/README.md#clear_admin_index) - Clears the admin index
* [clear_orphans_index](docs/sdks/admin/README.md#clear_orphans_index) - Retrieve and clear orphans from the admin index
* [continue_index_processing](docs/sdks/admin/README.md#continue_index_processing) - Continues the process of indexing partitions based on given parameters.
* [get_dataset_index](docs/sdks/admin/README.md#get_dataset_index) - Retrieve the index of a dataset given its persistentId
* [delete_dataset_by_id](docs/sdks/admin/README.md#delete_dataset_by_id) - Delete a specific dataset by its ID
* [get_file_metadata1](docs/sdks/admin/README.md#get_file_metadata1) - Retrieve file metadata for a specific dataset
* [file_search_index_get](docs/sdks/admin/README.md#file_search_index_get) - This endpoint retrieves data about file search index by persistentId, q, and/or semanticVersion.
* [get_admin_index_mod](docs/sdks/admin/README.md#get_admin_index_mod) - Retrieves modification of the admin index based on provided query parameters
* [get_admin_index_perms](docs/sdks/admin/README.md#get_admin_index_perms) - Retrieve permissions for the admin index
* [get_admin_index_perms_1](docs/sdks/admin/README.md#get_admin_index_perms_1) - Retrieve a specific admin index permissions by ID
* [get_perms_debug_info](docs/sdks/admin/README.md#get_perms_debug_info) - Retrieves permission debug info for specified id and key
* [get_solr_schema](docs/sdks/admin/README.md#get_solr_schema) - Retrieve the Solr schema configuration.
* [get_admin_index_status](docs/sdks/admin/README.md#get_admin_index_status) - Retrieve status of the admin index
* [get_admin_test_index](docs/sdks/admin/README.md#get_admin_test_index) - Obtain specific parameters from the Admin Test Index
* [delete_admin_index_timestamps](docs/sdks/admin/README.md#delete_admin_index_timestamps) - Delete timestamps from the admin index
* [delete_index_timestamp](docs/sdks/admin/README.md#delete_index_timestamp) - Delete index timestamp by dvObjectId
* [get_admin_index_type_by_id](docs/sdks/admin/README.md#get_admin_index_type_by_id) - Retrieves specific type and ID details in admin index
* [get_orcid_status](docs/sdks/admin/README.md#get_orcid_status) - Retrieve ORCID status for a specific admin
* [list_users](docs/sdks/admin/README.md#list_users) - Retrieve a list of all users
* [add_metrics_from_report](docs/sdks/admin/README.md#add_metrics_from_report) - Add usage metrics from a SUSHI report
* [admin_send_to_hub](docs/sdks/admin/README.md#admin_send_to_hub) - Send data count to the admin hub.
* [add_usage_metrics_from_sushi_repo](docs/sdks/admin/README.md#add_usage_metrics_from_sushi_repo) - Add usage metrics for a specific Dataverse file from a SUSHI Report
* [update_dataset_citations](docs/sdks/admin/README.md#update_dataset_citations) - Updates the citation count for a specified dataset
* [get_export_timestamps](docs/sdks/admin/README.md#get_export_timestamps) - Retrieve the export timestamps
* [get_metadata_export_all](docs/sdks/admin/README.md#get_metadata_export_all) - Fetches all metadata for export by admin
* [admin_metadata_export_oai_spec](docs/sdks/admin/README.md#admin_metadata_export_oai_spec) - Update the OAI export specification using provided 'specname'
* [re_export_all_metadata](docs/sdks/admin/README.md#re_export_all_metadata) - Retrieves and exports all metadata
* [get_metadata_re_export](docs/sdks/admin/README.md#get_metadata_re_export) - Retrieves and re-exports the specific metadata for the dataset using dataset ID
* [get_admin_permissions](docs/sdks/admin/README.md#get_admin_permissions) - Retrieve specific admin permission details
* [publish_dataverse_as_creator](docs/sdks/admin/README.md#publish_dataverse_as_creator) - Publish Dataverse as creator using the given ID
* [get_register_data_file_all](docs/sdks/admin/README.md#get_register_data_file_all) - Retrieve all registered data files from the admin.
* [get_register_data_files_by_alias](docs/sdks/admin/README.md#get_register_data_files_by_alias) - Retrieve data file registration details for a given alias
* [post_admin_signed_url](docs/sdks/admin/README.md#post_admin_signed_url) - Admin sends a request to receive a signed URL.
* [get_admin_roles](docs/sdks/admin/README.md#get_admin_roles) - Retrieve a list of all admin roles
* [create_admin_role](docs/sdks/admin/README.md#create_admin_role) - Create a new admin role
* [delete_admin_role](docs/sdks/admin/README.md#delete_admin_role) - Delete a specific admin role
* [get_saved_searches](docs/sdks/admin/README.md#get_saved_searches) - Retrieves all saved searches in the system.
* [add_saved_search](docs/sdks/admin/README.md#add_saved_search) - Adds a new saved search to the system.
* [get_saved_searches_list](docs/sdks/admin/README.md#get_saved_searches_list) - Retrieve a list of all saved searches by the administrator
* [update_all_saved_search_links](docs/sdks/admin/README.md#update_all_saved_search_links) - Updates all saved search links
* [make_links_for_saved_search](docs/sdks/admin/README.md#make_links_for_saved_search) - Updates the link for a specific saved search by ID
* [get_saved_search](docs/sdks/admin/README.md#get_saved_search) - Retrieves a saved search by ID
* [delete_saved_search](docs/sdks/admin/README.md#delete_saved_search) - Deletes a saved search by ID
* [get_admin_settings](docs/sdks/admin/README.md#get_admin_settings) - Retrieve administrator settings
* [get_admin_setting](docs/sdks/admin/README.md#get_admin_setting) - Retrieve a specified admin setting
* [update_admin_setting](docs/sdks/admin/README.md#update_admin_setting) - Update a specified admin setting
* [delete_admin_setting](docs/sdks/admin/README.md#delete_admin_setting) - Delete a specified admin setting
* [update_admin_settings_lang](docs/sdks/admin/README.md#update_admin_settings_lang) - Update a specific Admin setting for a given language
* [delete_admin_settings_lang](docs/sdks/admin/README.md#delete_admin_settings_lang) - Delete a specific Admin setting for a given language
* [generate_sitemap](docs/sdks/admin/README.md#generate_sitemap) - Generate a new sitemap for the application
* [get_storage_sites](docs/sdks/admin/README.md#get_storage_sites) - Fetches all storage sites
* [create_storage_site](docs/sdks/admin/README.md#create_storage_site) - Creates a new storage site
* [fetch_storage_site](docs/sdks/admin/README.md#fetch_storage_site) - Retrieves details of a specific storage site by its unique identifier
* [delete_storage_site](docs/sdks/admin/README.md#delete_storage_site) - Deletes a specific storage site by its unique identifier
* [update_primary_storage](docs/sdks/admin/README.md#update_primary_storage) - Update the primary storage of a storage site by ID
* [submit_dataset_version_to_archive](docs/sdks/admin/README.md#submit_dataset_version_to_archive) - Submit a specific dataset version to the archive by using provided dataset ID and version number
* [admin_create_super_user](docs/sdks/admin/README.md#admin_create_super_user) - Creates a new superuser with the provided identifier
* [delete_admin_template](docs/sdks/admin/README.md#delete_admin_template) - Delete an admin template by ID
* [get_admin_templates](docs/sdks/admin/README.md#get_admin_templates) - Retrieve all admin templates
* [get_admin_template](docs/sdks/admin/README.md#get_admin_template) - Retrieve a specific admin template using its alias.
* [get_external_tools_1](docs/sdks/admin/README.md#get_external_tools_1) - Gets an external tool associated with a specific dataset identified by its id
* [get_external_tool_by_id](docs/sdks/admin/README.md#get_external_tool_by_id) - Retrieve the details of a specific external tool by its ID for a given file
* [get_external_tools_1_1](docs/sdks/admin/README.md#get_external_tools_1_1) - Retrieve the external tools of a specific test file.
* [get_hash_values](docs/sdks/admin/README.md#get_hash_values) - Retrieve hash values based on specified algorithm
* [get_validate_dataset_files](docs/sdks/admin/README.md#get_validate_dataset_files) - Retrieve and validate specified dataset files
* [validate_dataset](docs/sdks/admin/README.md#validate_dataset) - Validate a dataset with a specified ID
* [admin_validate_datasets](docs/sdks/admin/README.md#admin_validate_datasets) - Validate datasets in the system
* [validate_data_file_hash](docs/sdks/admin/README.md#validate_data_file_hash) - Validate hash value of the specified data file
* [validate_admin_password](docs/sdks/admin/README.md#validate_admin_password) - Validates the password of an admin user
* [get_admin_workflows](docs/sdks/admin/README.md#get_admin_workflows) - Retrieve all workflows associated with the admin
* [create_admin_workflow](docs/sdks/admin/README.md#create_admin_workflow) - Create a new workflow for the admin
* [get_default_workflow](docs/sdks/admin/README.md#get_default_workflow) - Fetch default workflow configured for admin
* [get_trigger_type](docs/sdks/admin/README.md#get_trigger_type) - Retrieve a specific trigger type from workflows
* [update_trigger_type](docs/sdks/admin/README.md#update_trigger_type) - Update a specific trigger type in workflows
* [delete_trigger_type](docs/sdks/admin/README.md#delete_trigger_type) - Delete a specific trigger type from workflows
* [get_ip_whitelist](docs/sdks/admin/README.md#get_ip_whitelist) - Retrieve current IP Whitelist for admin workflows
* [update_ip_whitelist](docs/sdks/admin/README.md#update_ip_whitelist) - Update the IP Whitelist for admin workflows
* [delete_ip_whitelist](docs/sdks/admin/README.md#delete_ip_whitelist) - Remove the IP Whitelist for admin workflows
* [get_workflow_by_identifier](docs/sdks/admin/README.md#get_workflow_by_identifier) - Retrieve a specific workflow using its identifier
* [get_admin_data_file](docs/sdks/admin/README.md#get_admin_data_file) - Retrieve data file details registered by a specific admin
* [admin_reregister_hdl_to_pid](docs/sdks/admin/README.md#admin_reregister_hdl_to_pid) - Admin reruns the HDL to PID registration for a specific admin ID.


### [application.wadl](docs/sdks/wadl/README.md)

* [get_application_wadl](docs/sdks/wadl/README.md#get_application_wadl) - Retrieves the application WADL
* [get_application_wadl_1](docs/sdks/wadl/README.md#get_application_wadl_1) - Retrieve the application WADL

### [batch](docs/sdks/batch/README.md)

* [get_batch_harvest](docs/sdks/batch/README.md#get_batch_harvest) - Retrieves information about a batch harvest based on provided parameters
* [get_batch_import_status](docs/sdks/batch/README.md#get_batch_import_status) - Retrieve status of a batch import request
* [create_batch_import](docs/sdks/batch/README.md#create_batch_import) - Initiate a new batch import request
* [post_batch_job_import_datasets](docs/sdks/batch/README.md#post_batch_job_import_datasets) - Initiate a batch job for importing datasets using the provided identifier

### [builtin_users](docs/sdks/builtinusers/README.md)

* [post_builtin_users](docs/sdks/builtinusers/README.md#post_builtin_users) - Create a new builtin user
* [create_builtin_user](docs/sdks/builtinusers/README.md#create_builtin_user) - Create a new built-in user using a password and key
* [create_builtin_user_1](docs/sdks/builtinusers/README.md#create_builtin_user_1) - Create a new builtin-user with a specific key, password and email notification preference.
* [get_api_token_by_username](docs/sdks/builtinusers/README.md#get_api_token_by_username) - Gets the API token for the specified built-in user

### [datasets](docs/sdks/datasets/README.md)

* [get_datasets_export](docs/sdks/datasets/README.md#get_datasets_export) - Retrieves export information of a dataset given its exporter and persistent ID
* [get_curation_states](docs/sdks/datasets/README.md#get_curation_states) - Retrieve a list of curation states for datasets
* [get_dataset_locks](docs/sdks/datasets/README.md#get_dataset_locks) - Retrieve information about locks on datasets
* [modify_all_registrations](docs/sdks/datasets/README.md#modify_all_registrations) - Modifies registration details for all datasets
* [get_registration_pid_metadata](docs/sdks/datasets/README.md#get_registration_pid_metadata) - Retrieve registration PID metadata of all datasets
* [update_dataset_upload](docs/sdks/datasets/README.md#update_dataset_upload) - Update a multi-part upload for a dataset using the provided global ID, storage identifier, and upload ID
* [delete_dataset_upload](docs/sdks/datasets/README.md#delete_dataset_upload) - Delete a multi-part upload for a dataset using the provided global ID, storage identifier, and upload ID
* [get_private_url_dataset_version](docs/sdks/datasets/README.md#get_private_url_dataset_version) - Retrieves a dataset version using a private URL token
* [get_citation_by_private_url](docs/sdks/datasets/README.md#get_citation_by_private_url) - Retrieve citation information for a dataset version via a private URL token
* [get_summary_field_names](docs/sdks/datasets/README.md#get_summary_field_names) - Retrieve names of summary fields in the dataset
* [delete_dataset_link](docs/sdks/datasets/README.md#delete_dataset_link) - Delete a link between a dataset and a dataverse
* [get_allowed_curation_labels](docs/sdks/datasets/README.md#get_allowed_curation_labels) - Retrieve a list of allowed curation labels for a specific dataset
* [get_dataset_assignments](docs/sdks/datasets/README.md#get_dataset_assignments) - Retrieves assignments for a specific dataset
* [create_dataset_assignment](docs/sdks/datasets/README.md#create_dataset_assignment) - Creates an assignment for a specific dataset
* [delete_assignment](docs/sdks/datasets/README.md#delete_assignment) - Delete a specific assignment for a dataset
* [get_curation_label_set_1](docs/sdks/datasets/README.md#get_curation_label_set_1) - Retrieves the curation label set of the specified dataset
* [update_curation_label_set_1](docs/sdks/datasets/README.md#update_curation_label_set_1) - Updates the curation label set of the specified dataset
* [delete_curation_label_set_1](docs/sdks/datasets/README.md#delete_curation_label_set_1) - Deletes the curation label set for the specified dataset
* [validate_checksum](docs/sdks/datasets/README.md#validate_checksum) - Validate checksum for specified dataset
* [get_rsync_data_module](docs/sdks/datasets/README.md#get_rsync_data_module) - Retrieve the Rsync data capture module for a specific dataset
* [get_guestbook_entry](docs/sdks/datasets/README.md#get_guestbook_entry) - Retrieves a guestbook entry for a specific dataset
* [update_guestbook_entry](docs/sdks/datasets/README.md#update_guestbook_entry) - Updates a guestbook entry for a specific dataset
* [delete_guestbook_entry](docs/sdks/datasets/README.md#delete_guestbook_entry) - Deletes a guestbook entry for a specific dataset
* [lock_dataset](docs/sdks/datasets/README.md#lock_dataset) - Lock a specific dataset identified by the given identifier and type
* [get_dataset_locks_1](docs/sdks/datasets/README.md#get_dataset_locks_1) - Retrieves specific dataset locks
* [delete_dataset_locks](docs/sdks/datasets/README.md#delete_dataset_locks) - Deletes specific dataset locks
* [get_storage_driver_1](docs/sdks/datasets/README.md#get_storage_driver_1) - Retrieve the details of a specific storage driver based on the provided identifier
* [update_storage_driver_1](docs/sdks/datasets/README.md#update_storage_driver_1) - Update the details of a specific storage driver based on the provided identifier
* [delete_storage_driver_1](docs/sdks/datasets/README.md#delete_storage_driver_1) - Delete a specific storage driver based on the provided identifier
* [get_dataset_storage_size](docs/sdks/datasets/README.md#get_dataset_storage_size) - Retrieves the storage size of a dataset based on its identifier. An optional query parameter can be used to include cached files.
* [get_dataset_timestamps](docs/sdks/datasets/README.md#get_dataset_timestamps) - Retrieves the timestamps for a given dataset identified by the path parameter 'identifier'
* [get_download_size](docs/sdks/datasets/README.md#get_download_size) - Retrieve the download size of a specific version of a dataset
* [get_dataset](docs/sdks/datasets/README.md#get_dataset) - Retrieve the specified dataset
* [delete_dataset](docs/sdks/datasets/README.md#delete_dataset) - Delete the specified dataset
* [~~get_publish_dataset~~](docs/sdks/datasets/README.md#get_publish_dataset) - Retrieve publishing details of a designated dataset :warning: **Deprecated**
* [initiate_publishing](docs/sdks/datasets/README.md#initiate_publishing) - Publish a designated dataset with optional assurances
* [release_migrated_dataset](docs/sdks/datasets/README.md#release_migrated_dataset) - Release a migrated dataset with a specified ID
* [add_dataset](docs/sdks/datasets/README.md#add_dataset) - Add a new dataset to the existing record
* [add_files_to_dataset](docs/sdks/datasets/README.md#add_files_to_dataset) - Adds files to a specified dataset
* [add_globus_files_to_dataset](docs/sdks/datasets/README.md#add_globus_files_to_dataset) - Add globus files to a specific dataset
* [update_citation_date](docs/sdks/datasets/README.md#update_citation_date) - Update the citation date of a dataset based on dataset ID
* [delete_citation_date](docs/sdks/datasets/README.md#delete_citation_date) - Delete citation date of a dataset based on dataset ID
* [get_clean_storage_status](docs/sdks/datasets/README.md#get_clean_storage_status) - Get the status of the clean storage task for the specified dataset
* [get_curation_status](docs/sdks/datasets/README.md#get_curation_status) - Fetches the curation status of the specified dataset
* [update_curation_status](docs/sdks/datasets/README.md#update_curation_status) - Updates the curation status of the specified dataset
* [delete_curation_status](docs/sdks/datasets/README.md#delete_curation_status) - Deletes the curation status of the specified dataset
* [update_dataset_metadata](docs/sdks/datasets/README.md#update_dataset_metadata) - Update the metadata of a specific dataset
* [delete_dataset_1](docs/sdks/datasets/README.md#delete_dataset_1) - Delete a specific dataset by its ID.
* [get_dataset_directory_index](docs/sdks/datasets/README.md#get_dataset_directory_index) - Retrieve directory index of a dataset
* [edit_dataset_metadata](docs/sdks/datasets/README.md#edit_dataset_metadata) - Updates the metadata of a specific dataset represented by its ID
* [set_dataset_embargo](docs/sdks/datasets/README.md#set_dataset_embargo) - Set an embargo on a specific dataset's files
* [unset_embargo_on_dataset_files](docs/sdks/datasets/README.md#unset_embargo_on_dataset_files) - Unset embargo on files for a specific dataset
* [get_globus_download_parameters](docs/sdks/datasets/README.md#get_globus_download_parameters) - Retrieve the parameters for Globus download for a specified dataset
* [get_globus_upload_parameters](docs/sdks/datasets/README.md#get_globus_upload_parameters) - Retrieves Globus upload parameters for a specific dataset
* [get_dataset_links](docs/sdks/datasets/README.md#get_dataset_links) - Retrieves the links of a specified dataset
* [get_dataset_logo](docs/sdks/datasets/README.md#get_dataset_logo) - Retrieve the logo of a specific dataset
* [dataset_citation_count_get](docs/sdks/datasets/README.md#dataset_citation_count_get) - Retrieves the citation count for a specific dataset
* [get_dataset_metrics](docs/sdks/datasets/README.md#get_dataset_metrics) - Retrieve specific metrics for a specified dataset
* [get_dataset_metric](docs/sdks/datasets/README.md#get_dataset_metric) - Fetches a specific metric for a specific dataset
* [get_dataset_metadata](docs/sdks/datasets/README.md#get_dataset_metadata) - Retrieves the metadata of a dataset by its ID
* [update_dataset_metadata_1](docs/sdks/datasets/README.md#update_dataset_metadata_1) - Updates the metadata of a dataset by its ID, with an option to replace the existing metadata
* [update_metadata_deletion](docs/sdks/datasets/README.md#update_metadata_deletion) - Update the deletion status of the metadata of a specific dataset
* [get_registration_modification](docs/sdks/datasets/README.md#get_registration_modification) - Retrieve the modification details of a specific dataset registration
* [modify_dataset_registration_metadata](docs/sdks/datasets/README.md#modify_dataset_registration_metadata) - Modify the registration metadata of a specific dataset
* [monitor_globus_download](docs/sdks/datasets/README.md#monitor_globus_download) - Initiate the process to monitor a Globus download operation for a specific dataset
* [move_dataset_to_target](docs/sdks/datasets/README.md#move_dataset_to_target) - Moves a specific dataset to a target dataverse
* [get_private_url](docs/sdks/datasets/README.md#get_private_url) - Retrieve a specific dataset's private URL
* [create_private_url](docs/sdks/datasets/README.md#create_private_url) - Create a private URL for a specific dataset
* [delete_private_url](docs/sdks/datasets/README.md#delete_private_url) - Delete a specific dataset's private URL
* [replace_dataset_files](docs/sdks/datasets/README.md#replace_dataset_files) - Replace files in a specified dataset
* [submit_globus_download_request](docs/sdks/datasets/README.md#submit_globus_download_request) - Submit a request for Globus download for a specific dataset
* [post_globus_upload_paths_request](docs/sdks/datasets/README.md#post_globus_upload_paths_request) - Submit a request to get the paths for Globus file upload for a specified dataset
* [return_dataset_to_author](docs/sdks/datasets/README.md#return_dataset_to_author) - Returns the specified dataset back to its author
* [submit_dataset_for_review](docs/sdks/datasets/README.md#submit_dataset_for_review) - Submits a specified dataset for review
* [get_dataset_thumbnail](docs/sdks/datasets/README.md#get_dataset_thumbnail) - Retrieves a thumbnail from a specific dataset
* [post_dataset_thumbnail](docs/sdks/datasets/README.md#post_dataset_thumbnail) - Adds a thumbnail to a specific dataset
* [delete_dataset_thumbnail](docs/sdks/datasets/README.md#delete_dataset_thumbnail) - Deletes a thumbnail from a specific dataset
* [get_thumbnail_candidates](docs/sdks/datasets/README.md#get_thumbnail_candidates) - Retrieve the list of thumbnail candidates for a specific dataset
* [post_thumbnail_data](docs/sdks/datasets/README.md#post_thumbnail_data) - Upload a new thumbnail for a specific dataset
* [~~get_upload_id~~](docs/sdks/datasets/README.md#get_upload_id) - Retrieve the upload ID for the specified dataset :warning: **Deprecated**
* [get_upload_ur_ls](docs/sdks/datasets/README.md#get_upload_ur_ls) - Retrieve upload URLs for a specific dataset
* [get_user_permissions](docs/sdks/datasets/README.md#get_user_permissions) - Retrieve user permissions for a specific dataset
* [get_dataset_versions](docs/sdks/datasets/README.md#get_dataset_versions) - Retrieve versions of a specific dataset
* [get_dataset_version](docs/sdks/datasets/README.md#get_dataset_version) - Fetches the dataset version details, with options to exclude files or include deaccessioned ones
* [update_dataset_version](docs/sdks/datasets/README.md#update_dataset_version) - Updates the dataset version with the given ID
* [delete_dataset_version](docs/sdks/datasets/README.md#delete_dataset_version) - Deletes the specified version of a dataset
* [check_dataset_file_download_permission](docs/sdks/datasets/README.md#check_dataset_file_download_permission) - Checks if a user has permission to download at least one file from a specific dataset version
* [get_citation](docs/sdks/datasets/README.md#get_citation) - Retrieve the citation of a specific dataset version
* [get_custom_license](docs/sdks/datasets/README.md#get_custom_license) - Retrieve a specific dataset version's custom license
* [post_deaccession_dataset_by_version_id](docs/sdks/datasets/README.md#post_deaccession_dataset_by_version_id) - Remove access to a specific version of a dataset
* [get_dataset_version_files](docs/sdks/datasets/README.md#get_dataset_version_files) - Fetches files within a specific version of a dataset
* [get_dataset_files_count](docs/sdks/datasets/README.md#get_dataset_files_count) - Retrieve counts of various types of files in a specified dataset version
* [get_dataset_version_linkset](docs/sdks/datasets/README.md#get_dataset_version_linkset) - Retrieve linkset of a specific dataset version
* [get_dataset_version_metadata](docs/sdks/datasets/README.md#get_dataset_version_metadata) - Retrieve the metadata of a specific version of a dataset
* [get_dataset_version_metadata_1](docs/sdks/datasets/README.md#get_dataset_version_metadata_1) - Retrieve metadata of a specified version of a dataset
* [get_dataset_version_tool_param](docs/sdks/datasets/README.md#get_dataset_version_tool_param) - Retrieve tool parameters of a specific version of a dataset
* [get_dataset_archival_status](docs/sdks/datasets/README.md#get_dataset_archival_status) - Retrieve the archival status of a specific version of a dataset
* [update_dataset_archival_status](docs/sdks/datasets/README.md#update_dataset_archival_status) - Update the archival status of a specific version of a dataset
* [delete_dataset_archival_status](docs/sdks/datasets/README.md#delete_dataset_archival_status) - Remove the archival status of a specific version of a dataset
* [update_dataset_link](docs/sdks/datasets/README.md#update_dataset_link) - Updates the link between a dataset and a Dataverse alias

### [datatags](docs/sdks/datatags/README.md)

* [post_receive_tags](docs/sdks/datatags/README.md#post_receive_tags) - Create a new datatag and associate it with the specified unique cache ID

### [dataverses](docs/sdks/dataverses/README.md)

* [create_dataverse](docs/sdks/dataverses/README.md#create_dataverse) - Create a new Dataverse
* [get_dataverse](docs/sdks/dataverses/README.md#get_dataverse) - Retrieves a specified dataverse with the given identifier
* [create_dataverse_1](docs/sdks/dataverses/README.md#create_dataverse_1) - Creates a new dataverse with the given identifier
* [delete_dataverse](docs/sdks/dataverses/README.md#delete_dataverse) - Deletes a specified dataverse with the given identifier
* [publish_dataverse_by_id](docs/sdks/dataverses/README.md#publish_dataverse_by_id) - Publishes the identified Dataverse
* [get_dataverse_assignments](docs/sdks/dataverses/README.md#get_dataverse_assignments) - Retrieves assignments of specified Dataverse
* [post_dataverse_assignments](docs/sdks/dataverses/README.md#post_dataverse_assignments) - Assigns new user or role to specified Dataverse
* [delete_dataverse_assignment](docs/sdks/dataverses/README.md#delete_dataverse_assignment) - Delete a specific assignment from a specific dataverse
* [update_dataverse_attribute](docs/sdks/dataverses/README.md#update_dataverse_attribute) - Update a specific attribute of a Dataverse identified by the given identifier
* [get_dataverse_contents](docs/sdks/dataverses/README.md#get_dataverse_contents) - Retrieve contents of the specified Dataverse
* [get_dataset_schema](docs/sdks/dataverses/README.md#get_dataset_schema) - Retrieve the schema of a specific dataset in the dataverse identified by the given identifier
* [create_dataset_in_dataverse](docs/sdks/dataverses/README.md#create_dataset_in_dataverse) - Create a new dataset in the specified dataverse
* [import_dataset](docs/sdks/dataverses/README.md#import_dataset) - Imports a dataset into a given Dataverse identifier
* [import_ddi_to_dataset](docs/sdks/dataverses/README.md#import_ddi_to_dataset) - Imports DDI metadata to a dataset in the specified dataverse.
* [start_migration](docs/sdks/dataverses/README.md#start_migration) - Begins the migration process of datasets in a specific Dataverse identified by the provided identifier
* [update_default_contributor_role](docs/sdks/dataverses/README.md#update_default_contributor_role) - Update the default contributor role of a specific dataverse
* [get_facets](docs/sdks/dataverses/README.md#get_facets) - Retrieves the facets of the specified dataverse
* [post_facets](docs/sdks/dataverses/README.md#post_facets) - Updates the facets of the specified dataverse
* [get_dataverse_groups](docs/sdks/dataverses/README.md#get_dataverse_groups) - Retrieves groups associated with a specified dataverse
* [create_dataverse_group](docs/sdks/dataverses/README.md#create_dataverse_group) - Creates a new group in the specified dataverse
* [get_group_in_dataverse](docs/sdks/dataverses/README.md#get_group_in_dataverse) - Retrieve details of a specific group within the given Dataverse
* [update_group_in_dataverse](docs/sdks/dataverses/README.md#update_group_in_dataverse) - Update the details of a group within the specified Dataverse
* [delete_group_in_dataverse](docs/sdks/dataverses/README.md#delete_group_in_dataverse) - Delete a specific group from the specified Dataverse
* [assign_role](docs/sdks/dataverses/README.md#assign_role) - Assign a role to role assignees in a specified group within a dataverse
* [update_role_assignee](docs/sdks/dataverses/README.md#update_role_assignee) - Update a specific role assignee in a dataverse group
* [delete_role_assignee](docs/sdks/dataverses/README.md#delete_role_assignee) - Delete a specific role assignee from a dataverse group
* [get_guestbook_responses](docs/sdks/dataverses/README.md#get_guestbook_responses) - Retrieve all guestbook responses for a specific dataverse
* [get_dataverse_links](docs/sdks/dataverses/README.md#get_dataverse_links) - Retrieve all links associated with a specific dataverse identified by ID
* [get_metadatablock_facets](docs/sdks/dataverses/README.md#get_metadatablock_facets) - Retrieve metadatablock facets for a specific dataverse
* [post_metadatablock_facets](docs/sdks/dataverses/README.md#post_metadatablock_facets) - Add metadatablock facets to a specific dataverse
* [update_root_status](docs/sdks/dataverses/README.md#update_root_status) - Updates the root status of a Dataverse
* [get_metadatablock](docs/sdks/dataverses/README.md#get_metadatablock) - Retrieve the metadatablock of a Dataverse.
* [create_metadatablock](docs/sdks/dataverses/README.md#create_metadatablock) - Create a new metadatablock for a Dataverse.
* [get_metadatablock_1](docs/sdks/dataverses/README.md#get_metadatablock_1) - Retrieve metadata blocks for a specific dataverse identified by its unique identifier
* [post_metadatablock](docs/sdks/dataverses/README.md#post_metadatablock) - Add or update metadata block associated with the specified dataverse identifier
* [get_roles_by_identifier](docs/sdks/dataverses/README.md#get_roles_by_identifier) - Retrieve the roles for a given Dataverse identifier
* [create_role_by_identifier](docs/sdks/dataverses/README.md#create_role_by_identifier) - Create a new role for a given Dataverse identifier
* [get_storage_quota](docs/sdks/dataverses/README.md#get_storage_quota) - Retrieve storage quota of the dataverse identified by the given identifier
* [delete_storage_quota](docs/sdks/dataverses/README.md#delete_storage_quota) - Delete the storage quota configuration for the dataverse identified by the given identifier
* [set_storage_quota](docs/sdks/dataverses/README.md#set_storage_quota) - Sets the storage quota for a specific Dataverse
* [get_dataverse_storage_usage](docs/sdks/dataverses/README.md#get_dataverse_storage_usage) - Retrieve storage usage of a specific dataverse
* [get_dataverse_storage_size](docs/sdks/dataverses/README.md#get_dataverse_storage_size) - Retrieve the storage size of a specific Dataverse
* [validate_dataset_json](docs/sdks/dataverses/README.md#validate_dataset_json) - Validate the JSON of a dataset in a specific Dataverse
* [move_dataverse](docs/sdks/dataverses/README.md#move_dataverse) - Moves a Dataverse to a target Dataverse
* [link_dataverses](docs/sdks/dataverses/README.md#link_dataverses) - Links one Dataverse to another
* [delete_dataverse_link](docs/sdks/dataverses/README.md#delete_dataverse_link) - Delete a link between two dataverses

### [edit](docs/sdks/edit/README.md)

* [edit_file](docs/sdks/edit/README.md#edit_file) - Edits the content of a specified file

### [files](docs/sdks/files/README.md)

* [get_fixity_algorithm](docs/sdks/files/README.md#get_fixity_algorithm) - Retrieve the fixity algorithm of a file
* [get_file](docs/sdks/files/README.md#get_file) - Retrieve a specific file by ID.
* [delete_file](docs/sdks/files/README.md#delete_file) - Delete a specific file by ID.
* [get_file_data_tables](docs/sdks/files/README.md#get_file_data_tables) - Retrieve the data tables of a given file
* [get_download_count](docs/sdks/files/README.md#get_download_count) - Retrieve the download count of a file
* [get_file_draft](docs/sdks/files/README.md#get_file_draft) - Retrieve a file in draft mode by its ID
* [extract_ncml_by_id](docs/sdks/files/README.md#extract_ncml_by_id) - Extract Ncml information of a file based on the provided id
* [check_file_deletion_status](docs/sdks/files/README.md#check_file_deletion_status) - Check if specified file has been deleted
* [get_file_metadata](docs/sdks/files/README.md#get_file_metadata) - Retrieves metadata for a specific file
* [update_file_metadata](docs/sdks/files/README.md#update_file_metadata) - Updates metadata for a specific file
* [post_file_metadata_categories](docs/sdks/files/README.md#post_file_metadata_categories) - Adds new metadata categories for a specific file.
* [get_draft_meta_data](docs/sdks/files/README.md#get_draft_meta_data) - Retrieve the metadata of a draft file
* [post_tabular_tags](docs/sdks/files/README.md#post_tabular_tags) - Add tabular tags to a file metadata
* [get_file_metadata_tool_params](docs/sdks/files/README.md#get_file_metadata_tool_params) - Retrieves tool parameters for a specific file metadata ID
* [get_file_prov_freeform](docs/sdks/files/README.md#get_file_prov_freeform) - Retrieves the freeform provenance data for a specific file
* [post_file_prov_freeform](docs/sdks/files/README.md#post_file_prov_freeform) - Posts freeform provenance data for a specific file
* [get_file_prov_json](docs/sdks/files/README.md#get_file_prov_json) - Retrieving the PROV JSON of a specific file
* [post_file_prov_json](docs/sdks/files/README.md#post_file_prov_json) - Submit a new PROV JSON for a specific file
* [delete_file_prov_json](docs/sdks/files/README.md#delete_file_prov_json) - Delete the PROV JSON of a specific file
* [redetect_file](docs/sdks/files/README.md#redetect_file) - Invoke redetection process for the specified file
* [reingest_file](docs/sdks/files/README.md#reingest_file) - Reingest a file using its ID
* [replace_file](docs/sdks/files/README.md#replace_file) - Replace an existing file with a new version
* [restrict_file_access](docs/sdks/files/README.md#restrict_file_access) - Restrict access to a specific file
* [post_file_uningest](docs/sdks/files/README.md#post_file_uningest) - Uningest a file with the specified ID

### [harvest](docs/sdks/harvest/README.md)

* [get_harvest_clients](docs/sdks/harvest/README.md#get_harvest_clients) - Retrieve all harvest clients based on the provided key
* [get_harvest_client](docs/sdks/harvest/README.md#get_harvest_client) - Retrieves a harvest client details based on the provided unique nickname and key
* [update_harvest_client](docs/sdks/harvest/README.md#update_harvest_client) - Updates an existing harvest client's details using the provided unique nickname and key
* [create_harvest_client](docs/sdks/harvest/README.md#create_harvest_client) - Creates a new harvest client using the provided unique nickname and key
* [delete_harvest_client](docs/sdks/harvest/README.md#delete_harvest_client) - Deletes a harvest client based on the provided unique nickname
* [run_harvest_client](docs/sdks/harvest/README.md#run_harvest_client) - Initiate a run for a specified Harvest client
* [get_oai_sets](docs/sdks/harvest/README.md#get_oai_sets) - Retrieve the OAISets from the harvest server
* [add_oai_set](docs/sdks/harvest/README.md#add_oai_set) - Adds a new OAI set to the harvest server
* [get_oai_sets_1](docs/sdks/harvest/README.md#get_oai_sets_1) - Retrieve details of a specific OAI set
* [update_oai_sets](docs/sdks/harvest/README.md#update_oai_sets) - Update details of a specific OAI set
* [delete_oai_sets](docs/sdks/harvest/README.md#delete_oai_sets) - Remove a specific OAI set
* [get_harvest_datasets_by_spec_name](docs/sdks/harvest/README.md#get_harvest_datasets_by_spec_name) - Retrieve datasets related to a specified OAISet

### [inbox](docs/sdks/inbox/README.md)

* [post_inbox](docs/sdks/inbox/README.md#post_inbox) - Create a new inbox message

### [info](docs/sdks/info/README.md)

* [get_api_terms_of_use_info](docs/sdks/info/README.md#get_api_terms_of_use_info) - Retrieve the terms of use of the API
* [get_dataset_metrics_1](docs/sdks/info/README.md#get_dataset_metrics_1) - Retrieve dataset metrics based on the data location and parent alias
* [get_datasets_by_subject](docs/sdks/info/README.md#get_datasets_by_subject) - Retrieve datasets by subject according to specified data location and parent alias
* [get_monthly_subject_metrics](docs/sdks/info/README.md#get_monthly_subject_metrics) - Retrieve monthly metrics for datasets by subject
* [get_monthly_dataset_metrics](docs/sdks/info/README.md#get_monthly_dataset_metrics) - Retrieve monthly metrics of datasets based on data location and parent alias.
* [get_past_days_metrics](docs/sdks/info/README.md#get_past_days_metrics) - Retrieve metrics of datasets from past specified days
* [get_monthly_dataset_metrics_1](docs/sdks/info/README.md#get_monthly_dataset_metrics_1) - Retrieve dataset metrics for a specific month
* [get_metrics_dataverses](docs/sdks/info/README.md#get_metrics_dataverses) - Retrieves metrics of dataverses based on parent alias
* [get_metrics_by_category](docs/sdks/info/README.md#get_metrics_by_category) - Retrieves metrics of dataverses sorted by category
* [get_metrics_by_subject](docs/sdks/info/README.md#get_metrics_by_subject) - Retrieve metrics of dataverses by subject
* [get_monthly_dataverse_metrics](docs/sdks/info/README.md#get_monthly_dataverse_metrics) - Retrieve the monthly metrics of a specific dataverse
* [get_metrics_past_days](docs/sdks/info/README.md#get_metrics_past_days) - Retrieves the number of dataverses created over the past specified number of days
* [get_monthly_metrics_for_dataverses](docs/sdks/info/README.md#get_monthly_metrics_for_dataverses) - Retrieve the metrics for dataverses up to the specified month.
* [get_download_metrics](docs/sdks/info/README.md#get_download_metrics) - Retrieve download metrics based on a parent alias.
* [get_monthly_downloads](docs/sdks/info/README.md#get_monthly_downloads) - Retrieve monthly download metrics
* [get_past_days_downloads](docs/sdks/info/README.md#get_past_days_downloads) - Retrieve download metrics for the past specified number of days
* [get_download_metrics_to_month](docs/sdks/info/README.md#get_download_metrics_to_month) - Retrieve download metrics till a specific month
* [get_file_downloads_metrics](docs/sdks/info/README.md#get_file_downloads_metrics) - Retrieve File Downloads Metrics
* [get_monthly_file_downloads](docs/sdks/info/README.md#get_monthly_file_downloads) - Retrieve the monthly count of file downloads
* [get_file_downloads_to_month](docs/sdks/info/README.md#get_file_downloads_to_month) - Retrieve file download metrics for a specific month
* [get_file_info_metrics](docs/sdks/info/README.md#get_file_info_metrics) - Retrieve metrics information for files
* [get_metrics_by_file_type](docs/sdks/info/README.md#get_metrics_by_file_type) - Retrieve file metrics information categorized by file type
* [get_files_by_type_monthly](docs/sdks/info/README.md#get_files_by_type_monthly) - Retrieve monthly metrics for files by type
* [get_monthly_files_metrics](docs/sdks/info/README.md#get_monthly_files_metrics) - Retrieve monthly metrics for files
* [get_files_metrics](docs/sdks/info/README.md#get_files_metrics) - Retrieve metrics for files from the past specified number of days
* [get_monthly_files_info](docs/sdks/info/README.md#get_monthly_files_info) - Retrieve files metrics information for a specific month
* [get_metric_data](docs/sdks/info/README.md#get_metric_data) - Retrieve specific metric data by country and parentAlias
* [get_monthly_data_count_metrics](docs/sdks/info/README.md#get_monthly_data_count_metrics) - Retrieve the monthly data count metrics identified by the provided metric name
* [get_metrics_by_month](docs/sdks/info/README.md#get_metrics_by_month) - Retrieves data metrics for a specific month
* [get_metrics_tree](docs/sdks/info/README.md#get_metrics_tree) - Fetches the metrics tree based on the provided parent alias
* [get_monthly_metrics_by_alias](docs/sdks/info/README.md#get_monthly_metrics_by_alias) - Retrieve monthly metrics for a specific alias
* [get_unique_downloads](docs/sdks/info/README.md#get_unique_downloads) - Retrieve unique download metrics data for a particular alias
* [get_monthly_unique_downloads](docs/sdks/info/README.md#get_monthly_unique_downloads) - Retrieve monthly unique downloads metrics
* [get_monthly_unique_downloads_1](docs/sdks/info/README.md#get_monthly_unique_downloads_1) - Retrieve the number of unique downloads for a specified month
* [get_unique_file_downloads](docs/sdks/info/README.md#get_unique_file_downloads) - Retrieve the number of unique file downloads
* [get_monthly_unique_file_downloads](docs/sdks/info/README.md#get_monthly_unique_file_downloads) - Retrieve the count of unique file downloads per month
* [get_unique_file_downloads_1](docs/sdks/info/README.md#get_unique_file_downloads_1) - Fetches unique file downloads up to a specific month
* [get_open_api_info](docs/sdks/info/README.md#get_open_api_info) - Retrieve OpenAPI info in specified output format
* [get_server_info](docs/sdks/info/README.md#get_server_info) - Retrieve server information
* [get_dataset_publish_popup_custom_text](docs/sdks/info/README.md#get_dataset_publish_popup_custom_text) - Retrieve the custom text for dataset publish popup.
* [get_max_embargo_duration_in_months](docs/sdks/info/README.md#get_max_embargo_duration_in_months) - Retrieve the maximum duration of embargo in months from the settings
* [get_incomplete_metadata_settings](docs/sdks/info/README.md#get_incomplete_metadata_settings) - Retrieves the status of incomplete metadata settings
* [get_version_info](docs/sdks/info/README.md#get_version_info) - Retrieve the current version information
* [get_zip_download_limit](docs/sdks/info/README.md#get_zip_download_limit) - Retrieve the current zip file download limit

### [ingest](docs/sdks/ingest/README.md)

* [get_ingest_test_file](docs/sdks/ingest/README.md#get_ingest_test_file) - Retrieve details of a specific test file in the ingest process by filename and filetype

### [licenses](docs/sdks/licenses/README.md)

* [get_licenses](docs/sdks/licenses/README.md#get_licenses) - Retrieve all the licenses
* [add_license](docs/sdks/licenses/README.md#add_license) - Add a new license
* [get_default_license](docs/sdks/licenses/README.md#get_default_license) - Fetch the current default license
* [update_default_license](docs/sdks/licenses/README.md#update_default_license) - Update a default license by ID
* [get_license](docs/sdks/licenses/README.md#get_license) - Retrieve a specific license by its ID
* [delete_license](docs/sdks/licenses/README.md#delete_license) - Delete a specific license by its ID
* [update_license_active_state](docs/sdks/licenses/README.md#update_license_active_state) - Updates the activity state of a specific license
* [update_license_sort_order](docs/sdks/licenses/README.md#update_license_sort_order) - Update the sort order of a given license

### [logout](docs/sdks/logout/README.md)

* [logout_user](docs/sdks/logout/README.md#logout_user) - Log out the current user

### [mail](docs/sdks/mail/README.md)

* [get_mail_notifications](docs/sdks/mail/README.md#get_mail_notifications) - Retrieve a list of mail notifications

### [meta](docs/sdks/meta/README.md)

* [~~get_datafile_meta~~](docs/sdks/meta/README.md#get_datafile_meta) - Get metadata of a specific datafile by file id :warning: **Deprecated**
* [~~get_dataset_metadata_1~~](docs/sdks/meta/README.md#get_dataset_metadata_1) - Retrieves the metadata of a specific dataset by its ID :warning: **Deprecated**

### [metadatablocks](docs/sdks/metadatablocks/README.md)

* [get_metadatablocks](docs/sdks/metadatablocks/README.md#get_metadatablocks) - Retrieve metadata blocks available in the system
* [get_metadatablock_1_1](docs/sdks/metadatablocks/README.md#get_metadatablock_1_1) - Retrieve a specific Metadatablock by its identifier

### [mydata](docs/sdks/mydata/README.md)

* [my_data_retrieve](docs/sdks/mydata/README.md#my_data_retrieve) - Retrieve specific set of my data based on the provided filters

### [notifications](docs/sdks/notifications/README.md)

* [get_all_notifications](docs/sdks/notifications/README.md#get_all_notifications) - Retrieve all notifications
* [get_muted_emails](docs/sdks/notifications/README.md#get_muted_emails) - Retrieve a list of muted email notifications
* [update_muted_email_notification](docs/sdks/notifications/README.md#update_muted_email_notification) - Updates a muted email notification by type name
* [delete_muted_email_notification](docs/sdks/notifications/README.md#delete_muted_email_notification) - Deletes a muted email notification by type name
* [get_muted_notifications](docs/sdks/notifications/README.md#get_muted_notifications) - Retrieve all muted notifications
* [update_muted_notification](docs/sdks/notifications/README.md#update_muted_notification) - Update details of a specific muted notification
* [delete_muted_notification](docs/sdks/notifications/README.md#delete_muted_notification) - Delete a specific muted notification
* [delete_notification](docs/sdks/notifications/README.md#delete_notification) - Delete a notification by ID

### [pids](docs/sdks/pids/README.md)

* [get_persistent_id](docs/sdks/pids/README.md#get_persistent_id) - Retrieve a specific persistent identifier
* [get_unreserved_persistent_ids](docs/sdks/pids/README.md#get_unreserved_persistent_ids) - Retrieves unreserved persistent identifiers
* [delete_pid](docs/sdks/pids/README.md#delete_pid) - Delete a specific persistent identifier (PID)
* [reserve_pid](docs/sdks/pids/README.md#reserve_pid) - Reserve a specific PID

### [roles](docs/sdks/roles/README.md)

* [create_role](docs/sdks/roles/README.md#create_role) - Create a new role in the system
* [get_role](docs/sdks/roles/README.md#get_role) - Retrieve details of a specific role by id
* [delete_role](docs/sdks/roles/README.md#delete_role) - Delete a specific role by id

### [search](docs/sdks/search/README.md)

* [search_query](docs/sdks/search/README.md#search_query) - Executes a search query with various parameters and returns the matching records.

### [users](docs/sdks/users/README.md)

* [get_user_details](docs/sdks/users/README.md#get_user_details) - Retrieve the details of the logged-in user
* [get_user_token](docs/sdks/users/README.md#get_user_token) - Retrieves a user's authentication token
* [delete_user_token](docs/sdks/users/README.md#delete_user_token) - Deletes a user's authentication token
* [recreate_user_token](docs/sdks/users/README.md#recreate_user_token) - Recreates the authentication token for a given user
* [merge_users](docs/sdks/users/README.md#merge_users) - Merge the user with consumedIdentifier into the user with baseIdentifier
* [change_user_identifier](docs/sdks/users/README.md#change_user_identifier) - Change the identifier of a given user
* [remove_user_roles](docs/sdks/users/README.md#remove_user_roles) - Remove roles from a specific user
* [get_user_traces](docs/sdks/users/README.md#get_user_traces) - Retrieve a user's traces
* [get_user_trace_element](docs/sdks/users/README.md#get_user_trace_element) - Retrieve a specific trace element for a given user

### [workflows](docs/sdks/workflows/README.md)

* [start_workflow](docs/sdks/workflows/README.md#start_workflow) - Initiate a workflow using the given invocation id
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

### Example

```python
import pydataverse
from pydataverse.models import components, errors

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

res = None
try:
    res = s.dataverses.create_dataverse_1(identifier='<value>', dataverse_request=components.DataverseRequest(
    name='<value>',
    alias='<value>',
    affiliation='<value>',
    description='User-friendly stable benchmark',
    dataverse_type='<value>',
))

except errors.ErrorResponse as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.dataverse_response is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `{protocol}://{base_url}` | `protocol` (default is `https`), `base_url` (default is `demo.dataverse.org`) |

#### Example

```python
import pydataverse

s = pydataverse.PyDataverse(
    server_idx=0,
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_bundle(file_id='<value>')

if res.body is not None:
    # handle response
    pass

```

#### Variables

Some of the server options above contain variables. If you want to set the values of those variables, the following optional parameters are available when initializing the SDK client instance:
 * `protocol: models.ServerProtocol`
 * `base_url: str`

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import pydataverse

s = pydataverse.PyDataverse(
    server_url="{protocol}://{base_url}",
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.access.get_datafile_bundle(file_id='<value>')

if res.body is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import pydataverse
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = pydataverse.PyDataverse(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type           | Scheme         |
| -------------- | -------------- | -------------- |
| `api_key_auth` | apiKey         | API key        |

To authenticate with the API the `null` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
