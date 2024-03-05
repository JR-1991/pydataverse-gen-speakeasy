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

s = pydataverse.PyDataverse()


res = s.get_api_v1_access_datafile_bundle_file_id_(file_id='<value>', file_metadata_id=793125, gbrecs=False)

if res.body is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [PyDataverse SDK](docs/sdks/pydataverse/README.md)

* [get_api_v1_access_datafile_bundle_file_id_](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_bundle_file_id_)
* [get_api_v1_access_datafile_file_id_](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_file_id_)
* [get_api_v1_access_datafile_file_id_auxiliary](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_file_id_auxiliary)
* [get_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_)
* [post_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_](docs/sdks/pydataverse/README.md#post_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_)
* [delete_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_](docs/sdks/pydataverse/README.md#delete_api_v1_access_datafile_file_id_auxiliary_format_tag_format_version_)
* [get_api_v1_access_datafile_file_id_auxiliary_origin_](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_file_id_auxiliary_origin_)
* [get_api_v1_access_datafile_file_id_metadata](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_file_id_metadata)
* [get_api_v1_access_datafile_file_id_metadata_ddi](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_file_id_metadata_ddi)
* [put_api_v1_access_datafile_id_grant_access_identifier_](docs/sdks/pydataverse/README.md#put_api_v1_access_datafile_id_grant_access_identifier_)
* [get_api_v1_access_datafile_id_list_requests](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_id_list_requests)
* [put_api_v1_access_datafile_id_reject_access_identifier_](docs/sdks/pydataverse/README.md#put_api_v1_access_datafile_id_reject_access_identifier_)
* [put_api_v1_access_datafile_id_request_access](docs/sdks/pydataverse/README.md#put_api_v1_access_datafile_id_request_access)
* [delete_api_v1_access_datafile_id_revoke_access_identifier_](docs/sdks/pydataverse/README.md#delete_api_v1_access_datafile_id_revoke_access_identifier_)
* [get_api_v1_access_datafile_id_user_file_access_requested](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_id_user_file_access_requested)
* [get_api_v1_access_datafile_id_user_permissions](docs/sdks/pydataverse/README.md#get_api_v1_access_datafile_id_user_permissions)
* [post_api_v1_access_datafiles](docs/sdks/pydataverse/README.md#post_api_v1_access_datafiles)
* [get_api_v1_access_datafiles_file_ids_](docs/sdks/pydataverse/README.md#get_api_v1_access_datafiles_file_ids_)
* [get_api_v1_access_dataset_id_](docs/sdks/pydataverse/README.md#get_api_v1_access_dataset_id_)
* [get_api_v1_access_dataset_id_versions_version_id_](docs/sdks/pydataverse/README.md#get_api_v1_access_dataset_id_versions_version_id_)
* [get_api_v1_access_ds_card_image_version_id_](docs/sdks/pydataverse/README.md#get_api_v1_access_ds_card_image_version_id_)
* [get_api_v1_access_dv_card_image_dataverse_id_](docs/sdks/pydataverse/README.md#get_api_v1_access_dv_card_image_dataverse_id_)
* [get_api_v1_access_file_card_image_file_id_](docs/sdks/pydataverse/README.md#get_api_v1_access_file_card_image_file_id_)
* [put_api_v1_access_id_allow_access_request](docs/sdks/pydataverse/README.md#put_api_v1_access_id_allow_access_request)
* [post_api_v1_admin_archive_all_unarchived_dataset_versions](docs/sdks/pydataverse/README.md#post_api_v1_admin_archive_all_unarchived_dataset_versions)
* [get_api_v1_admin_assignee_idtf_](docs/sdks/pydataverse/README.md#get_api_v1_admin_assignee_idtf_)
* [get_api_v1_admin_assignments_assignees_ra_idtf_](docs/sdks/pydataverse/README.md#get_api_v1_admin_assignments_assignees_ra_idtf_)
* [~~get_api_v1_admin_authenticated_users~~](docs/sdks/pydataverse/README.md#get_api_v1_admin_authenticated_users) - :warning: **Deprecated**
* [post_api_v1_admin_authenticated_users](docs/sdks/pydataverse/README.md#post_api_v1_admin_authenticated_users)
* [put_api_v1_admin_authenticated_users_convert_builtin2oauth](docs/sdks/pydataverse/README.md#put_api_v1_admin_authenticated_users_convert_builtin2oauth)
* [put_api_v1_admin_authenticated_users_convert_builtin2shib](docs/sdks/pydataverse/README.md#put_api_v1_admin_authenticated_users_convert_builtin2shib)
* [delete_api_v1_admin_authenticated_users_id_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_authenticated_users_id_id_)
* [put_api_v1_admin_authenticated_users_id_id_convert_remote_to_built_in](docs/sdks/pydataverse/README.md#put_api_v1_admin_authenticated_users_id_id_convert_remote_to_built_in)
* [~~put_api_v1_admin_authenticated_users_id_id_convert_shib_to_built_in~~](docs/sdks/pydataverse/README.md#put_api_v1_admin_authenticated_users_id_id_convert_shib_to_built_in) - :warning: **Deprecated**
* [post_api_v1_admin_authenticated_users_id_id_deactivate](docs/sdks/pydataverse/README.md#post_api_v1_admin_authenticated_users_id_id_deactivate)
* [get_api_v1_admin_authenticated_users_identifier_](docs/sdks/pydataverse/README.md#get_api_v1_admin_authenticated_users_identifier_)
* [delete_api_v1_admin_authenticated_users_identifier_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_authenticated_users_identifier_)
* [post_api_v1_admin_authenticated_users_identifier_deactivate](docs/sdks/pydataverse/README.md#post_api_v1_admin_authenticated_users_identifier_deactivate)
* [get_api_v1_admin_authentication_provider_factories](docs/sdks/pydataverse/README.md#get_api_v1_admin_authentication_provider_factories)
* [get_api_v1_admin_authentication_providers](docs/sdks/pydataverse/README.md#get_api_v1_admin_authentication_providers)
* [post_api_v1_admin_authentication_providers](docs/sdks/pydataverse/README.md#post_api_v1_admin_authentication_providers)
* [get_api_v1_admin_authentication_providers_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_authentication_providers_id_)
* [delete_api_v1_admin_authentication_providers_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_authentication_providers_id_)
* [post_api_v1_admin_authentication_providers_id_enabled](docs/sdks/pydataverse/README.md#post_api_v1_admin_authentication_providers_id_enabled)
* [get_api_v1_admin_authentication_providers_id_enabled](docs/sdks/pydataverse/README.md#get_api_v1_admin_authentication_providers_id_enabled)
* [put_api_v1_admin_authentication_providers_id_enabled](docs/sdks/pydataverse/README.md#put_api_v1_admin_authentication_providers_id_enabled)
* [get_api_v1_admin_banner_message](docs/sdks/pydataverse/README.md#get_api_v1_admin_banner_message)
* [post_api_v1_admin_banner_message](docs/sdks/pydataverse/README.md#post_api_v1_admin_banner_message)
* [delete_api_v1_admin_banner_message_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_banner_message_id_)
* [put_api_v1_admin_banner_message_id_deactivate](docs/sdks/pydataverse/README.md#put_api_v1_admin_banner_message_id_deactivate)
* [get_api_v1_admin_batch_jobs](docs/sdks/pydataverse/README.md#get_api_v1_admin_batch_jobs)
* [get_api_v1_admin_batch_jobs_name_job_name_](docs/sdks/pydataverse/README.md#get_api_v1_admin_batch_jobs_name_job_name_)
* [get_api_v1_admin_batch_jobs_job_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_batch_jobs_job_id_)
* [delete_api_v1_admin_clear_metrics_cache](docs/sdks/pydataverse/README.md#delete_api_v1_admin_clear_metrics_cache)
* [delete_api_v1_admin_clear_metrics_cache_name_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_clear_metrics_cache_name_)
* [delete_api_v1_admin_clear_thumbnail_failure_flag](docs/sdks/pydataverse/README.md#delete_api_v1_admin_clear_thumbnail_failure_flag)
* [delete_api_v1_admin_clear_thumbnail_failure_flag_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_clear_thumbnail_failure_flag_id_)
* [post_api_v1_admin_compute_data_file_hash_value_file_id_algorithm_alg_](docs/sdks/pydataverse/README.md#post_api_v1_admin_compute_data_file_hash_value_file_id_algorithm_alg_)
* [get_api_v1_admin_confirm_email_user_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_confirm_email_user_id_)
* [post_api_v1_admin_confirm_email_user_id_](docs/sdks/pydataverse/README.md#post_api_v1_admin_confirm_email_user_id_)
* [post_api_v1_admin_convert_user_from_bcrypt_to_sha1](docs/sdks/pydataverse/README.md#post_api_v1_admin_convert_user_from_bcrypt_to_sha1)
* [get_api_v1_admin_datafiles_integrity_fixmissingoriginalsizes](docs/sdks/pydataverse/README.md#get_api_v1_admin_datafiles_integrity_fixmissingoriginalsizes)
* [get_api_v1_admin_datafiles_integrity_fixmissingoriginaltypes](docs/sdks/pydataverse/README.md#get_api_v1_admin_datafiles_integrity_fixmissingoriginaltypes)
* [get_api_v1_admin_datasetfield](docs/sdks/pydataverse/README.md#get_api_v1_admin_datasetfield)
* [get_api_v1_admin_datasetfield_controlled_vocabulary_subject](docs/sdks/pydataverse/README.md#get_api_v1_admin_datasetfield_controlled_vocabulary_subject)
* [post_api_v1_admin_datasetfield_load](docs/sdks/pydataverse/README.md#post_api_v1_admin_datasetfield_load)
* [get_api_v1_admin_datasetfield_load_na_controlled_vocabulary_value](docs/sdks/pydataverse/README.md#get_api_v1_admin_datasetfield_load_na_controlled_vocabulary_value)
* [post_api_v1_admin_datasetfield_loadpropertyfiles](docs/sdks/pydataverse/README.md#post_api_v1_admin_datasetfield_loadpropertyfiles)
* [get_api_v1_admin_datasetfield_name_](docs/sdks/pydataverse/README.md#get_api_v1_admin_datasetfield_name_)
* [post_api_v1_admin_datasets_integrity_dataset_version_id_fixmissingunf](docs/sdks/pydataverse/README.md#post_api_v1_admin_datasets_integrity_dataset_version_id_fixmissingunf)
* [get_api_v1_admin_datasets_thumbnail_metadata_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_datasets_thumbnail_metadata_id_)
* [get_api_v1_admin_dataverse_curation_label_sets](docs/sdks/pydataverse/README.md#get_api_v1_admin_dataverse_curation_label_sets)
* [get_api_v1_admin_dataverse_storage_drivers](docs/sdks/pydataverse/README.md#get_api_v1_admin_dataverse_storage_drivers)
* [get_api_v1_admin_dataverse_alias_add_role_assignments_to_children](docs/sdks/pydataverse/README.md#get_api_v1_admin_dataverse_alias_add_role_assignments_to_children)
* [get_api_v1_admin_dataverse_alias_curation_label_set](docs/sdks/pydataverse/README.md#get_api_v1_admin_dataverse_alias_curation_label_set)
* [put_api_v1_admin_dataverse_alias_curation_label_set](docs/sdks/pydataverse/README.md#put_api_v1_admin_dataverse_alias_curation_label_set)
* [delete_api_v1_admin_dataverse_alias_curation_label_set](docs/sdks/pydataverse/README.md#delete_api_v1_admin_dataverse_alias_curation_label_set)
* [get_api_v1_admin_dataverse_alias_storage_driver](docs/sdks/pydataverse/README.md#get_api_v1_admin_dataverse_alias_storage_driver)
* [put_api_v1_admin_dataverse_alias_storage_driver](docs/sdks/pydataverse/README.md#put_api_v1_admin_dataverse_alias_storage_driver)
* [delete_api_v1_admin_dataverse_alias_storage_driver](docs/sdks/pydataverse/README.md#delete_api_v1_admin_dataverse_alias_storage_driver)
* [get_api_v1_admin_download_tmp_file](docs/sdks/pydataverse/README.md#get_api_v1_admin_download_tmp_file)
* [get_api_v1_admin_external_tools](docs/sdks/pydataverse/README.md#get_api_v1_admin_external_tools)
* [post_api_v1_admin_external_tools](docs/sdks/pydataverse/README.md#post_api_v1_admin_external_tools)
* [get_api_v1_admin_external_tools_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_external_tools_id_)
* [delete_api_v1_admin_external_tools_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_external_tools_id_)
* [post_api_v1_admin_feedback](docs/sdks/pydataverse/README.md#post_api_v1_admin_feedback)
* [get_api_v1_admin_groups_domain](docs/sdks/pydataverse/README.md#get_api_v1_admin_groups_domain)
* [post_api_v1_admin_groups_domain](docs/sdks/pydataverse/README.md#post_api_v1_admin_groups_domain)
* [get_api_v1_admin_groups_domain_group_alias_](docs/sdks/pydataverse/README.md#get_api_v1_admin_groups_domain_group_alias_)
* [put_api_v1_admin_groups_domain_group_alias_](docs/sdks/pydataverse/README.md#put_api_v1_admin_groups_domain_group_alias_)
* [delete_api_v1_admin_groups_domain_group_alias_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_groups_domain_group_alias_)
* [get_api_v1_admin_groups_ip](docs/sdks/pydataverse/README.md#get_api_v1_admin_groups_ip)
* [post_api_v1_admin_groups_ip](docs/sdks/pydataverse/README.md#post_api_v1_admin_groups_ip)
* [get_api_v1_admin_groups_ip_group_idtf_](docs/sdks/pydataverse/README.md#get_api_v1_admin_groups_ip_group_idtf_)
* [delete_api_v1_admin_groups_ip_group_idtf_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_groups_ip_group_idtf_)
* [get_api_v1_admin_groups_shib](docs/sdks/pydataverse/README.md#get_api_v1_admin_groups_shib)
* [post_api_v1_admin_groups_shib](docs/sdks/pydataverse/README.md#post_api_v1_admin_groups_shib)
* [delete_api_v1_admin_groups_shib_primary_key_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_groups_shib_primary_key_)
* [get_api_v1_admin_index](docs/sdks/pydataverse/README.md#get_api_v1_admin_index)
* [get_api_v1_admin_index_clear](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_clear)
* [get_api_v1_admin_index_clear_orphans](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_clear_orphans)
* [get_api_v1_admin_index_continue](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_continue)
* [get_api_v1_admin_index_dataset](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_dataset)
* [delete_api_v1_admin_index_datasets_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_index_datasets_id_)
* [get_api_v1_admin_index_filemetadata_dataset_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_filemetadata_dataset_id_)
* [get_api_v1_admin_index_filesearch](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_filesearch)
* [get_api_v1_admin_index_mod](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_mod)
* [get_api_v1_admin_index_perms](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_perms)
* [get_api_v1_admin_index_perms_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_perms_id_)
* [get_api_v1_admin_index_perms_debug](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_perms_debug)
* [get_api_v1_admin_index_solr_schema](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_solr_schema)
* [get_api_v1_admin_index_status](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_status)
* [get_api_v1_admin_index_test](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_test)
* [delete_api_v1_admin_index_timestamps](docs/sdks/pydataverse/README.md#delete_api_v1_admin_index_timestamps)
* [delete_api_v1_admin_index_timestamps_dv_object_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_index_timestamps_dv_object_id_)
* [get_api_v1_admin_index_type_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_index_type_id_)
* [get_api_v1_admin_is_orcid](docs/sdks/pydataverse/README.md#get_api_v1_admin_is_orcid)
* [get_api_v1_admin_list_users](docs/sdks/pydataverse/README.md#get_api_v1_admin_list_users)
* [post_api_v1_admin_make_data_count_add_usage_metrics_from_sushi_report](docs/sdks/pydataverse/README.md#post_api_v1_admin_make_data_count_add_usage_metrics_from_sushi_report)
* [post_api_v1_admin_make_data_count_send_to_hub](docs/sdks/pydataverse/README.md#post_api_v1_admin_make_data_count_send_to_hub)
* [post_api_v1_admin_make_data_count_id_add_usage_metrics_from_sushi_report](docs/sdks/pydataverse/README.md#post_api_v1_admin_make_data_count_id_add_usage_metrics_from_sushi_report)
* [post_api_v1_admin_make_data_count_id_update_citations_for_dataset](docs/sdks/pydataverse/README.md#post_api_v1_admin_make_data_count_id_update_citations_for_dataset)
* [get_api_v1_admin_metadata_clear_export_timestamps](docs/sdks/pydataverse/README.md#get_api_v1_admin_metadata_clear_export_timestamps)
* [get_api_v1_admin_metadata_export_all](docs/sdks/pydataverse/README.md#get_api_v1_admin_metadata_export_all)
* [put_api_v1_admin_metadata_export_oai_specname_](docs/sdks/pydataverse/README.md#put_api_v1_admin_metadata_export_oai_specname_)
* [get_api_v1_admin_metadata_re_export_all](docs/sdks/pydataverse/README.md#get_api_v1_admin_metadata_re_export_all)
* [get_api_v1_admin_metadata_id_re_export_dataset](docs/sdks/pydataverse/README.md#get_api_v1_admin_metadata_id_re_export_dataset)
* [get_api_v1_admin_permissions_dvo_](docs/sdks/pydataverse/README.md#get_api_v1_admin_permissions_dvo_)
* [post_api_v1_admin_publish_dataverse_as_creator_id_](docs/sdks/pydataverse/README.md#post_api_v1_admin_publish_dataverse_as_creator_id_)
* [get_api_v1_admin_register_data_file_all](docs/sdks/pydataverse/README.md#get_api_v1_admin_register_data_file_all)
* [get_api_v1_admin_register_data_files_alias_](docs/sdks/pydataverse/README.md#get_api_v1_admin_register_data_files_alias_)
* [post_api_v1_admin_request_signed_url](docs/sdks/pydataverse/README.md#post_api_v1_admin_request_signed_url)
* [get_api_v1_admin_roles](docs/sdks/pydataverse/README.md#get_api_v1_admin_roles)
* [post_api_v1_admin_roles](docs/sdks/pydataverse/README.md#post_api_v1_admin_roles)
* [delete_api_v1_admin_roles_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_roles_id_)
* [get_api_v1_admin_savedsearches](docs/sdks/pydataverse/README.md#get_api_v1_admin_savedsearches)
* [post_api_v1_admin_savedsearches](docs/sdks/pydataverse/README.md#post_api_v1_admin_savedsearches)
* [get_api_v1_admin_savedsearches_list](docs/sdks/pydataverse/README.md#get_api_v1_admin_savedsearches_list)
* [put_api_v1_admin_savedsearches_makelinks_all](docs/sdks/pydataverse/README.md#put_api_v1_admin_savedsearches_makelinks_all)
* [put_api_v1_admin_savedsearches_makelinks_id_](docs/sdks/pydataverse/README.md#put_api_v1_admin_savedsearches_makelinks_id_)
* [get_api_v1_admin_savedsearches_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_savedsearches_id_)
* [delete_api_v1_admin_savedsearches_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_savedsearches_id_)
* [get_api_v1_admin_settings](docs/sdks/pydataverse/README.md#get_api_v1_admin_settings)
* [get_api_v1_admin_settings_name_](docs/sdks/pydataverse/README.md#get_api_v1_admin_settings_name_)
* [put_api_v1_admin_settings_name_](docs/sdks/pydataverse/README.md#put_api_v1_admin_settings_name_)
* [delete_api_v1_admin_settings_name_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_settings_name_)
* [put_api_v1_admin_settings_name_lang_lang_](docs/sdks/pydataverse/README.md#put_api_v1_admin_settings_name_lang_lang_)
* [delete_api_v1_admin_settings_name_lang_lang_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_settings_name_lang_lang_)
* [post_api_v1_admin_sitemap](docs/sdks/pydataverse/README.md#post_api_v1_admin_sitemap)
* [get_api_v1_admin_storage_sites](docs/sdks/pydataverse/README.md#get_api_v1_admin_storage_sites)
* [post_api_v1_admin_storage_sites](docs/sdks/pydataverse/README.md#post_api_v1_admin_storage_sites)
* [get_api_v1_admin_storage_sites_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_storage_sites_id_)
* [delete_api_v1_admin_storage_sites_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_storage_sites_id_)
* [put_api_v1_admin_storage_sites_id_primary_storage](docs/sdks/pydataverse/README.md#put_api_v1_admin_storage_sites_id_primary_storage)
* [post_api_v1_admin_submit_dataset_version_to_archive_id_version_](docs/sdks/pydataverse/README.md#post_api_v1_admin_submit_dataset_version_to_archive_id_version_)
* [post_api_v1_admin_superuser_identifier_](docs/sdks/pydataverse/README.md#post_api_v1_admin_superuser_identifier_)
* [delete_api_v1_admin_template_id_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_template_id_)
* [get_api_v1_admin_templates](docs/sdks/pydataverse/README.md#get_api_v1_admin_templates)
* [get_api_v1_admin_templates_alias_](docs/sdks/pydataverse/README.md#get_api_v1_admin_templates_alias_)
* [get_api_v1_admin_test_datasets_id_external_tools](docs/sdks/pydataverse/README.md#get_api_v1_admin_test_datasets_id_external_tools)
* [get_api_v1_admin_test_files_id_external_tool_tool_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_test_files_id_external_tool_tool_id_)
* [get_api_v1_admin_test_files_id_external_tools](docs/sdks/pydataverse/README.md#get_api_v1_admin_test_files_id_external_tools)
* [get_api_v1_admin_update_hash_values_alg_](docs/sdks/pydataverse/README.md#get_api_v1_admin_update_hash_values_alg_)
* [get_api_v1_admin_validate_dataset_files_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_validate_dataset_files_id_)
* [get_api_v1_admin_validate_dataset_id_](docs/sdks/pydataverse/README.md#get_api_v1_admin_validate_dataset_id_)
* [get_api_v1_admin_validate_datasets](docs/sdks/pydataverse/README.md#get_api_v1_admin_validate_datasets)
* [post_api_v1_admin_validate_data_file_hash_value_file_id_](docs/sdks/pydataverse/README.md#post_api_v1_admin_validate_data_file_hash_value_file_id_)
* [post_api_v1_admin_validate_password](docs/sdks/pydataverse/README.md#post_api_v1_admin_validate_password)
* [get_api_v1_admin_workflows](docs/sdks/pydataverse/README.md#get_api_v1_admin_workflows)
* [post_api_v1_admin_workflows](docs/sdks/pydataverse/README.md#post_api_v1_admin_workflows)
* [get_api_v1_admin_workflows_default](docs/sdks/pydataverse/README.md#get_api_v1_admin_workflows_default)
* [get_api_v1_admin_workflows_default_trigger_type_](docs/sdks/pydataverse/README.md#get_api_v1_admin_workflows_default_trigger_type_)
* [put_api_v1_admin_workflows_default_trigger_type_](docs/sdks/pydataverse/README.md#put_api_v1_admin_workflows_default_trigger_type_)
* [delete_api_v1_admin_workflows_default_trigger_type_](docs/sdks/pydataverse/README.md#delete_api_v1_admin_workflows_default_trigger_type_)
* [get_api_v1_admin_workflows_ip_whitelist](docs/sdks/pydataverse/README.md#get_api_v1_admin_workflows_ip_whitelist)
* [put_api_v1_admin_workflows_ip_whitelist](docs/sdks/pydataverse/README.md#put_api_v1_admin_workflows_ip_whitelist)
* [delete_api_v1_admin_workflows_ip_whitelist](docs/sdks/pydataverse/README.md#delete_api_v1_admin_workflows_ip_whitelist)
* [get_api_v1_admin_workflows_identifier_](docs/sdks/pydataverse/README.md#get_api_v1_admin_workflows_identifier_)
* [get_api_v1_admin_id_register_data_file](docs/sdks/pydataverse/README.md#get_api_v1_admin_id_register_data_file)
* [post_api_v1_admin_id_reregister_hdl_to_pid](docs/sdks/pydataverse/README.md#post_api_v1_admin_id_reregister_hdl_to_pid)
* [get_api_v1_application_wadl](docs/sdks/pydataverse/README.md#get_api_v1_application_wadl)
* [get_api_v1_application_wadl_path_](docs/sdks/pydataverse/README.md#get_api_v1_application_wadl_path_)
* [get_api_v1_batch_harvest](docs/sdks/pydataverse/README.md#get_api_v1_batch_harvest)
* [get_api_v1_batch_import](docs/sdks/pydataverse/README.md#get_api_v1_batch_import)
* [post_api_v1_batch_import](docs/sdks/pydataverse/README.md#post_api_v1_batch_import)
* [post_api_v1_batch_jobs_import_datasets_files_identifier_](docs/sdks/pydataverse/README.md#post_api_v1_batch_jobs_import_datasets_files_identifier_)
* [post_api_v1_builtin_users](docs/sdks/pydataverse/README.md#post_api_v1_builtin_users)
* [post_api_v1_builtin_users_password_key_](docs/sdks/pydataverse/README.md#post_api_v1_builtin_users_password_key_)
* [post_api_v1_builtin_users_password_key_send_email_notification_](docs/sdks/pydataverse/README.md#post_api_v1_builtin_users_password_key_send_email_notification_)
* [get_api_v1_builtin_users_username_api_token](docs/sdks/pydataverse/README.md#get_api_v1_builtin_users_username_api_token)
* [get_api_v1_datasets_export](docs/sdks/pydataverse/README.md#get_api_v1_datasets_export)
* [get_api_v1_datasets_list_curation_states](docs/sdks/pydataverse/README.md#get_api_v1_datasets_list_curation_states)
* [get_api_v1_datasets_locks](docs/sdks/pydataverse/README.md#get_api_v1_datasets_locks)
* [post_api_v1_datasets_modify_registration_all](docs/sdks/pydataverse/README.md#post_api_v1_datasets_modify_registration_all)
* [get_api_v1_datasets_modify_registration_pid_metadata_all](docs/sdks/pydataverse/README.md#get_api_v1_datasets_modify_registration_pid_metadata_all)
* [put_api_v1_datasets_mpupload](docs/sdks/pydataverse/README.md#put_api_v1_datasets_mpupload)
* [delete_api_v1_datasets_mpupload](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_mpupload)
* [get_api_v1_datasets_private_url_dataset_version_private_url_token_](docs/sdks/pydataverse/README.md#get_api_v1_datasets_private_url_dataset_version_private_url_token_)
* [get_api_v1_datasets_private_url_dataset_version_private_url_token_citation](docs/sdks/pydataverse/README.md#get_api_v1_datasets_private_url_dataset_version_private_url_token_citation)
* [get_api_v1_datasets_summary_field_names](docs/sdks/pydataverse/README.md#get_api_v1_datasets_summary_field_names)
* [delete_api_v1_datasets_dataset_id_delete_link_linked_dataverse_id_](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_dataset_id_delete_link_linked_dataverse_id_)
* [get_api_v1_datasets_identifier_allowed_curation_labels](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_allowed_curation_labels)
* [get_api_v1_datasets_identifier_assignments](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_assignments)
* [post_api_v1_datasets_identifier_assignments](docs/sdks/pydataverse/README.md#post_api_v1_datasets_identifier_assignments)
* [delete_api_v1_datasets_identifier_assignments_id_](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_identifier_assignments_id_)
* [get_api_v1_datasets_identifier_curation_label_set](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_curation_label_set)
* [put_api_v1_datasets_identifier_curation_label_set](docs/sdks/pydataverse/README.md#put_api_v1_datasets_identifier_curation_label_set)
* [delete_api_v1_datasets_identifier_curation_label_set](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_identifier_curation_label_set)
* [post_api_v1_datasets_identifier_data_capture_module_checksum_validation](docs/sdks/pydataverse/README.md#post_api_v1_datasets_identifier_data_capture_module_checksum_validation)
* [get_api_v1_datasets_identifier_data_capture_module_rsync](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_data_capture_module_rsync)
* [get_api_v1_datasets_identifier_guestbook_entry_at_request](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_guestbook_entry_at_request)
* [put_api_v1_datasets_identifier_guestbook_entry_at_request](docs/sdks/pydataverse/README.md#put_api_v1_datasets_identifier_guestbook_entry_at_request)
* [delete_api_v1_datasets_identifier_guestbook_entry_at_request](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_identifier_guestbook_entry_at_request)
* [post_api_v1_datasets_identifier_lock_type_](docs/sdks/pydataverse/README.md#post_api_v1_datasets_identifier_lock_type_)
* [get_api_v1_datasets_identifier_locks](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_locks)
* [delete_api_v1_datasets_identifier_locks](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_identifier_locks)
* [get_api_v1_datasets_identifier_storage_driver](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_storage_driver)
* [put_api_v1_datasets_identifier_storage_driver](docs/sdks/pydataverse/README.md#put_api_v1_datasets_identifier_storage_driver)
* [delete_api_v1_datasets_identifier_storage_driver](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_identifier_storage_driver)
* [get_api_v1_datasets_identifier_storagesize](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_storagesize)
* [get_api_v1_datasets_identifier_timestamps](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_timestamps)
* [get_api_v1_datasets_identifier_versions_version_id_downloadsize](docs/sdks/pydataverse/README.md#get_api_v1_datasets_identifier_versions_version_id_downloadsize)
* [get_api_v1_datasets_id_](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_)
* [delete_api_v1_datasets_id_](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_)
* [~~get_api_v1_datasets_id_actions_publish~~](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_actions_publish) - :warning: **Deprecated**
* [post_api_v1_datasets_id_actions_publish](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_actions_publish)
* [post_api_v1_datasets_id_actions_releasemigrated](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_actions_releasemigrated)
* [post_api_v1_datasets_id_add](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_add)
* [post_api_v1_datasets_id_add_files](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_add_files)
* [post_api_v1_datasets_id_add_globus_files](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_add_globus_files)
* [put_api_v1_datasets_id_citationdate](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_citationdate)
* [delete_api_v1_datasets_id_citationdate](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_citationdate)
* [get_api_v1_datasets_id_clean_storage](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_clean_storage)
* [get_api_v1_datasets_id_curation_status](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_curation_status)
* [put_api_v1_datasets_id_curation_status](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_curation_status)
* [delete_api_v1_datasets_id_curation_status](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_curation_status)
* [put_api_v1_datasets_id_delete_metadata](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_delete_metadata)
* [delete_api_v1_datasets_id_destroy](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_destroy)
* [get_api_v1_datasets_id_dirindex](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_dirindex)
* [put_api_v1_datasets_id_edit_metadata](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_edit_metadata)
* [post_api_v1_datasets_id_files_actions_set_embargo](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_files_actions_set_embargo)
* [post_api_v1_datasets_id_files_actions_unset_embargo](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_files_actions_unset_embargo)
* [get_api_v1_datasets_id_globus_download_parameters](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_globus_download_parameters)
* [get_api_v1_datasets_id_globus_upload_parameters](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_globus_upload_parameters)
* [get_api_v1_datasets_id_links](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_links)
* [get_api_v1_datasets_id_logo](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_logo)
* [get_api_v1_datasets_id_make_data_count_citations](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_make_data_count_citations)
* [get_api_v1_datasets_id_make_data_count_metric_](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_make_data_count_metric_)
* [get_api_v1_datasets_id_make_data_count_metric_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_make_data_count_metric_yyyymm_)
* [get_api_v1_datasets_id_metadata](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_metadata)
* [put_api_v1_datasets_id_metadata](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_metadata)
* [put_api_v1_datasets_id_metadata_delete](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_metadata_delete)
* [get_api_v1_datasets_id_modify_registration](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_modify_registration)
* [post_api_v1_datasets_id_modify_registration_metadata](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_modify_registration_metadata)
* [post_api_v1_datasets_id_monitor_globus_download](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_monitor_globus_download)
* [post_api_v1_datasets_id_move_target_dataverse_alias_](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_move_target_dataverse_alias_)
* [get_api_v1_datasets_id_private_url](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_private_url)
* [post_api_v1_datasets_id_private_url](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_private_url)
* [delete_api_v1_datasets_id_private_url](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_private_url)
* [post_api_v1_datasets_id_replace_files](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_replace_files)
* [post_api_v1_datasets_id_request_globus_download](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_request_globus_download)
* [post_api_v1_datasets_id_request_globus_upload_paths](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_request_globus_upload_paths)
* [post_api_v1_datasets_id_return_to_author](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_return_to_author)
* [post_api_v1_datasets_id_submit_for_review](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_submit_for_review)
* [get_api_v1_datasets_id_thumbnail](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_thumbnail)
* [post_api_v1_datasets_id_thumbnail](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_thumbnail)
* [delete_api_v1_datasets_id_thumbnail](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_thumbnail)
* [get_api_v1_datasets_id_thumbnail_candidates](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_thumbnail_candidates)
* [post_api_v1_datasets_id_thumbnail_data_file_id_](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_thumbnail_data_file_id_)
* [~~get_api_v1_datasets_id_uploadsid~~](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_uploadsid) - :warning: **Deprecated**
* [get_api_v1_datasets_id_uploadurls](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_uploadurls)
* [get_api_v1_datasets_id_user_permissions](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_user_permissions)
* [get_api_v1_datasets_id_versions](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions)
* [get_api_v1_datasets_id_versions_version_id_](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_)
* [put_api_v1_datasets_id_versions_version_id_](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_versions_version_id_)
* [delete_api_v1_datasets_id_versions_version_id_](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_versions_version_id_)
* [get_api_v1_datasets_id_versions_version_id_can_download_at_least_one_file](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_can_download_at_least_one_file)
* [get_api_v1_datasets_id_versions_version_id_citation](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_citation)
* [get_api_v1_datasets_id_versions_version_id_customlicense](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_customlicense)
* [post_api_v1_datasets_id_versions_version_id_deaccession](docs/sdks/pydataverse/README.md#post_api_v1_datasets_id_versions_version_id_deaccession)
* [get_api_v1_datasets_id_versions_version_id_files](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_files)
* [get_api_v1_datasets_id_versions_version_id_files_counts](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_files_counts)
* [get_api_v1_datasets_id_versions_version_id_linkset](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_linkset)
* [get_api_v1_datasets_id_versions_version_id_metadata](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_id_metadata)
* [get_api_v1_datasets_id_versions_version_number_metadata_block_](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_number_metadata_block_)
* [get_api_v1_datasets_id_versions_version_toolparams_tid_](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_versions_version_toolparams_tid_)
* [get_api_v1_datasets_id_version_archival_status](docs/sdks/pydataverse/README.md#get_api_v1_datasets_id_version_archival_status)
* [put_api_v1_datasets_id_version_archival_status](docs/sdks/pydataverse/README.md#put_api_v1_datasets_id_version_archival_status)
* [delete_api_v1_datasets_id_version_archival_status](docs/sdks/pydataverse/README.md#delete_api_v1_datasets_id_version_archival_status)
* [put_api_v1_datasets_linked_dataset_id_link_linking_dataverse_alias_](docs/sdks/pydataverse/README.md#put_api_v1_datasets_linked_dataset_id_link_linking_dataverse_alias_)
* [post_api_v1_datatags_receive_tags_unique_cache_id_](docs/sdks/pydataverse/README.md#post_api_v1_datatags_receive_tags_unique_cache_id_)
* [post_api_v1_dataverses](docs/sdks/pydataverse/README.md#post_api_v1_dataverses)
* [get_api_v1_dataverses_identifier_](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_)
* [post_api_v1_dataverses_identifier_](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_)
* [delete_api_v1_dataverses_identifier_](docs/sdks/pydataverse/README.md#delete_api_v1_dataverses_identifier_)
* [post_api_v1_dataverses_identifier_actions_publish](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_actions_publish)
* [get_api_v1_dataverses_identifier_assignments](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_assignments)
* [post_api_v1_dataverses_identifier_assignments](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_assignments)
* [delete_api_v1_dataverses_identifier_assignments_id_](docs/sdks/pydataverse/README.md#delete_api_v1_dataverses_identifier_assignments_id_)
* [put_api_v1_dataverses_identifier_attribute_attribute_](docs/sdks/pydataverse/README.md#put_api_v1_dataverses_identifier_attribute_attribute_)
* [get_api_v1_dataverses_identifier_contents](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_contents)
* [get_api_v1_dataverses_identifier_dataset_schema](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_dataset_schema)
* [post_api_v1_dataverses_identifier_datasets](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_datasets)
* [post_api_v1_dataverses_identifier_datasets_import](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_datasets_import)
* [post_api_v1_dataverses_identifier_datasets_importddi](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_datasets_importddi)
* [post_api_v1_dataverses_identifier_datasets_startmigration](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_datasets_startmigration)
* [put_api_v1_dataverses_identifier_default_contributor_role_role_alias_](docs/sdks/pydataverse/README.md#put_api_v1_dataverses_identifier_default_contributor_role_role_alias_)
* [get_api_v1_dataverses_identifier_facets](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_facets)
* [post_api_v1_dataverses_identifier_facets](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_facets)
* [get_api_v1_dataverses_identifier_groups](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_groups)
* [post_api_v1_dataverses_identifier_groups](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_groups)
* [get_api_v1_dataverses_identifier_groups_alias_in_owner_](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_groups_alias_in_owner_)
* [put_api_v1_dataverses_identifier_groups_alias_in_owner_](docs/sdks/pydataverse/README.md#put_api_v1_dataverses_identifier_groups_alias_in_owner_)
* [delete_api_v1_dataverses_identifier_groups_alias_in_owner_](docs/sdks/pydataverse/README.md#delete_api_v1_dataverses_identifier_groups_alias_in_owner_)
* [post_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees)
* [put_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_](docs/sdks/pydataverse/README.md#put_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_)
* [delete_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_](docs/sdks/pydataverse/README.md#delete_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_)
* [get_api_v1_dataverses_identifier_guestbook_responses](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_guestbook_responses)
* [get_api_v1_dataverses_identifier_links](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_links)
* [get_api_v1_dataverses_identifier_metadatablockfacets](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_metadatablockfacets)
* [post_api_v1_dataverses_identifier_metadatablockfacets](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_metadatablockfacets)
* [post_api_v1_dataverses_identifier_metadatablockfacets_is_root](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_metadatablockfacets_is_root)
* [get_api_v1_dataverses_identifier_metadatablocks](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_metadatablocks)
* [post_api_v1_dataverses_identifier_metadatablocks](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_metadatablocks)
* [get_api_v1_dataverses_identifier_metadatablocks_is_root](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_metadatablocks_is_root)
* [post_api_v1_dataverses_identifier_metadatablocks_is_root](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_metadatablocks_is_root)
* [get_api_v1_dataverses_identifier_roles](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_roles)
* [post_api_v1_dataverses_identifier_roles](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_roles)
* [get_api_v1_dataverses_identifier_storage_quota](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_storage_quota)
* [delete_api_v1_dataverses_identifier_storage_quota](docs/sdks/pydataverse/README.md#delete_api_v1_dataverses_identifier_storage_quota)
* [post_api_v1_dataverses_identifier_storage_quota_bytes_allocated_](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_storage_quota_bytes_allocated_)
* [get_api_v1_dataverses_identifier_storage_use](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_storage_use)
* [get_api_v1_dataverses_identifier_storagesize](docs/sdks/pydataverse/README.md#get_api_v1_dataverses_identifier_storagesize)
* [post_api_v1_dataverses_identifier_validate_dataset_json](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_identifier_validate_dataset_json)
* [post_api_v1_dataverses_id_move_target_dataverse_alias_](docs/sdks/pydataverse/README.md#post_api_v1_dataverses_id_move_target_dataverse_alias_)
* [put_api_v1_dataverses_linked_dataverse_alias_link_linking_dataverse_alias_](docs/sdks/pydataverse/README.md#put_api_v1_dataverses_linked_dataverse_alias_link_linking_dataverse_alias_)
* [delete_api_v1_dataverses_linking_dataverse_id_delete_link_linked_dataverse_id_](docs/sdks/pydataverse/README.md#delete_api_v1_dataverses_linking_dataverse_id_delete_link_linked_dataverse_id_)
* [put_api_v1_edit_file_id_](docs/sdks/pydataverse/README.md#put_api_v1_edit_file_id_)
* [get_api_v1_files_fixity_algorithm](docs/sdks/pydataverse/README.md#get_api_v1_files_fixity_algorithm)
* [get_api_v1_files_id_](docs/sdks/pydataverse/README.md#get_api_v1_files_id_)
* [delete_api_v1_files_id_](docs/sdks/pydataverse/README.md#delete_api_v1_files_id_)
* [get_api_v1_files_id_data_tables](docs/sdks/pydataverse/README.md#get_api_v1_files_id_data_tables)
* [get_api_v1_files_id_download_count](docs/sdks/pydataverse/README.md#get_api_v1_files_id_download_count)
* [get_api_v1_files_id_draft](docs/sdks/pydataverse/README.md#get_api_v1_files_id_draft)
* [post_api_v1_files_id_extract_ncml](docs/sdks/pydataverse/README.md#post_api_v1_files_id_extract_ncml)
* [get_api_v1_files_id_has_been_deleted](docs/sdks/pydataverse/README.md#get_api_v1_files_id_has_been_deleted)
* [get_api_v1_files_id_metadata](docs/sdks/pydataverse/README.md#get_api_v1_files_id_metadata)
* [post_api_v1_files_id_metadata](docs/sdks/pydataverse/README.md#post_api_v1_files_id_metadata)
* [post_api_v1_files_id_metadata_categories](docs/sdks/pydataverse/README.md#post_api_v1_files_id_metadata_categories)
* [get_api_v1_files_id_metadata_draft](docs/sdks/pydataverse/README.md#get_api_v1_files_id_metadata_draft)
* [post_api_v1_files_id_metadata_tabular_tags](docs/sdks/pydataverse/README.md#post_api_v1_files_id_metadata_tabular_tags)
* [get_api_v1_files_id_metadata_fmid_toolparams_tid_](docs/sdks/pydataverse/README.md#get_api_v1_files_id_metadata_fmid_toolparams_tid_)
* [get_api_v1_files_id_prov_freeform](docs/sdks/pydataverse/README.md#get_api_v1_files_id_prov_freeform)
* [post_api_v1_files_id_prov_freeform](docs/sdks/pydataverse/README.md#post_api_v1_files_id_prov_freeform)
* [get_api_v1_files_id_prov_json](docs/sdks/pydataverse/README.md#get_api_v1_files_id_prov_json)
* [post_api_v1_files_id_prov_json](docs/sdks/pydataverse/README.md#post_api_v1_files_id_prov_json)
* [delete_api_v1_files_id_prov_json](docs/sdks/pydataverse/README.md#delete_api_v1_files_id_prov_json)
* [post_api_v1_files_id_redetect](docs/sdks/pydataverse/README.md#post_api_v1_files_id_redetect)
* [post_api_v1_files_id_reingest](docs/sdks/pydataverse/README.md#post_api_v1_files_id_reingest)
* [post_api_v1_files_id_replace](docs/sdks/pydataverse/README.md#post_api_v1_files_id_replace)
* [put_api_v1_files_id_restrict](docs/sdks/pydataverse/README.md#put_api_v1_files_id_restrict)
* [post_api_v1_files_id_uningest](docs/sdks/pydataverse/README.md#post_api_v1_files_id_uningest)
* [get_api_v1_harvest_clients](docs/sdks/pydataverse/README.md#get_api_v1_harvest_clients)
* [get_api_v1_harvest_clients_nick_name_](docs/sdks/pydataverse/README.md#get_api_v1_harvest_clients_nick_name_)
* [put_api_v1_harvest_clients_nick_name_](docs/sdks/pydataverse/README.md#put_api_v1_harvest_clients_nick_name_)
* [post_api_v1_harvest_clients_nick_name_](docs/sdks/pydataverse/README.md#post_api_v1_harvest_clients_nick_name_)
* [delete_api_v1_harvest_clients_nick_name_](docs/sdks/pydataverse/README.md#delete_api_v1_harvest_clients_nick_name_)
* [post_api_v1_harvest_clients_nick_name_run](docs/sdks/pydataverse/README.md#post_api_v1_harvest_clients_nick_name_run)
* [get_api_v1_harvest_server_oaisets](docs/sdks/pydataverse/README.md#get_api_v1_harvest_server_oaisets)
* [post_api_v1_harvest_server_oaisets_add](docs/sdks/pydataverse/README.md#post_api_v1_harvest_server_oaisets_add)
* [get_api_v1_harvest_server_oaisets_specname_](docs/sdks/pydataverse/README.md#get_api_v1_harvest_server_oaisets_specname_)
* [put_api_v1_harvest_server_oaisets_specname_](docs/sdks/pydataverse/README.md#put_api_v1_harvest_server_oaisets_specname_)
* [delete_api_v1_harvest_server_oaisets_specname_](docs/sdks/pydataverse/README.md#delete_api_v1_harvest_server_oaisets_specname_)
* [get_api_v1_harvest_server_oaisets_specname_datasets](docs/sdks/pydataverse/README.md#get_api_v1_harvest_server_oaisets_specname_datasets)
* [post_api_v1_inbox](docs/sdks/pydataverse/README.md#post_api_v1_inbox)
* [get_api_v1_info_api_terms_of_use](docs/sdks/pydataverse/README.md#get_api_v1_info_api_terms_of_use)
* [get_api_v1_info_metrics_datasets](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_datasets)
* [get_api_v1_info_metrics_datasets_by_subject](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_datasets_by_subject)
* [get_api_v1_info_metrics_datasets_by_subject_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_datasets_by_subject_to_month_yyyymm_)
* [get_api_v1_info_metrics_datasets_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_datasets_monthly)
* [get_api_v1_info_metrics_datasets_past_days_days_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_datasets_past_days_days_)
* [get_api_v1_info_metrics_datasets_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_datasets_to_month_yyyymm_)
* [get_api_v1_info_metrics_dataverses](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_dataverses)
* [get_api_v1_info_metrics_dataverses_by_category](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_dataverses_by_category)
* [get_api_v1_info_metrics_dataverses_by_subject](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_dataverses_by_subject)
* [get_api_v1_info_metrics_dataverses_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_dataverses_monthly)
* [get_api_v1_info_metrics_dataverses_past_days_days_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_dataverses_past_days_days_)
* [get_api_v1_info_metrics_dataverses_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_dataverses_to_month_yyyymm_)
* [get_api_v1_info_metrics_downloads](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_downloads)
* [get_api_v1_info_metrics_downloads_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_downloads_monthly)
* [get_api_v1_info_metrics_downloads_past_days_days_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_downloads_past_days_days_)
* [get_api_v1_info_metrics_downloads_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_downloads_to_month_yyyymm_)
* [get_api_v1_info_metrics_filedownloads](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_filedownloads)
* [get_api_v1_info_metrics_filedownloads_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_filedownloads_monthly)
* [get_api_v1_info_metrics_filedownloads_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_filedownloads_to_month_yyyymm_)
* [get_api_v1_info_metrics_files](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_files)
* [get_api_v1_info_metrics_files_by_type](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_files_by_type)
* [get_api_v1_info_metrics_files_by_type_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_files_by_type_monthly)
* [get_api_v1_info_metrics_files_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_files_monthly)
* [get_api_v1_info_metrics_files_past_days_days_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_files_past_days_days_)
* [get_api_v1_info_metrics_files_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_files_to_month_yyyymm_)
* [get_api_v1_info_metrics_make_data_count_metric_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_make_data_count_metric_)
* [get_api_v1_info_metrics_make_data_count_metric_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_make_data_count_metric_monthly)
* [get_api_v1_info_metrics_make_data_count_metric_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_make_data_count_metric_to_month_yyyymm_)
* [get_api_v1_info_metrics_tree](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_tree)
* [get_api_v1_info_metrics_tree_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_tree_to_month_yyyymm_)
* [get_api_v1_info_metrics_uniquedownloads](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_uniquedownloads)
* [get_api_v1_info_metrics_uniquedownloads_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_uniquedownloads_monthly)
* [get_api_v1_info_metrics_uniquedownloads_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_uniquedownloads_to_month_yyyymm_)
* [get_api_v1_info_metrics_uniquefiledownloads](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_uniquefiledownloads)
* [get_api_v1_info_metrics_uniquefiledownloads_monthly](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_uniquefiledownloads_monthly)
* [get_api_v1_info_metrics_uniquefiledownloads_to_month_yyyymm_](docs/sdks/pydataverse/README.md#get_api_v1_info_metrics_uniquefiledownloads_to_month_yyyymm_)
* [get_api_v1_info_openapi_format_](docs/sdks/pydataverse/README.md#get_api_v1_info_openapi_format_)
* [get_api_v1_info_server](docs/sdks/pydataverse/README.md#get_api_v1_info_server)
* [get_api_v1_info_settings_dataset_publish_popup_custom_text](docs/sdks/pydataverse/README.md#get_api_v1_info_settings_dataset_publish_popup_custom_text)
* [get_api_v1_info_settings_max_embargo_duration_in_months](docs/sdks/pydataverse/README.md#get_api_v1_info_settings_max_embargo_duration_in_months)
* [get_api_v1_info_settings_incomplete_metadata_via_api](docs/sdks/pydataverse/README.md#get_api_v1_info_settings_incomplete_metadata_via_api)
* [get_api_v1_info_version](docs/sdks/pydataverse/README.md#get_api_v1_info_version)
* [get_api_v1_info_zip_download_limit](docs/sdks/pydataverse/README.md#get_api_v1_info_zip_download_limit)
* [get_api_v1_ingest_test_file](docs/sdks/pydataverse/README.md#get_api_v1_ingest_test_file)
* [get_api_v1_licenses](docs/sdks/pydataverse/README.md#get_api_v1_licenses)
* [post_api_v1_licenses](docs/sdks/pydataverse/README.md#post_api_v1_licenses)
* [get_api_v1_licenses_default](docs/sdks/pydataverse/README.md#get_api_v1_licenses_default)
* [put_api_v1_licenses_default_id_](docs/sdks/pydataverse/README.md#put_api_v1_licenses_default_id_)
* [get_api_v1_licenses_id_](docs/sdks/pydataverse/README.md#get_api_v1_licenses_id_)
* [delete_api_v1_licenses_id_](docs/sdks/pydataverse/README.md#delete_api_v1_licenses_id_)
* [put_api_v1_licenses_id_active_active_state_](docs/sdks/pydataverse/README.md#put_api_v1_licenses_id_active_active_state_)
* [put_api_v1_licenses_id_sort_order_sort_order_](docs/sdks/pydataverse/README.md#put_api_v1_licenses_id_sort_order_sort_order_)
* [post_api_v1_logout](docs/sdks/pydataverse/README.md#post_api_v1_logout)
* [get_api_v1_mail_notifications](docs/sdks/pydataverse/README.md#get_api_v1_mail_notifications)
* [~~get_api_v1_meta_datafile_file_id_~~](docs/sdks/pydataverse/README.md#get_api_v1_meta_datafile_file_id_) - :warning: **Deprecated**
* [~~get_api_v1_meta_dataset_dataset_id_~~](docs/sdks/pydataverse/README.md#get_api_v1_meta_dataset_dataset_id_) - :warning: **Deprecated**
* [get_api_v1_metadatablocks](docs/sdks/pydataverse/README.md#get_api_v1_metadatablocks)
* [get_api_v1_metadatablocks_identifier_](docs/sdks/pydataverse/README.md#get_api_v1_metadatablocks_identifier_)
* [get_api_v1_mydata_retrieve](docs/sdks/pydataverse/README.md#get_api_v1_mydata_retrieve)
* [get_api_v1_notifications_all](docs/sdks/pydataverse/README.md#get_api_v1_notifications_all)
* [get_api_v1_notifications_muted_emails](docs/sdks/pydataverse/README.md#get_api_v1_notifications_muted_emails)
* [put_api_v1_notifications_muted_emails_type_name_](docs/sdks/pydataverse/README.md#put_api_v1_notifications_muted_emails_type_name_)
* [delete_api_v1_notifications_muted_emails_type_name_](docs/sdks/pydataverse/README.md#delete_api_v1_notifications_muted_emails_type_name_)
* [get_api_v1_notifications_muted_notifications](docs/sdks/pydataverse/README.md#get_api_v1_notifications_muted_notifications)
* [put_api_v1_notifications_muted_notifications_type_name_](docs/sdks/pydataverse/README.md#put_api_v1_notifications_muted_notifications_type_name_)
* [delete_api_v1_notifications_muted_notifications_type_name_](docs/sdks/pydataverse/README.md#delete_api_v1_notifications_muted_notifications_type_name_)
* [delete_api_v1_notifications_id_](docs/sdks/pydataverse/README.md#delete_api_v1_notifications_id_)
* [get_api_v1_pids](docs/sdks/pydataverse/README.md#get_api_v1_pids)
* [get_api_v1_pids_unreserved](docs/sdks/pydataverse/README.md#get_api_v1_pids_unreserved)
* [delete_api_v1_pids_id_delete](docs/sdks/pydataverse/README.md#delete_api_v1_pids_id_delete)
* [post_api_v1_pids_id_reserve](docs/sdks/pydataverse/README.md#post_api_v1_pids_id_reserve)
* [post_api_v1_roles](docs/sdks/pydataverse/README.md#post_api_v1_roles)
* [get_api_v1_roles_id_](docs/sdks/pydataverse/README.md#get_api_v1_roles_id_)
* [delete_api_v1_roles_id_](docs/sdks/pydataverse/README.md#delete_api_v1_roles_id_)
* [get_api_v1_search](docs/sdks/pydataverse/README.md#get_api_v1_search)
* [get_api_v1_users_me](docs/sdks/pydataverse/README.md#get_api_v1_users_me)
* [get_api_v1_users_token](docs/sdks/pydataverse/README.md#get_api_v1_users_token)
* [delete_api_v1_users_token](docs/sdks/pydataverse/README.md#delete_api_v1_users_token)
* [post_api_v1_users_token_recreate](docs/sdks/pydataverse/README.md#post_api_v1_users_token_recreate)
* [post_api_v1_users_consumed_identifier_merge_into_user_base_identifier_](docs/sdks/pydataverse/README.md#post_api_v1_users_consumed_identifier_merge_into_user_base_identifier_)
* [post_api_v1_users_identifier_change_identifier_new_identifier_](docs/sdks/pydataverse/README.md#post_api_v1_users_identifier_change_identifier_new_identifier_)
* [post_api_v1_users_identifier_remove_roles](docs/sdks/pydataverse/README.md#post_api_v1_users_identifier_remove_roles)
* [get_api_v1_users_identifier_traces](docs/sdks/pydataverse/README.md#get_api_v1_users_identifier_traces)
* [get_api_v1_users_identifier_traces_element_](docs/sdks/pydataverse/README.md#get_api_v1_users_identifier_traces_element_)
* [post_api_v1_workflows_invocation_id_](docs/sdks/pydataverse/README.md#post_api_v1_workflows_invocation_id_)
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import pydataverse
from pydataverse.models import errors

s = pydataverse.PyDataverse()


res = None
try:
    res = s.get_api_v1_access_datafile_bundle_file_id_(file_id='<value>', file_metadata_id=793125, gbrecs=False)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.body is not None:
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
| 0 | `http://localhost:8000` | None |

#### Example

```python
import pydataverse

s = pydataverse.PyDataverse(
    server_idx=0,
)


res = s.get_api_v1_access_datafile_bundle_file_id_(file_id='<value>', file_metadata_id=793125, gbrecs=False)

if res.body is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import pydataverse

s = pydataverse.PyDataverse(
    server_url="http://localhost:8000",
)


res = s.get_api_v1_access_datafile_bundle_file_id_(file_id='<value>', file_metadata_id=793125, gbrecs=False)

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
s = pydataverse.PyDataverse(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

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
