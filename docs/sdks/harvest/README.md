# Harvest
(*harvest*)

### Available Operations

* [get_api_v1_harvest_clients](#get_api_v1_harvest_clients)
* [get_api_v1_harvest_clients_nick_name_](#get_api_v1_harvest_clients_nick_name_)
* [put_api_v1_harvest_clients_nick_name_](#put_api_v1_harvest_clients_nick_name_)
* [post_api_v1_harvest_clients_nick_name_](#post_api_v1_harvest_clients_nick_name_)
* [delete_api_v1_harvest_clients_nick_name_](#delete_api_v1_harvest_clients_nick_name_)
* [post_api_v1_harvest_clients_nick_name_run](#post_api_v1_harvest_clients_nick_name_run)
* [get_api_v1_harvest_server_oaisets](#get_api_v1_harvest_server_oaisets)
* [post_api_v1_harvest_server_oaisets_add](#post_api_v1_harvest_server_oaisets_add)
* [get_api_v1_harvest_server_oaisets_specname_](#get_api_v1_harvest_server_oaisets_specname_)
* [put_api_v1_harvest_server_oaisets_specname_](#put_api_v1_harvest_server_oaisets_specname_)
* [delete_api_v1_harvest_server_oaisets_specname_](#delete_api_v1_harvest_server_oaisets_specname_)
* [get_api_v1_harvest_server_oaisets_specname_datasets](#get_api_v1_harvest_server_oaisets_specname_datasets)

## get_api_v1_harvest_clients

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.get_api_v1_harvest_clients(key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1HarvestClientsResponse](../../models/operations/getapiv1harvestclientsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_harvest_clients_nick_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.get_api_v1_harvest_clients_nick_name_(nick_name='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `nick_name`        | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1HarvestClientsNickNameResponse](../../models/operations/getapiv1harvestclientsnicknameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_harvest_clients_nick_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.put_api_v1_harvest_clients_nick_name_(nick_name='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `nick_name`        | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PutAPIV1HarvestClientsNickNameResponse](../../models/operations/putapiv1harvestclientsnicknameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_harvest_clients_nick_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.post_api_v1_harvest_clients_nick_name_(nick_name='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `nick_name`        | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1HarvestClientsNickNameResponse](../../models/operations/postapiv1harvestclientsnicknameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_harvest_clients_nick_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.delete_api_v1_harvest_clients_nick_name_(nick_name='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `nick_name`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1HarvestClientsNickNameResponse](../../models/operations/deleteapiv1harvestclientsnicknameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_harvest_clients_nick_name_run

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.post_api_v1_harvest_clients_nick_name_run(nick_name='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `nick_name`        | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1HarvestClientsNickNameRunResponse](../../models/operations/postapiv1harvestclientsnicknamerunresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_harvest_server_oaisets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.get_api_v1_harvest_server_oaisets(key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1HarvestServerOaisetsResponse](../../models/operations/getapiv1harvestserveroaisetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_v1_harvest_server_oaisets_add

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.post_api_v1_harvest_server_oaisets_add(key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PostAPIV1HarvestServerOaisetsAddResponse](../../models/operations/postapiv1harvestserveroaisetsaddresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_harvest_server_oaisets_specname_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.get_api_v1_harvest_server_oaisets_specname_(specname='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `specname`         | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1HarvestServerOaisetsSpecnameResponse](../../models/operations/getapiv1harvestserveroaisetsspecnameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_harvest_server_oaisets_specname_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.put_api_v1_harvest_server_oaisets_specname_(specname='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `specname`         | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.PutAPIV1HarvestServerOaisetsSpecnameResponse](../../models/operations/putapiv1harvestserveroaisetsspecnameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_harvest_server_oaisets_specname_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.delete_api_v1_harvest_server_oaisets_specname_(specname='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `specname`         | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.DeleteAPIV1HarvestServerOaisetsSpecnameResponse](../../models/operations/deleteapiv1harvestserveroaisetsspecnameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_harvest_server_oaisets_specname_datasets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.harvest.get_api_v1_harvest_server_oaisets_specname_datasets(specname='<value>', key='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `specname`         | *str*              | :heavy_check_mark: | N/A                |
| `key`              | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1HarvestServerOaisetsSpecnameDatasetsResponse](../../models/operations/getapiv1harvestserveroaisetsspecnamedatasetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
