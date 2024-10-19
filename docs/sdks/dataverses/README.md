# Dataverses
(*dataverses*)

## Overview

### Available Operations

* [create_dataverse](#create_dataverse) - Create a new Dataverse
* [get_dataverse](#get_dataverse) - Retrieves a specified dataverse with the given identifier
* [create_dataverse_1](#create_dataverse_1) - Creates a new dataverse with the given identifier
* [delete_dataverse](#delete_dataverse) - Deletes a specified dataverse with the given identifier
* [publish_dataverse_by_id](#publish_dataverse_by_id) - Publishes the identified Dataverse
* [get_dataverse_assignments](#get_dataverse_assignments) - Retrieves assignments of specified Dataverse
* [post_dataverse_assignments](#post_dataverse_assignments) - Assigns new user or role to specified Dataverse
* [delete_dataverse_assignment](#delete_dataverse_assignment) - Delete a specific assignment from a specific dataverse
* [update_dataverse_attribute](#update_dataverse_attribute) - Update a specific attribute of a Dataverse identified by the given identifier
* [get_dataverse_contents](#get_dataverse_contents) - Retrieve contents of the specified Dataverse
* [get_dataset_schema](#get_dataset_schema) - Retrieve the schema of a specific dataset in the dataverse identified by the given identifier
* [create_dataset_in_dataverse](#create_dataset_in_dataverse) - Create a new dataset in the specified dataverse
* [import_dataset](#import_dataset) - Imports a dataset into a given Dataverse identifier
* [import_ddi_to_dataset](#import_ddi_to_dataset) - Imports DDI metadata to a dataset in the specified dataverse.
* [start_migration](#start_migration) - Begins the migration process of datasets in a specific Dataverse identified by the provided identifier
* [update_default_contributor_role](#update_default_contributor_role) - Update the default contributor role of a specific dataverse
* [get_facets](#get_facets) - Retrieves the facets of the specified dataverse
* [post_facets](#post_facets) - Updates the facets of the specified dataverse
* [get_dataverse_groups](#get_dataverse_groups) - Retrieves groups associated with a specified dataverse
* [create_dataverse_group](#create_dataverse_group) - Creates a new group in the specified dataverse
* [get_group_in_dataverse](#get_group_in_dataverse) - Retrieve details of a specific group within the given Dataverse
* [update_group_in_dataverse](#update_group_in_dataverse) - Update the details of a group within the specified Dataverse
* [delete_group_in_dataverse](#delete_group_in_dataverse) - Delete a specific group from the specified Dataverse
* [assign_role](#assign_role) - Assign a role to role assignees in a specified group within a dataverse
* [update_role_assignee](#update_role_assignee) - Update a specific role assignee in a dataverse group
* [delete_role_assignee](#delete_role_assignee) - Delete a specific role assignee from a dataverse group
* [get_guestbook_responses](#get_guestbook_responses) - Retrieve all guestbook responses for a specific dataverse
* [get_dataverse_links](#get_dataverse_links) - Retrieve all links associated with a specific dataverse identified by ID
* [get_metadatablock_facets](#get_metadatablock_facets) - Retrieve metadatablock facets for a specific dataverse
* [post_metadatablock_facets](#post_metadatablock_facets) - Add metadatablock facets to a specific dataverse
* [update_root_status](#update_root_status) - Updates the root status of a Dataverse
* [get_metadatablock](#get_metadatablock) - Retrieve the metadatablock of a Dataverse.
* [create_metadatablock](#create_metadatablock) - Create a new metadatablock for a Dataverse.
* [get_metadatablock_1](#get_metadatablock_1) - Retrieve metadata blocks for a specific dataverse identified by its unique identifier
* [post_metadatablock](#post_metadatablock) - Add or update metadata block associated with the specified dataverse identifier
* [get_roles_by_identifier](#get_roles_by_identifier) - Retrieve the roles for a given Dataverse identifier
* [create_role_by_identifier](#create_role_by_identifier) - Create a new role for a given Dataverse identifier
* [get_storage_quota](#get_storage_quota) - Retrieve storage quota of the dataverse identified by the given identifier
* [delete_storage_quota](#delete_storage_quota) - Delete the storage quota configuration for the dataverse identified by the given identifier
* [set_storage_quota](#set_storage_quota) - Sets the storage quota for a specific Dataverse
* [get_dataverse_storage_usage](#get_dataverse_storage_usage) - Retrieve storage usage of a specific dataverse
* [get_dataverse_storage_size](#get_dataverse_storage_size) - Retrieve the storage size of a specific Dataverse
* [validate_dataset_json](#validate_dataset_json) - Validate the JSON of a dataset in a specific Dataverse
* [move_dataverse](#move_dataverse) - Moves a Dataverse to a target Dataverse
* [link_dataverses](#link_dataverses) - Links one Dataverse to another
* [delete_dataverse_link](#delete_dataverse_link) - Delete a link between two dataverses

## create_dataverse

Create a new Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.create_dataverse()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.CreateDataverseResponse](../../models/operations/createdataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataverse

Retrieves a specified dataverse with the given identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataverse(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDataverseResponse](../../models/operations/getdataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dataverse_1

Creates a new dataverse with the given identifier

### Example Usage

```python
import pydataverse
from pydataverse.models import components

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.create_dataverse_1(dataverse_request=components.DataverseRequest(
    name='<value>',
    alias='<value>',
    affiliation='<value>',
    description='User-friendly stable benchmark',
    dataverse_type='<value>',
), identifier='<value>')

if res.dataverse_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `identifier`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `dataverse_request`                                                        | [components.DataverseRequest](../../models/components/dataverserequest.md) | :heavy_check_mark:                                                         | N/A                                                                        |

### Response

**[operations.CreateDataverse1Response](../../models/operations/createdataverse1response.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |

## delete_dataverse

Deletes a specified dataverse with the given identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.delete_dataverse(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteDataverseResponse](../../models/operations/deletedataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## publish_dataverse_by_id

Publishes the identified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.publish_dataverse_by_id(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.PublishDataverseByIDResponse](../../models/operations/publishdataversebyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataverse_assignments

Retrieves assignments of specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataverse_assignments(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDataverseAssignmentsResponse](../../models/operations/getdataverseassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_dataverse_assignments

Assigns new user or role to specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.post_dataverse_assignments(identifier='<value>')

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

**[operations.PostDataverseAssignmentsResponse](../../models/operations/postdataverseassignmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataverse_assignment

Delete a specific assignment from a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.delete_dataverse_assignment(id=540951, identifier='<value>')

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

**[operations.DeleteDataverseAssignmentResponse](../../models/operations/deletedataverseassignmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_dataverse_attribute

Update a specific attribute of a Dataverse identified by the given identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.update_dataverse_attribute(attribute='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `attribute`        | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `value`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.UpdateDataverseAttributeResponse](../../models/operations/updatedataverseattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataverse_contents

Retrieve contents of the specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataverse_contents(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDataverseContentsResponse](../../models/operations/getdataversecontentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataset_schema

Retrieve the schema of a specific dataset in the dataverse identified by the given identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataset_schema(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDatasetSchemaResponse](../../models/operations/getdatasetschemaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dataset_in_dataverse

Create a new dataset in the specified dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.create_dataset_in_dataverse(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `do_not_validate`  | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.CreateDatasetInDataverseResponse](../../models/operations/createdatasetindataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## import_dataset

Imports a dataset into a given Dataverse identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.import_dataset(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `pid`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `release`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.ImportDatasetResponse](../../models/operations/importdatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## import_ddi_to_dataset

Imports DDI metadata to a dataset in the specified dataverse.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.import_ddi_to_dataset(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `pid`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `release`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.ImportDdiToDatasetResponse](../../models/operations/importdditodatasetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## start_migration

Begins the migration process of datasets in a specific Dataverse identified by the provided identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.start_migration(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.StartMigrationResponse](../../models/operations/startmigrationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_default_contributor_role

Update the default contributor role of a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.update_default_contributor_role(identifier='<value>', role_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `role_alias`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateDefaultContributorRoleResponse](../../models/operations/updatedefaultcontributorroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_facets

Retrieves the facets of the specified dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_facets(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetFacetsResponse](../../models/operations/getfacetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_facets

Updates the facets of the specified dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.post_facets(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.PostFacetsResponse](../../models/operations/postfacetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataverse_groups

Retrieves groups associated with a specified dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataverse_groups(identifier='<value>')

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

**[operations.GetDataverseGroupsResponse](../../models/operations/getdataversegroupsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_dataverse_group

Creates a new group in the specified dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.create_dataverse_group(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.CreateDataverseGroupResponse](../../models/operations/createdataversegroupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_group_in_dataverse

Retrieve details of a specific group within the given Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_group_in_dataverse(alias_in_owner='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias_in_owner`   | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetGroupInDataverseResponse](../../models/operations/getgroupindataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_group_in_dataverse

Update the details of a group within the specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.update_group_in_dataverse(alias_in_owner='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias_in_owner`   | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateGroupInDataverseResponse](../../models/operations/updategroupindataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_group_in_dataverse

Delete a specific group from the specified Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.delete_group_in_dataverse(alias_in_owner='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias_in_owner`   | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteGroupInDataverseResponse](../../models/operations/deletegroupindataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## assign_role

Assign a role to role assignees in a specified group within a dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.assign_role(alias_in_owner='<value>', identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias_in_owner`   | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | List[*str*]        | :heavy_minus_sign: | N/A                |

### Response

**[operations.AssignRoleResponse](../../models/operations/assignroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_role_assignee

Update a specific role assignee in a dataverse group

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.update_role_assignee(alias_in_owner='<value>', identifier='<value>', role_assignee_identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                  | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `alias_in_owner`           | *str*                      | :heavy_check_mark:         | N/A                        |
| `identifier`               | *str*                      | :heavy_check_mark:         | N/A                        |
| `role_assignee_identifier` | *str*                      | :heavy_check_mark:         | N/A                        |

### Response

**[operations.UpdateRoleAssigneeResponse](../../models/operations/updateroleassigneeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_role_assignee

Delete a specific role assignee from a dataverse group

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.delete_role_assignee(alias_in_owner='<value>', identifier='<value>', role_assignee_identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                  | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `alias_in_owner`           | *str*                      | :heavy_check_mark:         | N/A                        |
| `identifier`               | *str*                      | :heavy_check_mark:         | N/A                        |
| `role_assignee_identifier` | *str*                      | :heavy_check_mark:         | N/A                        |

### Response

**[operations.DeleteRoleAssigneeResponse](../../models/operations/deleteroleassigneeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_guestbook_responses

Retrieve all guestbook responses for a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_guestbook_responses(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `guestbook_id`     | *Optional[int]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.GetGuestbookResponsesResponse](../../models/operations/getguestbookresponsesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataverse_links

Retrieve all links associated with a specific dataverse identified by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataverse_links(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDataverseLinksResponse](../../models/operations/getdataverselinksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_metadatablock_facets

Retrieve metadatablock facets for a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_metadatablock_facets(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetMetadatablockFacetsResponse](../../models/operations/getmetadatablockfacetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_metadatablock_facets

Add metadatablock facets to a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.post_metadatablock_facets(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | List[*str*]        | :heavy_minus_sign: | N/A                |

### Response

**[operations.PostMetadatablockFacetsResponse](../../models/operations/postmetadatablockfacetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_root_status

Updates the root status of a Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.update_root_status(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.UpdateRootStatusResponse](../../models/operations/updaterootstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_metadatablock

Retrieve the metadatablock of a Dataverse.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_metadatablock(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetMetadatablockResponse](../../models/operations/getmetadatablockresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_metadatablock

Create a new metadatablock for a Dataverse.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.create_metadatablock(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.CreateMetadatablockResponse](../../models/operations/createmetadatablockresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_metadatablock_1

Retrieve metadata blocks for a specific dataverse identified by its unique identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_metadatablock_1(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetMetadatablock1Response](../../models/operations/getmetadatablock1response.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## post_metadatablock

Add or update metadata block associated with the specified dataverse identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.post_metadatablock(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.PostMetadatablockResponse](../../models/operations/postmetadatablockresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_roles_by_identifier

Retrieve the roles for a given Dataverse identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_roles_by_identifier(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetRolesByIdentifierResponse](../../models/operations/getrolesbyidentifierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_role_by_identifier

Create a new role for a given Dataverse identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.create_role_by_identifier(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.CreateRoleByIdentifierResponse](../../models/operations/createrolebyidentifierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_storage_quota

Retrieve storage quota of the dataverse identified by the given identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_storage_quota(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetStorageQuotaResponse](../../models/operations/getstoragequotaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_storage_quota

Delete the storage quota configuration for the dataverse identified by the given identifier

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.delete_storage_quota(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteStorageQuotaResponse](../../models/operations/deletestoragequotaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set_storage_quota

Sets the storage quota for a specific Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.set_storage_quota(bytes_allocated=789024, identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `bytes_allocated`  | *int*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.SetStorageQuotaResponse](../../models/operations/setstoragequotaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataverse_storage_usage

Retrieve storage usage of a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataverse_storage_usage(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.GetDataverseStorageUsageResponse](../../models/operations/getdataversestorageusageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_dataverse_storage_size

Retrieve the storage size of a specific Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.get_dataverse_storage_size(identifier='<value>')

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

**[operations.GetDataverseStorageSizeResponse](../../models/operations/getdataversestoragesizeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## validate_dataset_json

Validate the JSON of a dataset in a specific Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.validate_dataset_json(identifier='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |

### Response

**[operations.ValidateDatasetJSONResponse](../../models/operations/validatedatasetjsonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## move_dataverse

Moves a Dataverse to a target Dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.move_dataverse(id='<id>', target_dataverse_alias='<value>')

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

**[operations.MoveDataverseResponse](../../models/operations/movedataverseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## link_dataverses

Links one Dataverse to another

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.link_dataverses(linked_dataverse_alias='<value>', linking_dataverse_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `linked_dataverse_alias`  | *str*                     | :heavy_check_mark:        | N/A                       |
| `linking_dataverse_alias` | *str*                     | :heavy_check_mark:        | N/A                       |

### Response

**[operations.LinkDataversesResponse](../../models/operations/linkdataversesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_dataverse_link

Delete a link between two dataverses

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.dataverses.delete_dataverse_link(linked_dataverse_id='<value>', linking_dataverse_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `linked_dataverse_id`  | *str*                  | :heavy_check_mark:     | N/A                    |
| `linking_dataverse_id` | *str*                  | :heavy_check_mark:     | N/A                    |

### Response

**[operations.DeleteDataverseLinkResponse](../../models/operations/deletedataverselinkresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |