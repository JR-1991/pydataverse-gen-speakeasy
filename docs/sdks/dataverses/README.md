# Dataverses
(*dataverses*)

### Available Operations

* [post_api_v1_dataverses](#post_api_v1_dataverses)
* [get_api_v1_dataverses_identifier_](#get_api_v1_dataverses_identifier_)
* [post_api_v1_dataverses_identifier_](#post_api_v1_dataverses_identifier_)
* [delete_api_v1_dataverses_identifier_](#delete_api_v1_dataverses_identifier_)
* [post_api_v1_dataverses_identifier_actions_publish](#post_api_v1_dataverses_identifier_actions_publish)
* [get_api_v1_dataverses_identifier_assignments](#get_api_v1_dataverses_identifier_assignments)
* [post_api_v1_dataverses_identifier_assignments](#post_api_v1_dataverses_identifier_assignments)
* [delete_api_v1_dataverses_identifier_assignments_id_](#delete_api_v1_dataverses_identifier_assignments_id_)
* [put_api_v1_dataverses_identifier_attribute_attribute_](#put_api_v1_dataverses_identifier_attribute_attribute_)
* [get_api_v1_dataverses_identifier_contents](#get_api_v1_dataverses_identifier_contents)
* [get_api_v1_dataverses_identifier_dataset_schema](#get_api_v1_dataverses_identifier_dataset_schema)
* [post_api_v1_dataverses_identifier_datasets](#post_api_v1_dataverses_identifier_datasets)
* [post_api_v1_dataverses_identifier_datasets_import](#post_api_v1_dataverses_identifier_datasets_import)
* [post_api_v1_dataverses_identifier_datasets_importddi](#post_api_v1_dataverses_identifier_datasets_importddi)
* [post_api_v1_dataverses_identifier_datasets_startmigration](#post_api_v1_dataverses_identifier_datasets_startmigration)
* [put_api_v1_dataverses_identifier_default_contributor_role_role_alias_](#put_api_v1_dataverses_identifier_default_contributor_role_role_alias_)
* [get_api_v1_dataverses_identifier_facets](#get_api_v1_dataverses_identifier_facets)
* [post_api_v1_dataverses_identifier_facets](#post_api_v1_dataverses_identifier_facets)
* [get_api_v1_dataverses_identifier_groups](#get_api_v1_dataverses_identifier_groups)
* [post_api_v1_dataverses_identifier_groups](#post_api_v1_dataverses_identifier_groups)
* [get_api_v1_dataverses_identifier_groups_alias_in_owner_](#get_api_v1_dataverses_identifier_groups_alias_in_owner_)
* [put_api_v1_dataverses_identifier_groups_alias_in_owner_](#put_api_v1_dataverses_identifier_groups_alias_in_owner_)
* [delete_api_v1_dataverses_identifier_groups_alias_in_owner_](#delete_api_v1_dataverses_identifier_groups_alias_in_owner_)
* [post_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees](#post_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees)
* [put_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_](#put_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_)
* [delete_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_](#delete_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_)
* [get_api_v1_dataverses_identifier_guestbook_responses](#get_api_v1_dataverses_identifier_guestbook_responses)
* [get_api_v1_dataverses_identifier_links](#get_api_v1_dataverses_identifier_links)
* [get_api_v1_dataverses_identifier_metadatablockfacets](#get_api_v1_dataverses_identifier_metadatablockfacets)
* [post_api_v1_dataverses_identifier_metadatablockfacets](#post_api_v1_dataverses_identifier_metadatablockfacets)
* [post_api_v1_dataverses_identifier_metadatablockfacets_is_root](#post_api_v1_dataverses_identifier_metadatablockfacets_is_root)
* [get_api_v1_dataverses_identifier_metadatablocks](#get_api_v1_dataverses_identifier_metadatablocks)
* [post_api_v1_dataverses_identifier_metadatablocks](#post_api_v1_dataverses_identifier_metadatablocks)
* [get_api_v1_dataverses_identifier_metadatablocks_is_root](#get_api_v1_dataverses_identifier_metadatablocks_is_root)
* [post_api_v1_dataverses_identifier_metadatablocks_is_root](#post_api_v1_dataverses_identifier_metadatablocks_is_root)
* [get_api_v1_dataverses_identifier_roles](#get_api_v1_dataverses_identifier_roles)
* [post_api_v1_dataverses_identifier_roles](#post_api_v1_dataverses_identifier_roles)
* [get_api_v1_dataverses_identifier_storage_quota](#get_api_v1_dataverses_identifier_storage_quota)
* [delete_api_v1_dataverses_identifier_storage_quota](#delete_api_v1_dataverses_identifier_storage_quota)
* [post_api_v1_dataverses_identifier_storage_quota_bytes_allocated_](#post_api_v1_dataverses_identifier_storage_quota_bytes_allocated_)
* [get_api_v1_dataverses_identifier_storage_use](#get_api_v1_dataverses_identifier_storage_use)
* [get_api_v1_dataverses_identifier_storagesize](#get_api_v1_dataverses_identifier_storagesize)
* [post_api_v1_dataverses_identifier_validate_dataset_json](#post_api_v1_dataverses_identifier_validate_dataset_json)
* [post_api_v1_dataverses_id_move_target_dataverse_alias_](#post_api_v1_dataverses_id_move_target_dataverse_alias_)
* [put_api_v1_dataverses_linked_dataverse_alias_link_linking_dataverse_alias_](#put_api_v1_dataverses_linked_dataverse_alias_link_linking_dataverse_alias_)
* [delete_api_v1_dataverses_linking_dataverse_id_delete_link_linked_dataverse_id_](#delete_api_v1_dataverses_linking_dataverse_id_delete_link_linked_dataverse_id_)

## post_api_v1_dataverses

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostAPIV1DataversesResponse](../../models/operations/postapiv1dataversesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierResponse](../../models/operations/getapiv1dataversesidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierResponse](../../models/operations/postapiv1dataversesidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_dataverses_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.delete_api_v1_dataverses_identifier_(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1DataversesIdentifierResponse](../../models/operations/deleteapiv1dataversesidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_actions_publish

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_actions_publish(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierActionsPublishResponse](../../models/operations/postapiv1dataversesidentifieractionspublishresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_assignments

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_assignments(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierAssignmentsResponse](../../models/operations/getapiv1dataversesidentifierassignmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_assignments

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_assignments(identifier='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierAssignmentsResponse](../../models/operations/postapiv1dataversesidentifierassignmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_dataverses_identifier_assignments_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.delete_api_v1_dataverses_identifier_assignments_id_(id=735432, identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1DataversesIdentifierAssignmentsIDResponse](../../models/operations/deleteapiv1dataversesidentifierassignmentsidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_dataverses_identifier_attribute_attribute_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.put_api_v1_dataverses_identifier_attribute_attribute_(attribute='<value>', identifier='<value>', value='<value>')

if res.status_code == 200:
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

**[operations.PutAPIV1DataversesIdentifierAttributeAttributeResponse](../../models/operations/putapiv1dataversesidentifierattributeattributeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_contents

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_contents(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierContentsResponse](../../models/operations/getapiv1dataversesidentifiercontentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_dataset_schema

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_dataset_schema(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierDatasetSchemaResponse](../../models/operations/getapiv1dataversesidentifierdatasetschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_datasets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_datasets(identifier='<value>', do_not_validate='<value>', request_body='<value>')

if res.status_code == 200:
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

**[operations.PostAPIV1DataversesIdentifierDatasetsResponse](../../models/operations/postapiv1dataversesidentifierdatasetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_datasets_import

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_datasets_import(identifier='<value>', pid='<value>', release='<value>')

if res.status_code == 200:
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

**[operations.PostAPIV1DataversesIdentifierDatasetsImportResponse](../../models/operations/postapiv1dataversesidentifierdatasetsimportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_datasets_importddi

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_datasets_importddi(identifier='<value>', pid='<value>', release='<value>')

if res.status_code == 200:
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

**[operations.PostAPIV1DataversesIdentifierDatasetsImportddiResponse](../../models/operations/postapiv1dataversesidentifierdatasetsimportddiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_datasets_startmigration

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_datasets_startmigration(identifier='<value>', request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierDatasetsStartmigrationResponse](../../models/operations/postapiv1dataversesidentifierdatasetsstartmigrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_dataverses_identifier_default_contributor_role_role_alias_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.put_api_v1_dataverses_identifier_default_contributor_role_role_alias_(identifier='<value>', role_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `role_alias`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1DataversesIdentifierDefaultContributorRoleRoleAliasResponse](../../models/operations/putapiv1dataversesidentifierdefaultcontributorrolerolealiasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_facets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_facets(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierFacetsResponse](../../models/operations/getapiv1dataversesidentifierfacetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_facets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_facets(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierFacetsResponse](../../models/operations/postapiv1dataversesidentifierfacetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_groups

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_groups(identifier='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierGroupsResponse](../../models/operations/getapiv1dataversesidentifiergroupsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_groups

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_groups(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierGroupsResponse](../../models/operations/postapiv1dataversesidentifiergroupsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_groups_alias_in_owner_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_groups_alias_in_owner_(alias_in_owner='<value>', identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias_in_owner`   | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierGroupsAliasInOwnerResponse](../../models/operations/getapiv1dataversesidentifiergroupsaliasinownerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_dataverses_identifier_groups_alias_in_owner_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.put_api_v1_dataverses_identifier_groups_alias_in_owner_(alias_in_owner='<value>', identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias_in_owner`   | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1DataversesIdentifierGroupsAliasInOwnerResponse](../../models/operations/putapiv1dataversesidentifiergroupsaliasinownerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_dataverses_identifier_groups_alias_in_owner_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.delete_api_v1_dataverses_identifier_groups_alias_in_owner_(alias_in_owner='<value>', identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `alias_in_owner`   | *str*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1DataversesIdentifierGroupsAliasInOwnerResponse](../../models/operations/deleteapiv1dataversesidentifiergroupsaliasinownerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees(alias_in_owner='<value>', identifier='<value>', request_body=[
    '<value>',
])

if res.status_code == 200:
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

**[operations.PostAPIV1DataversesIdentifierGroupsAliasInOwnerRoleAssigneesResponse](../../models/operations/postapiv1dataversesidentifiergroupsaliasinownerroleassigneesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.put_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_(alias_in_owner='<value>', identifier='<value>', role_assignee_identifier='<value>')

if res.status_code == 200:
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

**[operations.PutAPIV1DataversesIdentifierGroupsAliasInOwnerRoleAssigneesRoleAssigneeIdentifierResponse](../../models/operations/putapiv1dataversesidentifiergroupsaliasinownerroleassigneesroleassigneeidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.delete_api_v1_dataverses_identifier_groups_alias_in_owner_role_assignees_role_assignee_identifier_(alias_in_owner='<value>', identifier='<value>', role_assignee_identifier='<value>')

if res.status_code == 200:
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

**[operations.DeleteAPIV1DataversesIdentifierGroupsAliasInOwnerRoleAssigneesRoleAssigneeIdentifierResponse](../../models/operations/deleteapiv1dataversesidentifiergroupsaliasinownerroleassigneesroleassigneeidentifierresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_guestbook_responses

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_guestbook_responses(identifier='<value>', guestbook_id=164918)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `guestbook_id`     | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierGuestbookResponsesResponse](../../models/operations/getapiv1dataversesidentifierguestbookresponsesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_links

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_links(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierLinksResponse](../../models/operations/getapiv1dataversesidentifierlinksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_metadatablockfacets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_metadatablockfacets(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierMetadatablockfacetsResponse](../../models/operations/getapiv1dataversesidentifiermetadatablockfacetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_metadatablockfacets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_metadatablockfacets(identifier='<value>', request_body=[
    '<value>',
])

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | List[*str*]        | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierMetadatablockfacetsResponse](../../models/operations/postapiv1dataversesidentifiermetadatablockfacetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_metadatablockfacets_is_root

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_metadatablockfacets_is_root(identifier='<value>', request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierMetadatablockfacetsIsRootResponse](../../models/operations/postapiv1dataversesidentifiermetadatablockfacetsisrootresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_metadatablocks

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_metadatablocks(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierMetadatablocksResponse](../../models/operations/getapiv1dataversesidentifiermetadatablocksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_metadatablocks

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_metadatablocks(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierMetadatablocksResponse](../../models/operations/postapiv1dataversesidentifiermetadatablocksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_metadatablocks_is_root

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_metadatablocks_is_root(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierMetadatablocksIsRootResponse](../../models/operations/getapiv1dataversesidentifiermetadatablocksisrootresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_metadatablocks_is_root

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_metadatablocks_is_root(identifier='<value>', request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierMetadatablocksIsRootResponse](../../models/operations/postapiv1dataversesidentifiermetadatablocksisrootresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_roles

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_roles(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierRolesResponse](../../models/operations/getapiv1dataversesidentifierrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_roles

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_roles(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierRolesResponse](../../models/operations/postapiv1dataversesidentifierrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_storage_quota

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_storage_quota(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierStorageQuotaResponse](../../models/operations/getapiv1dataversesidentifierstoragequotaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_dataverses_identifier_storage_quota

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.delete_api_v1_dataverses_identifier_storage_quota(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1DataversesIdentifierStorageQuotaResponse](../../models/operations/deleteapiv1dataversesidentifierstoragequotaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_storage_quota_bytes_allocated_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_storage_quota_bytes_allocated_(bytes_allocated=163160, identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `bytes_allocated`  | *int*              | :heavy_check_mark: | N/A                |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierStorageQuotaBytesAllocatedResponse](../../models/operations/postapiv1dataversesidentifierstoragequotabytesallocatedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_storage_use

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_storage_use(identifier='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierStorageUseResponse](../../models/operations/getapiv1dataversesidentifierstorageuseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_dataverses_identifier_storagesize

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.get_api_v1_dataverses_identifier_storagesize(identifier='<value>', include_cached=False)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `include_cached`   | *Optional[bool]*   | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1DataversesIdentifierStoragesizeResponse](../../models/operations/getapiv1dataversesidentifierstoragesizeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_identifier_validate_dataset_json

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_identifier_validate_dataset_json(identifier='<value>', request_body='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `identifier`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1DataversesIdentifierValidateDatasetJSONResponse](../../models/operations/postapiv1dataversesidentifiervalidatedatasetjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_dataverses_id_move_target_dataverse_alias_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.post_api_v1_dataverses_id_move_target_dataverse_alias_(id='<value>', target_dataverse_alias='<value>', force_move=False)

if res.status_code == 200:
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

**[operations.PostAPIV1DataversesIDMoveTargetDataverseAliasResponse](../../models/operations/postapiv1dataversesidmovetargetdataversealiasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_dataverses_linked_dataverse_alias_link_linking_dataverse_alias_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.put_api_v1_dataverses_linked_dataverse_alias_link_linking_dataverse_alias_(linked_dataverse_alias='<value>', linking_dataverse_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `linked_dataverse_alias`  | *str*                     | :heavy_check_mark:        | N/A                       |
| `linking_dataverse_alias` | *str*                     | :heavy_check_mark:        | N/A                       |


### Response

**[operations.PutAPIV1DataversesLinkedDataverseAliasLinkLinkingDataverseAliasResponse](../../models/operations/putapiv1dataverseslinkeddataversealiaslinklinkingdataversealiasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_dataverses_linking_dataverse_id_delete_link_linked_dataverse_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.dataverses.delete_api_v1_dataverses_linking_dataverse_id_delete_link_linked_dataverse_id_(linked_dataverse_id='<value>', linking_dataverse_id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `linked_dataverse_id`  | *str*                  | :heavy_check_mark:     | N/A                    |
| `linking_dataverse_id` | *str*                  | :heavy_check_mark:     | N/A                    |


### Response

**[operations.DeleteAPIV1DataversesLinkingDataverseIDDeleteLinkLinkedDataverseIDResponse](../../models/operations/deleteapiv1dataverseslinkingdataverseiddeletelinklinkeddataverseidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
