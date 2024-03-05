# Info
(*info*)

### Available Operations

* [get_api_v1_info_api_terms_of_use](#get_api_v1_info_api_terms_of_use)
* [get_api_v1_info_metrics_datasets](#get_api_v1_info_metrics_datasets)
* [get_api_v1_info_metrics_datasets_by_subject](#get_api_v1_info_metrics_datasets_by_subject)
* [get_api_v1_info_metrics_datasets_by_subject_to_month_yyyymm_](#get_api_v1_info_metrics_datasets_by_subject_to_month_yyyymm_)
* [get_api_v1_info_metrics_datasets_monthly](#get_api_v1_info_metrics_datasets_monthly)
* [get_api_v1_info_metrics_datasets_past_days_days_](#get_api_v1_info_metrics_datasets_past_days_days_)
* [get_api_v1_info_metrics_datasets_to_month_yyyymm_](#get_api_v1_info_metrics_datasets_to_month_yyyymm_)
* [get_api_v1_info_metrics_dataverses](#get_api_v1_info_metrics_dataverses)
* [get_api_v1_info_metrics_dataverses_by_category](#get_api_v1_info_metrics_dataverses_by_category)
* [get_api_v1_info_metrics_dataverses_by_subject](#get_api_v1_info_metrics_dataverses_by_subject)
* [get_api_v1_info_metrics_dataverses_monthly](#get_api_v1_info_metrics_dataverses_monthly)
* [get_api_v1_info_metrics_dataverses_past_days_days_](#get_api_v1_info_metrics_dataverses_past_days_days_)
* [get_api_v1_info_metrics_dataverses_to_month_yyyymm_](#get_api_v1_info_metrics_dataverses_to_month_yyyymm_)
* [get_api_v1_info_metrics_downloads](#get_api_v1_info_metrics_downloads)
* [get_api_v1_info_metrics_downloads_monthly](#get_api_v1_info_metrics_downloads_monthly)
* [get_api_v1_info_metrics_downloads_past_days_days_](#get_api_v1_info_metrics_downloads_past_days_days_)
* [get_api_v1_info_metrics_downloads_to_month_yyyymm_](#get_api_v1_info_metrics_downloads_to_month_yyyymm_)
* [get_api_v1_info_metrics_filedownloads](#get_api_v1_info_metrics_filedownloads)
* [get_api_v1_info_metrics_filedownloads_monthly](#get_api_v1_info_metrics_filedownloads_monthly)
* [get_api_v1_info_metrics_filedownloads_to_month_yyyymm_](#get_api_v1_info_metrics_filedownloads_to_month_yyyymm_)
* [get_api_v1_info_metrics_files](#get_api_v1_info_metrics_files)
* [get_api_v1_info_metrics_files_by_type](#get_api_v1_info_metrics_files_by_type)
* [get_api_v1_info_metrics_files_by_type_monthly](#get_api_v1_info_metrics_files_by_type_monthly)
* [get_api_v1_info_metrics_files_monthly](#get_api_v1_info_metrics_files_monthly)
* [get_api_v1_info_metrics_files_past_days_days_](#get_api_v1_info_metrics_files_past_days_days_)
* [get_api_v1_info_metrics_files_to_month_yyyymm_](#get_api_v1_info_metrics_files_to_month_yyyymm_)
* [get_api_v1_info_metrics_make_data_count_metric_](#get_api_v1_info_metrics_make_data_count_metric_)
* [get_api_v1_info_metrics_make_data_count_metric_monthly](#get_api_v1_info_metrics_make_data_count_metric_monthly)
* [get_api_v1_info_metrics_make_data_count_metric_to_month_yyyymm_](#get_api_v1_info_metrics_make_data_count_metric_to_month_yyyymm_)
* [get_api_v1_info_metrics_tree](#get_api_v1_info_metrics_tree)
* [get_api_v1_info_metrics_tree_to_month_yyyymm_](#get_api_v1_info_metrics_tree_to_month_yyyymm_)
* [get_api_v1_info_metrics_uniquedownloads](#get_api_v1_info_metrics_uniquedownloads)
* [get_api_v1_info_metrics_uniquedownloads_monthly](#get_api_v1_info_metrics_uniquedownloads_monthly)
* [get_api_v1_info_metrics_uniquedownloads_to_month_yyyymm_](#get_api_v1_info_metrics_uniquedownloads_to_month_yyyymm_)
* [get_api_v1_info_metrics_uniquefiledownloads](#get_api_v1_info_metrics_uniquefiledownloads)
* [get_api_v1_info_metrics_uniquefiledownloads_monthly](#get_api_v1_info_metrics_uniquefiledownloads_monthly)
* [get_api_v1_info_metrics_uniquefiledownloads_to_month_yyyymm_](#get_api_v1_info_metrics_uniquefiledownloads_to_month_yyyymm_)
* [get_api_v1_info_openapi_output_format_](#get_api_v1_info_openapi_output_format_)
* [get_api_v1_info_server](#get_api_v1_info_server)
* [get_api_v1_info_settings_dataset_publish_popup_custom_text](#get_api_v1_info_settings_dataset_publish_popup_custom_text)
* [get_api_v1_info_settings_max_embargo_duration_in_months](#get_api_v1_info_settings_max_embargo_duration_in_months)
* [get_api_v1_info_settings_incomplete_metadata_via_api](#get_api_v1_info_settings_incomplete_metadata_via_api)
* [get_api_v1_info_version](#get_api_v1_info_version)
* [get_api_v1_info_zip_download_limit](#get_api_v1_info_zip_download_limit)

## get_api_v1_info_api_terms_of_use

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_api_terms_of_use()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1InfoAPITermsOfUseResponse](../../models/operations/getapiv1infoapitermsofuseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_datasets

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_datasets(data_location='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDatasetsResponse](../../models/operations/getapiv1infometricsdatasetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_datasets_by_subject

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_datasets_by_subject(data_location='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDatasetsBySubjectResponse](../../models/operations/getapiv1infometricsdatasetsbysubjectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_datasets_by_subject_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_datasets_by_subject_to_month_yyyymm_(yyyymm='<value>', data_location='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDatasetsBySubjectToMonthYyyymmResponse](../../models/operations/getapiv1infometricsdatasetsbysubjecttomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_datasets_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_datasets_monthly(data_location='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDatasetsMonthlyResponse](../../models/operations/getapiv1infometricsdatasetsmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_datasets_past_days_days_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_datasets_past_days_days_(days=907566, data_location='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDatasetsPastDaysDaysResponse](../../models/operations/getapiv1infometricsdatasetspastdaysdaysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_datasets_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_datasets_to_month_yyyymm_(yyyymm='<value>', data_location='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDatasetsToMonthYyyymmResponse](../../models/operations/getapiv1infometricsdatasetstomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_dataverses

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_dataverses(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDataversesResponse](../../models/operations/getapiv1infometricsdataversesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_dataverses_by_category

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_dataverses_by_category(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDataversesByCategoryResponse](../../models/operations/getapiv1infometricsdataversesbycategoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_dataverses_by_subject

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_dataverses_by_subject(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDataversesBySubjectResponse](../../models/operations/getapiv1infometricsdataversesbysubjectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_dataverses_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_dataverses_monthly(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDataversesMonthlyResponse](../../models/operations/getapiv1infometricsdataversesmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_dataverses_past_days_days_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_dataverses_past_days_days_(days=123806, parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDataversesPastDaysDaysResponse](../../models/operations/getapiv1infometricsdataversespastdaysdaysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_dataverses_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_dataverses_to_month_yyyymm_(yyyymm='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDataversesToMonthYyyymmResponse](../../models/operations/getapiv1infometricsdataversestomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_downloads

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_downloads(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDownloadsResponse](../../models/operations/getapiv1infometricsdownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_downloads_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_downloads_monthly(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDownloadsMonthlyResponse](../../models/operations/getapiv1infometricsdownloadsmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_downloads_past_days_days_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_downloads_past_days_days_(days=646171, parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDownloadsPastDaysDaysResponse](../../models/operations/getapiv1infometricsdownloadspastdaysdaysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_downloads_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_downloads_to_month_yyyymm_(yyyymm='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsDownloadsToMonthYyyymmResponse](../../models/operations/getapiv1infometricsdownloadstomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_filedownloads

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_filedownloads(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFiledownloadsResponse](../../models/operations/getapiv1infometricsfiledownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_filedownloads_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_filedownloads_monthly(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFiledownloadsMonthlyResponse](../../models/operations/getapiv1infometricsfiledownloadsmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_filedownloads_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_filedownloads_to_month_yyyymm_(yyyymm='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFiledownloadsToMonthYyyymmResponse](../../models/operations/getapiv1infometricsfiledownloadstomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_files

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_files(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFilesResponse](../../models/operations/getapiv1infometricsfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_files_by_type

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_files_by_type(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFilesByTypeResponse](../../models/operations/getapiv1infometricsfilesbytyperesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_files_by_type_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_files_by_type_monthly(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFilesByTypeMonthlyResponse](../../models/operations/getapiv1infometricsfilesbytypemonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_files_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_files_monthly(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFilesMonthlyResponse](../../models/operations/getapiv1infometricsfilesmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_files_past_days_days_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_files_past_days_days_(days=112599, parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFilesPastDaysDaysResponse](../../models/operations/getapiv1infometricsfilespastdaysdaysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_files_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_files_to_month_yyyymm_(yyyymm='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsFilesToMonthYyyymmResponse](../../models/operations/getapiv1infometricsfilestomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_make_data_count_metric_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_make_data_count_metric_(metric='<value>', country='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsMakeDataCountMetricResponse](../../models/operations/getapiv1infometricsmakedatacountmetricresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_make_data_count_metric_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_make_data_count_metric_monthly(metric='<value>', country='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsMakeDataCountMetricMonthlyResponse](../../models/operations/getapiv1infometricsmakedatacountmetricmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_make_data_count_metric_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_make_data_count_metric_to_month_yyyymm_(metric='<value>', yyyymm='<value>', country='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsMakeDataCountMetricToMonthYyyymmResponse](../../models/operations/getapiv1infometricsmakedatacountmetrictomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_tree

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_tree(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsTreeResponse](../../models/operations/getapiv1infometricstreeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_tree_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_tree_to_month_yyyymm_(yyyymm='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsTreeToMonthYyyymmResponse](../../models/operations/getapiv1infometricstreetomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_uniquedownloads

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_uniquedownloads(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsUniquedownloadsResponse](../../models/operations/getapiv1infometricsuniquedownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_uniquedownloads_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_uniquedownloads_monthly(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsUniquedownloadsMonthlyResponse](../../models/operations/getapiv1infometricsuniquedownloadsmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_uniquedownloads_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_uniquedownloads_to_month_yyyymm_(yyyymm='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsUniquedownloadsToMonthYyyymmResponse](../../models/operations/getapiv1infometricsuniquedownloadstomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_uniquefiledownloads

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_uniquefiledownloads(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsUniquefiledownloadsResponse](../../models/operations/getapiv1infometricsuniquefiledownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_uniquefiledownloads_monthly

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_uniquefiledownloads_monthly(parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsUniquefiledownloadsMonthlyResponse](../../models/operations/getapiv1infometricsuniquefiledownloadsmonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_metrics_uniquefiledownloads_to_month_yyyymm_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_metrics_uniquefiledownloads_to_month_yyyymm_(yyyymm='<value>', parent_alias='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetAPIV1InfoMetricsUniquefiledownloadsToMonthYyyymmResponse](../../models/operations/getapiv1infometricsuniquefiledownloadstomonthyyyymmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_openapi_output_format_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_openapi_output_format_(output_format='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `output_format`    | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetAPIV1InfoOpenapiOutputFormatResponse](../../models/operations/getapiv1infoopenapioutputformatresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_server

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_server()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1InfoServerResponse](../../models/operations/getapiv1infoserverresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_settings_dataset_publish_popup_custom_text

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_settings_dataset_publish_popup_custom_text()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1InfoSettingsDatasetPublishPopupCustomTextResponse](../../models/operations/getapiv1infosettingsdatasetpublishpopupcustomtextresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_settings_max_embargo_duration_in_months

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_settings_max_embargo_duration_in_months()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1InfoSettingsMaxEmbargoDurationInMonthsResponse](../../models/operations/getapiv1infosettingsmaxembargodurationinmonthsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_settings_incomplete_metadata_via_api

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_settings_incomplete_metadata_via_api()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1InfoSettingsIncompleteMetadataViaAPIResponse](../../models/operations/getapiv1infosettingsincompletemetadataviaapiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_version

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_version()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1InfoVersionResponse](../../models/operations/getapiv1infoversionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_info_zip_download_limit

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.info.get_api_v1_info_zip_download_limit()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1InfoZipDownloadLimitResponse](../../models/operations/getapiv1infozipdownloadlimitresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
